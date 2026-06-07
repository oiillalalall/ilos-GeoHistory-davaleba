from ext import db, app
from flask import render_template, request, redirect, url_for, flash
from forms import registerForm, HistoryForm, LoginForm
from os import path
from models import History, Review, User
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def home():
    geohistory = History.query.all()
    return render_template('index.html', geohistory=geohistory, role="admin")

@app.route('/profile')
def profile():
    return render_template('profile.html', profile=current_user)

@app.route('/search')
def search():
    search_text = request.args.get('text')

    if not search_text:
        return redirect(url_for("home"))

    results = History.query.filter(
        History.history_title.ilike(f'%{search_text}%')
    ).all()

    return render_template('index.html', geohistory=results, role="admin")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter(User.username == form.username.data).first()
    if user:
        login_user(user)
        flash("ოოო ბრავო ბოოოსსს შენ დარეგისტრირდი Geo History-ში")
        return redirect("/")
    return render_template('login.html', form=form)

@app.route('/add_history', methods=["GET",'POST'])
@login_required
def add_history():
    form = HistoryForm()
    if form.validate_on_submit():
        new_history = History(history_title = form.history_title.data, description = form.description.data)
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            new_history.image = img.filename

        new_history.create()
        return redirect("/")
    return render_template("add_history.html", form=form)

@app.route('/edit_history/<int:id>', methods=['GET', 'POST'])
def edit_history(id):
    history = History.query.get(id)
    form = HistoryForm(history_title=history.history_title, description=history.description)
    if form.validate_on_submit():
        history.history_title = form.history_title.data
        history.description = form.description.data
        img = form.image.data
        if img:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            history.image = img.filename

        history.save()
        return redirect("/")
    return render_template("edit_history.html", form=form)


@app.route("/delete_history/<int:id>")
def delete_history(id):
    history = History.query.get(id)
    history.delete()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()
        return redirect("/")
    return render_template('register.html', form=form)

@app.route('/geohistory/<int:geo_id>')
def see_geo(geo_id):
    geo = History.query.get(geo_id)
    reviews = Review.query.filter(Review.history_id == geo_id).all()
    return render_template('geohistory.html', place=geo, reviews=reviews)

@app.route('/logout')
def log_out():
    logout_user()
    return redirect("/")