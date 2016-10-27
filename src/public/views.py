"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template,url_for,request,redirect
from .forms import LogUserForm, AddItems, RemoveItems
from ..data.database import db
from ..data.models import LogUser
from ..data.models.additem import AddItem
blueprint = Blueprint('public', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')


@blueprint.route('/loguserinput', methods=['GET', 'POST'])
def insert_log_user():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)


@blueprint.route('/loguserlist', methods=['GET'])
def list_user_log():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl", data=pole)


@blueprint.route('/manageitems', methods=['GET', 'POST'])
def manage_items():
    add_form = AddItems()
    if add_form.validate_on_submit():
        AddItem.create(**add_form.data)

    # Remove items

    form = RemoveItems()
    if form.validate_on_submit():
        id_value = form.data["id"]
        if type(id_value) != int:
            return render_template('public/removeerror.tmpl', id="ID isn't an integer, LUL  ")
        try:
            to_remove = db.session.query(AddItem).filter_by(id=id_value).first()
            db.session.delete(to_remove)
            db.session.commit()
        except:
            return render_template('public/removeerror.tmpl', id=id_value)
    # return render_template('public/removeitems.tmpl', form=form)

    return render_template("public/additemsnew.tmpl", add_form=add_form, form=form)


@blueprint.route('/additems', methods=['GET', 'POST'])
def add_items():
    form = AddItems()
    if form.validate_on_submit():
        AddItem.create(**form.data)
    return render_template("public/additems.tmpl", form=form)


@blueprint.route('/listitems', methods=['GET', 'POST'])
def list_items():
    data = db.session.query(AddItem).all()
    return render_template("public/listitems.tmpl", data=data)


@blueprint.route('/removeitems', methods=['GET', 'POST'])
def remove_items():
    form = RemoveItems()
    if form.validate_on_submit():
        id_value = form.data["id"]
        if type(id_value) != int:
            return render_template('public/removeerror.tmpl', id="ID isn't an integer, LUL  ")
        try:
            to_remove = db.session.query(AddItem).filter_by(id=id_value).first()
            db.session.delete(to_remove)
            db.session.commit()
        except:
            return render_template('public/removeerror.tmpl', id=id_value)
    return render_template('public/removeitems.tmpl', form=form)
