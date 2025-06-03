from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import  InputRequired, DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class DebtForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    amount = FloatField('Monto total', validators=[DataRequired()])
    abono = FloatField('Monto abonado', validators=[InputRequired()])
    due_date = DateField('Fecha de vencimiento', format='%Y-%m-%d', validators=[], render_kw={"placeholder": "YYYY-MM-DD"})
    submit = SubmitField('Guardar')
    