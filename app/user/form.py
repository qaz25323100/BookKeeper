from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, PasswordField, SubmitField, SelectField
from wtforms import validators
from app.Entity.Kinda import Kinda


class FormLogin(FlaskForm):
    """
    使用者登入使用
    以email為主要登入帳號，密碼需做解碼驗證
    記住我的部份透過flask-login來實現
    """

    phone = StringField('Phone', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
    ])

    password = PasswordField('PassWord', validators=[
        validators.DataRequired()
    ])

    submit = SubmitField('Log in')

class FormNewKeeper(FlaskForm):
    kindas_select = Kinda.query.all()
    kindas = SelectField(u'用途種類', choices=[kinda.kindas for kinda in kindas_select])
    money = IntegerField(u'金額')

    submit = SubmitField('新增')
    prevpage = SubmitField('上一頁')

