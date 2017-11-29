from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)

app = Flask(__name__)



@app.route('/')
def index():
    template = jinja_env.get_template('home.html')
    place_holder = ''
    return template.render()
 

@app.route('/', methods=['POST'])
def validate():
 
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['verify']
    email = request.form['email']


    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''

    if username.isalnum():
        a=0
    else:
        username_error = 'Username cannot be empty or have spaces in it.'
        username = ''
        
        
    if  password.isalnum():
        a=0
    else:
        password_error = 'Password cannot be empty or have spaces in it.'
        password = ''

    if  vpassword.isalnum():
        a=0
    else:
        vpassword_error = 'Field cannot be empty or have spaces in it.'
        verify = ''

    if len(username) < 3 or len(username) > 20:
        username_error = 'Username must be 3 to 20 characters long'
        

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be 3 to 20 characters long'
        

    if password != vpassword:
        vpassword_error = 'Password and verification did not match.'
        

    if len(email) > 0:
        if len(email) < 3 or len(email) > 20:
            email_error = 'Please provide a valid email that is between 3-20 characters long with no spaces '
        if (' ' in email):
            email_error = 'Please provide a valid email that is between 3-20 characters long with no spaces '
        if ('@' in email):
            if email.count("@") > 1:
                email_error = 'Please provide a valid email that is between 3-20 characters long with no spaces @ issue to many'
        else:
            email_error = 'Please provide a valid email that is between 3-20 characters long with no spaces - @ issue none'
        if ('.' in email):
            if email.count(".") > 1:
                email_error = 'Please provide a valid email that is between 3-20 characters long with no spaces - period issue to many'
        else:
            email_error = 'Please provide a valid email that is between 3-20 characters long with no spaces - period issue none'

        

    if not username_error and not password_error and not vpassword_error and not email_error:
        return redirect('/valid-user?username={0}'.format(username))

    else:
        template = jinja_env.get_template('home.html')
        return template.render(username_error=username_error,
            password_error=password_error,vpassword_error=vpassword_error,
            email_error=email_error,
            username=username,email=email)

@app.route('/valid-user')
def valid_user():
    name = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(name=name)
    
if __name__ == "__main__":
    app.run(debug=True)
