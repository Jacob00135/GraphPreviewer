import os
import paramiko
from flask import current_app, g
from config import root_path


def get_ssh_client():
    if 'ssh' in g:
        return g.ssh

    g.ssh = paramiko.SSHClient()
    g.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    g.ssh.connect(
        hostname=current_app.config['REMOTE_SERVER_HOSTNAME'],
        port=current_app.config['REMOTE_SERVER_SSH_PORT'],
        username=current_app.config['REMOTE_SERVER_USERNAME'],
        password=current_app.config['REMOTE_SERVER_PASSWORD']
    )

    return g.ssh


def close_ssh_connection(e=None):
    if 'ssh' in g:
        ssh = g.pop('ssh')
        ssh.close()


def draw_graph():
    # 执行命令并获取输出
    ssh = get_ssh_client()
    command = current_app.config['REMOTE_COMMAND']
    stdin, stdout, stderr = ssh.exec_command(command)
    execute_error = stderr.read().decode()
    print('=' * 80)
    print(execute_error)
    print(stdout.read().decode())
    print('=' * 80)

    # 获取图片名称
    remote_graph_path = current_app.config['REMOTE_SERVER_GRAPH_PATH']
    command = 'ls {}'.format(remote_graph_path)
    stdin, stdout, stderr = ssh.exec_command(command)
    filenames = stdout.read().decode().split('\n')
    filenames = [fn for fn in filenames if fn != '']

    # 获取文件
    sftp = ssh.open_sftp()
    try:
        for fn in filenames:
            sftp.get(
                os.path.join(remote_graph_path, fn).replace('\\', '/'),
                os.path.join(root_path, 'static/images', fn).replace('/', '\\')
            )
    except Exception as e:
        print('=' * 80)
        print(e)
        print('=' * 80)
    finally:
        sftp.close()

    return filenames, execute_error


def delete_all_image():
    image_path = os.path.join(root_path, 'static/images')
    for fn in os.listdir(image_path):
        fp = os.path.join(image_path, fn)
        try:
            os.remove(fp)
        except Exception as e:
            print(e)
