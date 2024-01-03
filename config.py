import os

root_path = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    SECRET_KEY = os.urandom(16)

    REMOTE_SERVER_HOSTNAME = os.environ.get('REMOTE_SERVER_HOSTNAME')
    REMOTE_SERVER_USERNAME = os.environ.get('REMOTE_SERVER_USERNAME')
    REMOTE_SERVER_PASSWORD = os.environ.get('REMOTE_SERVER_PASSWORD')
    REMOTE_SERVER_SSH_PORT = int(os.environ.get('REMOTE_SERVER_SSH_PORT', 22))
    REMOTE_SERVER_GRAPH_PATH = os.environ.get('REMOTE_SERVER_GRAPH_PATH')

    COMMAND_MAPPING = {
        'full': 'python /home/xjy/python_code/TransMF_AD/draw_graph.py --category full',
        'magnify': 'python /home/xjy/python_code/TransMF_AD/draw_graph.py --category magnify',
        'subplot': 'python /home/xjy/python_code/TransMF_AD/draw_graph.py --category subplot'
    }
