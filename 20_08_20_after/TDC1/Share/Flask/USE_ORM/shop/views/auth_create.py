from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from shop import db
from shop.forms import UserCreateForm
from shop.models import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        user2 = User.query.filter_by(email=form.email.data).first()
        print(user2)
        if not user2 and not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('hm.index'))
        elif user:
            flash('이미 존재하는 사용자입니다.')
        else:
            flash('이미 존재하는 이메일입니다.')
    return render_template('signup.html', form=form)