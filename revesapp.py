from flask import Flask
from flask import render_template
from flask import request
import form


app=Flask(__name__,template_folder="docs",static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def index2():
    return render_template("index.html")

@app.route("/get-the-number.html",methods=["POST","GET"])
def get_the_number():
    comment_form=form.CommentForm(request.form)
    moviename="Your movie's"
    directors=[]
    screenplayers=[]
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

    if request.method=="POST" and comment_form.validate():

       #importing data and libraries

       #loading data from comment form

        moviename=(comment_form.name.data)+"'s"
        directors=comment_form.screenplayers.data
        screenplayers=comment_form.screenplayers.data
        name1=comment_form.cast1name.data
        name2=comment_form.cast2name.data
        name3=comment_form.cast3name.data
        name4=comment_form.cast4name.data
        gender1=comment_form.cast1gender.data
        gender2=comment_form.cast2gender.data
        gender3=comment_form.cast3gender.data
        gender4=comment_form.cast4gender.data
        cast_names.append([name1,name2,name3,name4])
        cast_genders.append([gender1,gender2,gender3,gender4])
        collection=comment_form.bellongsToCollection.data
        collection_name=comment_form.collectionName.data
        language=comment_form.originalLanguage.data
        production_companies=comment_form.productionCompanies.data
        runtime = comment_form.runtime.data
        month=comment_form.month.data
        weekday=comment_form.weekday.data
        imax=comment_form.imax.data
        d3=comment_form.d3.data
        keywords=comment_form.keywords.data

       #data transformation

       #applying Reves model

    revenue = revenue + runtime*2




    return render_template("get-the-number.html",
                           form=comment_form,
                           moviename=moviename,
                           directors=directors,
                           screenplayers=screenplayers,
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

@app.route("/screenplayers-index.html")
def screenplayersindex():
    import pandas as pd
    screenplayers=pd.read_pickle("./docs/dicts/screenplayers_dict.pickle")
    b=sorted(list(screenplayers.keys()))
    c=len(b)
    return render_template("screenplayers-index.html",screenplayers=screenplayers,b=b,c=c)

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