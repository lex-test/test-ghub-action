#---------------------------------------------------------------------
# This is copy project adv4000/github-actions-part-2-cicd-to-aws
# Thanks for example application
#---------------------------------------------------------------------

from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")

@application.route("/help")
def helppage():
    return render_template("help.html")

@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v0.0.1"

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------