from web.app import create_module
from flask import render_template


app = create_module(__name__)


@app.route('/')
def index():
    return render_template('www/index.html')
