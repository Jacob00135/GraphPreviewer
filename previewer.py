import os
import sys
from flask import Flask, render_template, request
from config import root_path, Config
from utils import close_ssh_connection, draw_graph, delete_all_image

app = Flask(__name__)
app.config.from_object(Config)
app.teardown_appcontext(close_ssh_connection)


@app.route('/')
def index():
    if str(request.args.get('repaint', '0')) == '1':
        delete_all_image()
        filenames, execute_error = draw_graph()
    else:
        filenames = os.listdir(os.path.join(root_path, 'static/images'))
        execute_error = ''
    
    if execute_error != '':
        filenames = []

    return render_template(
        'index.html',
        image_filenames=filenames,
        execute_error=execute_error
    )
