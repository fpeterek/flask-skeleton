import re

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField, FloatField
from wtforms.validators import EqualTo, Email, InputRequired, Length, NumberRange

from ..data.models import User, LogUser
from ..fields import Predicate


def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)


def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)


def safe_characters(s):
    """ Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator """
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None


class LogUserForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')


class AddItems(Form):

    name = TextField('Item name', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=3, max=50, message="Please use between 3 and 50 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    amount = IntegerField('Item count', validators=[InputRequired(message="You can't leave this empty"),
                                                    NumberRange(min=0,
                                                                message="Item count can't be lower than zero. ")])
    price = FloatField('Item price', validators=[InputRequired(message="You can't leave this empty"),
                                                 NumberRange(min=0,
                                                             message="Item price can't be lower than zero. ")])


class RemoveItems(Form):

    id = IntegerField('Item ID', validators=[InputRequired(message="You can't leave this empty"),
                                             NumberRange(min=0,
                                                         message="Item ID can't be lower than zero. ")])
