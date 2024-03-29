from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kacper'}
    drones = [
        {'name':{'username':'Mavic 2'},
         'price':'1500€'},

        {'name':{'username':'Mavic 3'},
         'price':'2000€'}
    ]
    return render_template('index.html',title='Home',user=user, drones = drones) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)