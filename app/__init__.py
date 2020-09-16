from flask import Flask, session, redirect, url_for, request, flash, render_template
from app import planisphere
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from app.parser import parse_sentence, scan
from app.planisphere import Room
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Input(FlaskForm):
    player_input = StringField(validators=[DataRequired()])
    submit = SubmitField()

@app.route('/')
def index():
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    room = Room.room_list.get(room_name)
    form = Input()
    
    if form.validate_on_submit():
        player_input = parse_sentence(scan(form.player_input.data))
        next_room = room.go(f'{player_input}')
        error = planisphere.set_error(room_name, player_input)
        
        if next_room == room.death:
            return render_template("you_died.html", room=next_room)
        
        elif next_room == planisphere.the_end:
            return render_template("the_end.html", room=next_room)
        
        elif next_room == planisphere.code:
            return render_template("note.html", code=planisphere.code)
        
        if next_room:
            session['room_name'] = planisphere.name_room(next_room)
            room = next_room
        
        else:
            flash(error)
            return render_template("show_room.html", room=room, form=form)
    
    return render_template("show_room.html", room=room, form=form)






