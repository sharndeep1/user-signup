from flask import Flask, request, render_template
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
	
	return render_template('index.html',username='',user_error='',password_error='',verify_error='',email='',email_error='')
	#return form.format(username='',user_error='',password_error='',verify_error='',email='',email_error='')

@app.route('/',methods=['POST'])
def validateform():
	n=(request.form['username'])
	p=(request.form['password'])
	v=(request.form['verify'])
	e=(request.form['email'])
	user_error=''
	password_error=''
	verify_error=''
	email_error=''	
	
	if 	n=='':
		user_error='username should not be blank'
	elif n.find(' ')!=-1 or len(n)<3 or len(n)>20:
	       user_error='invalid usename'
	
	if 	p=='':
        	password_error='password should not be blank'
	
	elif 	p.find(' ')!=-1 or len(p)<3 or len(p)>20:
	       password_error='invalid password'	
	if 	v=='':
		verify_error='verify field should not blank'
	elif    p != v:
		verify_error='password doesnot match'
	if	len(e)>0:	
		if 	e.find(' ')!=-1 or (e.count('@')>1 or e.count('@')<1) or (e.count('.')>1 or e.count('.')<1):
			email_error='Invalid email id'
		
				
	if 	not user_error and not password_error and not verify_error and not email_error:
		return render_template("welcome.html",username=n) 
	else:		
		return render_template("index.html",username=n,user_error=user_error,password_error=password_error,verify_error=verify_error,email=e,email_error=email_error)
		#return  form.format(username=n,user_error=user_error,password_error=password_error,verify_error=verify_error,email=e,email_error=email_error)
app.run()