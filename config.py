import os

root_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(root_path, 'static/images')):
    os.mkdir(os.path.join(root_path, 'static/images'))


class Config(object):
    SECRET_KEY = os.urandom(16)

    REMOTE_SERVER_HOSTNAME = os.environ.get('REMOTE_SERVER_HOSTNAME')
    REMOTE_SERVER_USERNAME = os.environ.get('REMOTE_SERVER_USERNAME')
    REMOTE_SERVER_PASSWORD = os.environ.get('REMOTE_SERVER_PASSWORD')
    REMOTE_SERVER_SSH_PORT = int(os.environ.get('REMOTE_SERVER_SSH_PORT', 22))
    REMOTE_SERVER_GRAPH_PATH = os.environ.get('REMOTE_SERVER_GRAPH_PATH')
    REMOTE_COMMAND = os.environ.get('REMOTE_COMMAND')
