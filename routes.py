import werkzeug
from flask import redirect, url_for, abort, session, request
from flask.templating import render_template
from validators import url as UrlValidator

from URLForm import URLForm
from app import app
from shortUrlHandler import ShortURL

UrlProcessor = ShortURL()


# Homepage ↓
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    urlForm = URLForm()
    if urlForm.validate_on_submit():
        longURL: str = urlForm.longURL.data.strip()
        if not longURL.startswith('http'):
            longURL = f'https://{longURL}'
        if UrlValidator(longURL):
            session.permanent = True
            session['longURL'] = longURL
            return redirect(url_for('shortener'))
        else:
            return redirect(url_for('invalidUrl'))
    return render_template(
        'index.html.jinja2',
        form=urlForm
    )


# Shortener Page ↓
@app.route('/shortener', methods=['GET'])
def shortener():
    try:
        longURL: str = session['longURL']
        shortURL: str = UrlProcessor.getShortURL(longURL=longURL)
        session['shortURL'] = shortURL
        return render_template(
            'shortener.html.jinja2',
            longURL=longURL,
            shortURL=f'{request.host}/{shortURL}'
        )
    except KeyError:
        abort(404)


# Short URL Redirect Page ↓
@app.route('/<short_url>', methods=['GET'])
def short_url_redirect(short_url):
    if len(short_url) != 7:
        abort(404)
    URL = UrlProcessor.getLongURL(short_url=short_url)
    if URL is None:
        return redirect(url_for('invalidUrl'))
    else:
        return redirect(URL, code=307)


# Bad Request Page ↓
@app.route('/invalid-url', methods=['GET'])
def invalidUrl():
    error_message: list = [
        'An error occurred to generate the URL',
        'The <b>URL is not valid</b>, make sure the URL you tried to shorten is correct.'
    ]
    error_code: int = 406
    return render_template(
        'error.html.jinja2',
        error_message=error_message
    ), error_code


# 404 Page ↓
@app.errorhandler(404)
def pageNotFound(error: werkzeug.exceptions.NotFound):
    error_message: list = error.__str__().split(':')
    error_code: int = error.code
    return render_template(
        'error.html.jinja2',
        error_message=error_message
    ), error_code


if __name__ == '__main__':
    print('Hello World')
