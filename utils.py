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


def draw_graph(category):
    # 执行命令并获取输出
    ssh = get_ssh_client()
    command = current_app.config['COMMAND_MAPPING'][category]
    stdin, stdout, stderr = ssh.exec_command(command)
    exec_command_out = stdout.read().decode()
    print('=' * 80)
    print(exec_command_out)
    print('=' * 80)

    # 获取图片路径
    remote_graph_path = current_app.config['REMOTE_SERVER_GRAPH_PATH']
    command = 'ls {}'.format(remote_graph_path)
    stdin, stdout, stderr = ssh.exec_command(command)
    exec_command_out = stdout.read().decode()
    image_filenames = []
    image_fullpaths = []
    for row in exec_command_out.split('\n'):
        if row.startswith(category):
            image_filenames.append(row)
            image_fullpaths.append(os.path.join(remote_graph_path, row).replace('\\', '/'))

    # 获取文件
    sftp = ssh.open_sftp()
    try:
        for filename, fullpath in zip(image_filenames, image_fullpaths):
            local_path = os.path.join(root_path, 'static/images/{}'.format(filename)).replace('/', '\\')
            sftp.get(fullpath, local_path)
    except Exception as e:
        print('=' * 80)
        print(e)
        print('=' * 80)
    finally:
        sftp.close()

    return image_filenames, image_fullpaths


def get_filenames(category):
    graph_path = os.path.join(root_path, 'static/images')
    remote_graph_path = current_app.config['REMOTE_SERVER_GRAPH_PATH']
    image_filenames = []
    image_fullpaths = []
    for filename in os.listdir(graph_path):
        if filename.startswith(category):
            image_filenames.append(filename)
            image_fullpaths.append(os.path.join(remote_graph_path, filename).replace('\\', '/'))

    return image_filenames, image_fullpaths
