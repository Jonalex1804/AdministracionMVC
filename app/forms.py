from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
<<<<<<< HEAD
from wtforms.validators import  InputRequired, DataRequired
=======
from wtforms.validators import DataRequired
>>>>>>> d97651a80dbbcd304d728757b633b57fcea39c18

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class DebtForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    amount = FloatField('Monto total', validators=[DataRequired()])
<<<<<<< HEAD
    abono = FloatField('Monto abonado', validators=[InputRequired()])
    due_date = DateField('Fecha de vencimiento', format='%Y-%m-%d', validators=[], render_kw={"placeholder": "YYYY-MM-DD"})
    submit = SubmitField('Guardar')
    
=======
    abono = FloatField('Monto abonado', validators=[DataRequired()])
    due_date = DateField('Fecha de vencimiento', format='%Y-%m-%d', validators=[], render_kw={"placeholder": "YYYY-MM-DD"})
    submit = SubmitField('Guardar')
>>>>>>> d97651a80dbbcd304d728757b633b57fcea39c18
