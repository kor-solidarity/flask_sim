from flask_blog import app


@app.route('/index')
def index(page_num=0):
    return