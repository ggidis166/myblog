import wtforms
from wtforms.validators import Length, InputRequired


class LoginForm(wtforms.Form):
    password = wtforms.StringField(validators=[Length(min=3, max=20, message='密码错误'), InputRequired(message='请输入密码')])