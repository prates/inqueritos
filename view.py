from datetime import datetime, timedelta

from flask import request, Flask, render_template
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.core import DateField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = 'you-will-never-guess'

db = SQLAlchemy(app)


class Inquerito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bandido = db.Column(db.String(80), nullable=False)
    vitima = db.Column(db.String(80), nullable=False)
    data_abertura = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)

        

class ControllerInquerito():

    def salva_inquerito(vitima, bandido, data_abertura_str):
        data_abertura = datetime.strptime(data_abertura_str, "%d/%m/%Y")
        data_vencimento = data_abertura + timedelta(days=30)
        inquerito = Inquerito(bandido=bandido, vitima=vitima, 
                            data_abertura=data_abertura,
                            data_vencimento=data_vencimento)
        db.session.add(inquerito)
        db.commit()

    def lista_inqueritos():
        inqueritos = Inquerito.query.all()
        return inqueritos            

    def prorroga_inquerito(inquerito_id):
        inquerito = Inquerito.query.filter_by(id=inquerito_id).first()
        



class FormInquerito(FlaskForm):
    vitima = StringField("vitima", validators=[DataRequired()])
    bandido = StringField("bandido", validators=[DataRequired()])
    data_inquerito = DateField("data_inquerito")
    submit = SubmitField("Criar Inquerito")


@app.route('/', methods=['POST', 'GET'])
def novo_inquerito():
    form = FormInquerito()
    if request.method == "POST":
        vitima = request.form["vitima"]
        bandido = request.form["bandido"]
        data_inquerito = request.form["data_inquerito"]
        controller = ControllerInquerito()

    return render_template("cria_inquerito.html", form=form)



app.run(host="0.0.0.0", port=4444)