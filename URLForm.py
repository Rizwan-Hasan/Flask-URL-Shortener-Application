from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators


class URLForm(FlaskForm):
    longURL = StringField(
        'Enter the link here',
        validators=[
            validators.DataRequired(),
        ],
        render_kw={
            'placeholder': 'Enter the link here'
        }
    )
    submit = SubmitField(
        'Shorten URL',
        render_kw={
            'value': 'Shorten URL'
        }
    )


if __name__ == '__main__':
    print('Hello World')
