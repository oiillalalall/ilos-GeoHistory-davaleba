from ext import db, app
from flask import render_template, request, redirect, url_for
from forms import registerForm, HistoryForm
from os import path
from models import History

profiles = []


page = {
    "ალავერდი": "/geohistory/1",
    "კაცხის სვეტი": "/geohistory/2",
    "უფლისციხე": "/geohistory/3",

}

@app.route('/')
def home():
    geohistory = History.query.all()
    return render_template('index.html', geohistory=geohistory, role="admin")

@app.route('/profile/<int:id>')
def profile(id):
    profile = profiles[id]
    return render_template('profile.html', profile=profile)

@app.route('/search')
def search():
    search_text = request.args.get('text')

    if not search_text:
        return redirect(url_for("home"))

    search_text = search_text.lower().strip()

    if search_text in page:
        return redirect((page[search_text]))

    return redirect(url_for("home"))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add_history', methods=["GET",'POST'])
def add_history():
    form = HistoryForm()
    if form.validate_on_submit():
        new_history = History(history_title = form.history_title.data, description = form.description.data)
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            new_history.image = img.filename

        db.session.add(new_history)
        db.session.commit()
    return render_template("add_history.html", form=form)


@app.route("/delete_history/<int:id>")
def delete_history(id):
    history = History.query.get(id)
    db.session.delete(history)
    db.session.commit()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "password": form.password.data,
            "email": form.email.data,
            "mobile": form.mobile.data,
            "date": form.birthdate.data,
            "gender": form.gender.data,
            "country": form.country.data
        }
        profiles.append(new_user)
        print(new_user)
    return render_template('register.html', form=form)

@app.route('/geohistory/<int:geo_id>')
def see_geo(geo_id):
    geo = History.query.get(geo_id)
    return render_template('geohistory.html', place=geo)