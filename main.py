from flask import Flask, render_template
from user.app import user, User

app = Flask(__name__)

print(User.greeting_user(user))
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", name=User.greeting_user(user))


if __name__ == '__main__':
    app.run(debug=True)
