from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
import random

app = Flask(__name__)

# Configure secret key for session
app.config['SECRET_KEY'] = 'your_secret_key'

# Create a list of possible CAPTCHA strings
captcha_strings = ['A', 'B', 'C', 'D', 'E']

# CAPTCHA length (number of characters)
captcha_length = 6

# Create a WTForms form for login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

# CAPTCHA route
@app.route('/captcha')
def captcha():
    # Generate a random CAPTCHA string
    captcha_text = ''.join(random.choice(captcha_strings) for _ in range(captcha_length))

    # Store the CAPTCHA string in the session
    session['captcha'] = captcha_text

    return captcha_text

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        entered_captcha = request.form.get('captcha_input')

        # Verify CAPTCHA
        if session.get('captcha') == entered_captcha:
            # Check username and password (replace with your own authentication logic)
            if username == 'admin' and password == 'password123':  # Updated the password
                return 'Login successful!'
            else:
                return 'Invalid username or password.'
        else:
            return 'CAPTCHA verification failed.'

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
