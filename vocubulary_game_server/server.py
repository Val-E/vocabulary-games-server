import math
# import json
# from pymongo import MongoClient
from flask import Flask, url_for, request, render_template
# from OpenSSL import SSL

# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_certificate('add cert')
# context.use_privatekey('add privatekey')

# Todo: Add a database.
# cluster = MongoClient(
# "mongodb+srv://")
# db = cluster["vocabulary-game"]
# collection = db["vocabulary-game"]


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    return render_template("home.html", title="Vocabulary Game")


@app.route("/create/<game>", methods=["POST", "GET"])
def create(game):
    if request.method == "POST":
        try:
            num1 = math.fabs(int(request.form["num1"]))
            num2 = math.fabs(int(request.form["num2"]))
            game_id = request.form["game_id"]
        except ValueError:
            return render_template("error.html",
                                   title="Bad Input",
                                   errormsg="Looks like something went wrong. Check your inputs."), 404

        if num1 == 0 or num2 == 0:
            return render_template("error.html",
                                   title="Bad Input",
                                   errormsg="Looks like something went wrong. Check your inputs."), 404
        if num1*num2 > 625:
            return render_template("error.html",
                                   title="Bad Input",
                                   errormsg="You are limited to 625 cells! "), 404

        game_code = 'game_id===' + str(game_id) + ';;; ' + \
                    'game_type===' + str(game) + ';;; ' + \
                    'num1===' + str(num1) + ';;; ' + \
                    'num2===' + str(num2) + ';;; '

        try:
            if game == "quiz":
                for i in range(int(num1)):
                    game_code += 'category' + str(i+1) + '===' + str(request.form["category"+str(i+1)]) + ';;; '

                for i in range(int(num1 * num2)):
                    game_code += 'question' + str(i+1) + '===' + str(request.form["question"+str(i+1)]) + ';;; '

                for i in range(int(num1 * num2)):
                    game_code += 'answer' + str(i+1) + '===' + str(request.form["answer"+str(i+1)]) + ';;; '

            if game == "memory":
                for i in range(int(num1 * num2)):
                    game_code += 'question' + str(i+1) + '===' + str(request.form["question"+str(i+1)]) + ';;; '

                for i in range(int(num1 * num2)):
                    game_code += 'answer' + str(i+1) + '===' + str(request.form["answer" + str(i+1)]) + ';;; '
        except KeyError:
            return render_template("error.html", title="Bad Input",
                                   errormsg="Looks like something went wrong. Check your inputs."), 404

        game_code = game_code[:-4]
        return render_template("create.html",
                               game=game,
                               title=("Create a " + game),
                               create_challenges=True,
                               json=game_code)

    else:
        if game == "memory":
            p1 = "Horizontal"
            p2 = "Vertical"
        elif game == "quiz":
            p1 = "categories"
            p2 = "levels"
        else:
            return render_template("error.html",
                                   title="404 Error",
                                   errormsg="404 Not Found: The requested URL was not found on the server. "
                                            "If you entered the URL manually please check your spelling and try again."), 404

        return render_template("create.html",
                               game=game,
                               title=("Create a " + game),
                               create_challenges=False,
                               placeholder1=p1,
                               placeholder2=p2)


@app.route("/play")
def play():
    return render_template("play.html", title="Play")


@app.route("/documentation")
def documentation():
    return render_template("documentation.html", title="Documentation")


@app.route("/games")
def games():
    return render_template("games.html", title="Games")


@app.route("/readme")
def readme():
    return render_template("readme.html", title="Readme")


@app.route("/search")
def search():
    return render_template("search.html", title="Find a Game")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html",
                           title="404 Error",
                           errormsg=e), 404


@app.errorhandler(403)
def permission_denied(e):
    return render_template("error.html",
                           title="403 Error",
                           errormsg=e), 403


if __name__ == "__main__":
    app.run(port=3000, debug=True, threaded=True)
    # ssl_context=context
