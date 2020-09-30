from app import planisphere, app, db
from app.parser import parse_sentence, scan
from app.planisphere import Room
from app.models import User
from flask import session, redirect, url_for, flash, render_template, request
from app.forms import Input, LoginForm, RegisterForm 
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("welcome"))
    
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()

        if user and user.check_password(login_form.password.data):
            login_user(user, remember=login_form.remember_me.data)
            next_page = request.args.get('next')

            if next_page and url_parse(next_page).netloc == '':
                return redirect(next_page)
                 
            return redirect(url_for("welcome"))

        flash("Invalid username or password")
        return redirect(url_for("login"))

    return render_template("login.html", form=login_form)

@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        new_user = User(username=register_form.username.data)
        new_user.set_password(register_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("You have successfully registered!")
        
        return redirect(url_for('login'))
    
    return render_template("register.html", form=register_form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("welcome"))

@app.route("/play")
@login_required
def play():
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



