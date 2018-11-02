from flask import Flask
from flask import render_template
from flask import request
import form


app=Flask(__name__,template_folder="docs2",static_folder="static")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/get-the-number.html",methods=["POST","GET"])
def get_the_number():
    comment_form=form.CommentForm(request.form)
    moviename = "Your movie's"
    revenue=0
    if request.method=="POST" and comment_form.validate():
        moviename=(comment_form.name.data)+"'s"
        revenue = comment_form.runtime.data

    return render_template("get-the-number.html",form=comment_form,moviename=moviename,revenue=revenue)

@app.route("/reason-why.html")
def reason_why():
    return render_template("reason-why.html")

@app.route("/screenplayers.html")
def screenplayers():
    return render_template("screenplayers.html")

@app.route("/show-me-the-money.html")
def show_me_the_money():
    return render_template("show-me-the-money.html")

@app.route("/specifications.html")
def specifications():
    return render_template("specifications.html")

@app.route("/directors-index.html")
def directors():
    directors={'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    b=list(directors.keys())
    return render_template("directors-index.html",directors=directors,b=b)

@app.route("/screenplayers-index.html")
def screenplayersindex():
    screenplayers={'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    b=list(screenplayers.keys())
    return render_template("screenplayers-index.html",screenplayers=screenplayers,b=b)

@app.route("/teacher-view.html")
def teacher():
    return render_template("teacher-view.html")

@app.route("/collections-index.html")
def collectionsindex():
    collections={'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    b=list(collections.keys())
    return render_template("collections-index.html",collections=collections,b=b)

@app.route("/cast-index.html")
def castindex():
    cast={'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    b=list(cast.keys())
    return render_template("cast-index.html",cast=cast,b=b)

@app.route("/keywords-index.html")
def keywordsindex():
    keywords={'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    b=list(keywords.keys())
    return render_template("keywords-index.html",keywords=keywords,b=b)

@app.route("/companies-index.html")
def companiesindex():
    companies={'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    b=list(companies.keys())
    return render_template("companies-index.html",companies=companies,b=b)

if __name__ == '__main__':
    app.run(debug=True)