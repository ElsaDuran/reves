from flask import Flask
from flask import render_template
from flask import request
import form


app=Flask(__name__,template_folder="docs",static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/elements.html")
def elements():
    return render_template("elements.html")

@app.route("/index.html")
def index2():
    return render_template("index.html")

@app.route("/get-the-number.html",methods=["POST","GET"])
def get_the_number():
    comment_form=form.CommentForm(request.form)
    moviename="Your movie's"
    directors=[]
    scriptwriters=[]
    genres=[]
    cast_names=[]
    cast_genders =[]
    collection=0
    collection_name=""
    language=0
    production_companies=[]
    runtime=0
    imax=0
    d3=0
    month=0
    weekday=0
    keywords=[]
    revenue=0

    import numpy as np
    import pandas as pd
    import pickle
    import revesFunctions as rf

    with open("transformation/collection_dict.pickle", "rb") as handle:
        collection_dict = pickle.load(handle)
    with open("transformation/genres_dict.pickle", "rb") as handle:
        genres_dict = pickle.load(handle)
    with open("transformation/language_dict.pickle", "rb") as handle:
        language_dict = pickle.load(handle)
    with open("transformation/production_company_dict.pickle", "rb") as handle:
        production_company_dict = pickle.load(handle)
    with open("transformation/cast_dict.pickle", "rb") as handle:
        cast_dict = pickle.load(handle)
    with open("transformation/cast_gender_dict.pickle", "rb") as handle:
        cast_gender_dict = pickle.load(handle)
    with open("transformation/directors_dict.pickle", "rb") as handle:
        directors_dict = pickle.load(handle)
    with open("transformation/writers_dict.pickle", "rb") as handle:
        writers_dict = pickle.load(handle)
    with open("transformation/keywords_dict.pickle", "rb") as handle:
        keywords_dict = pickle.load(handle)
    with open("transformation/month_dict.pickle", "rb") as handle:
        month_dict = pickle.load(handle)
    with open("transformation/weekday_dict.pickle", "rb") as handle:
        weekday_dict = pickle.load(handle)

    if request.method=="POST" and comment_form.validate():

       #loading data from comment form

        moviename=(comment_form.name.data)+"'s"
        directors=str.split(comment_form.directors.data,",")
        scriptwriters=str.split(comment_form.scriptwriters.data,",")
        genres=comment_form.genres.data
        cast_names=str.split(comment_form.castnames.data,",")
        cast_genders=comment_form.cast1gender.data
        collection=comment_form.bellongsToCollection.data
        collection_name=comment_form.collectionName.data
        language=comment_form.originalLanguage.data
        production_companies=str.split(comment_form.productionCompanies.data,",")
        runtime = (comment_form.runtime.data)
        month=comment_form.month.data
        weekday=comment_form.weekday.data
        imax=comment_form.imax.data
        d3=comment_form.d3.data
        keywords=str.split(comment_form.keywords.data,",")

       #data transformation

       #applying Reves model

    revenue = revenue + runtime*2




    return render_template("get-the-number.html",
                           form=comment_form,
                           moviename=moviename,
                           directors=directors,
                           genres=genres,
                           scriptwriters=scriptwriters,
                           cast_names=cast_names,
                           cast_genders=cast_genders,
                           collection=collection,
                           collection_name=collection_name,
                           language=language,
                           production_companies=production_companies,
                           runtime=runtime,
                           month=month,
                           weekday=weekday,
                           imax=imax,
                           d3=d3,
                           keywords=keywords,
                           revenue=revenue)

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
    import pandas as pd
    directors=pd.read_pickle("./docs/dicts/directors_dict.pickle")
    b=sorted(list(directors.keys()))
    c=len(b)
    return render_template("directors-index.html",directors=directors,b=b,c=c)

@app.route("/scriptwriters-index.html")
def scriptwritersindex():
    import pandas as pd
    scriptwriters=pd.read_pickle("./docs/dicts/writers_dict.pickle")
    b=sorted(list(scriptwriters.keys()))
    c=len(b)
    return render_template("scriptwriters-index.html",scriptwriters=scriptwriters,b=b,c=c)

@app.route("/teacher-view.html")
def teacher():
    return render_template("teacher-view.html")

@app.route("/collections-index.html")
def collectionsindex():
    import pandas as pd
    collections =pd.read_pickle("./docs/dicts/collection.pickle")
    b=sorted(list(collections.keys()))
    c=len(b)
    return render_template("collections-index.html",collections=collections,b=b,c=c)

@app.route("/cast-index.html")
def castindex():
    import pandas as pd
    cast=pd.read_pickle("./docs/dicts/cast_dict.pickle")
    b=sorted(list(cast.keys()))
    c=len(b)
    return render_template("cast-index.html",cast=cast,b=b,c=c)

@app.route("/keywords-index.html")
def keywordsindex():
    import pandas as pd
    keywords=pd.read_pickle("./docs/dicts/keywords_dict.pickle")
    b=sorted(list(keywords.keys()))
    c = len(b)
    return render_template("keywords-index.html",keywords=keywords,b=b,c=c)

@app.route("/companies-index.html")
def companiesindex():
    import pandas as pd
    companies=pd.read_pickle("./docs/dicts/production_company_dict.pickle")
    b=sorted(list(companies.keys()))
    c=len(b)
    return render_template("companies-index.html",companies=companies,b=b,c=c)

if __name__ == '__main__':
    app.run(debug=True)