
from flask import Flask,render_template,send_from_directory
from Member import *
from User import *
from Api import *
from config import *
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "anyvalue"
app.permanent_session_lifetime = timedelta(minutes=5)
app.register_blueprint(member)
app.register_blueprint(user)
app.register_blueprint(memberapi)

@app.route("/")
def Index():
    if "username" not in session:
        return render_template("login/login.html",headername="Login")
    else:
        return redirect(url_for('member.Showdatamember'))

@app.route('/static/images/<filename>')
def protect(filename):
    if "username" not in session:
        return "You can't copy this picture"
    return send_from_directory("static/images",filename)

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for("notfound"))

@app.route("/notfound")
def notfound():
    return render_template('error/error.html')



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="5005")
