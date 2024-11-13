from flask import Blueprint, render_template, request, redirect, session
from .forms import LoginForm
from models import UserModel

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            password = form.password.data
            res = UserModel.query.filter_by(id='1', password=password).first()
            if res:
                session['user_id'] = res.id
                return redirect('/')
            else:
                return redirect('/auth/login')
        else:
            return redirect('/auth/login')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')