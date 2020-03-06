from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators


class InputData(FlaskForm):
    """
    Retrieves the user input using a form.
    """

    price = IntegerField('Price (£)', [validators.NumberRange(min=0)])
    date_from = StringField('From (MM/YYYY)')
    date_to = StringField('To (MM/YYYY)')
    borough = StringField('Borough')
