import os
import sys
from flask import Flask, render_template, request
from config import root_path, Config
from utils import close_ssh_connection, draw_graph, get_image_filenames, remove_all_image

app = Flask(__name__)
app.config.from_object(Config)
app.teardown_appcontext(close_ssh_connection)


@app.route('/')
def index():
    category = request.args.get('category', 'full')
    if category not in app.config['COMMAND_MAPPING']:
        category = 'full'

    if str(request.args.get('repaint', '0')) == '1':
        image_filenames = draw_graph(category)
    else:
        remove_all_image(category)
        image_filenames = get_image_filenames(category)

    return render_template(
        'index.html',
        category=category,
        image_filenames=image_filenames
    )
