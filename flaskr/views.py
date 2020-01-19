from flask import Blueprint, render_template, abort, current_app
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page':'index'})
@simple_page.route('/<page>')
def show(page):
    current_app.logger.info('matched!')
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound as e:
        current_app.logger.error(e)
        abort(404)
