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

@app.route("/get-the-number-result.html", methods=["POST","GET"])
def result():
    comment_form = form.CommentForm(request.form)
    title = ""
    directors = []
    scriptwriters = []
    cast_names = []
    main_actor_genre = []
    collection = 0
    collection_name = ""
    genres = []
    genres_count = 2
    language = ""
    planguage = []
    production_companies = []
    companies_count = 2
    runtime = 0
    imax = 0
    d3 = 0
    month = ""
    weekday = ""
    keywords = []
    revenue = 0
    drama = "a"
    comedy = "a"
    thriller = "a"
    action = "a"
    romance = "a"
    adventure = "a"
    crime = "a"
    science_fiction = "a"
    horror = "a"
    family = "a"
    fantasy = "a"
    mystery = "a"
    animation = "a"
    history = "a"
    music = "a"
    war = "a"
    documentary = "a"
    western = "a"
    foreign = "a"
    tv = "a"

    import numpy as np
    import pandas as pd
    import pickle
    import revesFunctions as rf
    from xgboost import XGBRegressor

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
    #with open("transformation/writers_dict.pickle", "rb") as handle:
        writers_dict=pickle.load(open("./transformation/writers_dict.pickle", "rb"))
    with open("transformation/keywords_dict.pickle", "rb") as handle:
        keywords_dict = pickle.load(handle)
    with open("transformation/month_dict.pickle", "rb") as handle:
        month_dict = pickle.load(handle)
    with open("transformation/weekday_dict.pickle", "rb") as handle:
        weekday_dict = pickle.load(handle)

    xgbo = pickle.load(open("xgbo_model.pkl", "rb"))

    if request.method == "POST":

        # loading data from comment form

        if len(title)==0:
            title="Your movie"
        else:
            title = (comment_form.title.data)

        directors = str.split(comment_form.directors.data, ",")
        scriptwriters = str.split(comment_form.scriptwriters.data, ",")
        cast_names = str.split(comment_form.cast_names.data, ",")
        main_actor_genre = c = str(comment_form.main_actor_genre.data).split(" ")
        collection = comment_form.bellongsToCollection.data
        collection_name = str.split(comment_form.collectionName.data, "...")
        drama = comment_form.drama.data
        comedy = comment_form.comedy.data
        thriller = comment_form.thriller.data
        action = comment_form.action.data
        romance = comment_form.romance.data
        adventure = comment_form.adventure.data
        crime = comment_form.crime.data
        science_fiction = comment_form.science_fiction.data
        horror = comment_form.horror.data
        family = comment_form.family.data
        fantasy = comment_form.fantasy.data
        mystery = comment_form.mystery.data
        animation = comment_form.animation.data
        history = comment_form.history.data
        music = comment_form.music.data
        war = comment_form.war.data
        documentary = comment_form.documentary.data
        western = comment_form.western.data
        foreign = comment_form.foreign.data
        tv = comment_form.tv.data
        planguage = comment_form.originalLanguage.data
        production_companies = str.split(comment_form.productionCompanies.data, ",")
        runtime = (comment_form.runtime.data)
        imax = comment_form.imax.data
        d3 = comment_form.d3.data
        month = str(comment_form.month.data).split(" ")
        weekday = str(comment_form.weekday.data).split(" ")
        keywords = str.split(comment_form.keywords.data, ",")

        if cast_names[0] == "" and directors[0] == "" and scriptwriters[0]=="" and production_companies[0]=="":
            revenue = 0
        else:

            # data transformation

            companies_count = len(production_companies)

            genres = [drama, comedy, thriller, action, romance, adventure, crime, science_fiction, horror, family, fantasy,
                      mystery, animation, history, music, war, documentary, western, foreign, tv]
            genres = [x for x in genres if x != "None"]
            genres_count = len(genres)

            if imax == 2:
                if "imax" not in keywords:
                    keywords.append("imax")

            if d3 == 2:
                if "3d" not in keywords:
                    keywords.append("3d")

            if planguage == 1:
                language = "en"
            elif planguage == 2:
                language = "no"

            data = [directors,
                    scriptwriters,
                    collection_name,
                    genres,
                    language,
                    production_companies,
                    runtime,
                    keywords,
                    month,
                    weekday,
                    cast_names,
                    companies_count,
                    title,
                    genres_count,
                    main_actor_genre]

            x = pd.DataFrame([data], columns=['directors', 'writers', 'belongs_to_collection', 'genres',
                                              'original_language', 'production_companies', 'runtime', 'keywords',
                                              'release_month', 'release_weekday', 'cast_names',
                                              'production_companies_counter', 'title', 'genres_counter',
                                              'main_actor_genre'])

            x["directors"] = x["directors"].apply(lambda x: [rf.clean(name) for name in x])
            x["directors"] = x["directors"].apply(rf.get_mean, variable_mean_dict=directors_dict)

            x["writers"] = x["writers"].apply(lambda x: [rf.clean(name) for name in x])
            x["writers"] = x["writers"].apply(rf.get_mean, variable_mean_dict=writers_dict)

            x["genres"] = x["genres"].apply(lambda x: [rf.clean(name) for name in x])
            x["genres"] = x["genres"].apply(rf.get_mean, variable_mean_dict=genres_dict)

            x["cast_names"] = x["cast_names"].apply(lambda x: [rf.clean(name) for name in x])
            x["cast_names"] = x["cast_names"].apply(rf.get_mean, variable_mean_dict=cast_dict)

            x["belongs_to_collection"] = x["belongs_to_collection"].apply(lambda x: [rf.clean(name) for name in x])
            x["belongs_to_collection"] = x["belongs_to_collection"].apply(rf.get_mean, variable_mean_dict=collection_dict)

            x["original_language"] = x["original_language"].apply(lambda x: [rf.clean(name) for name in [x]])
            x["original_language"] = x["original_language"].apply(rf.get_mean, variable_mean_dict=language_dict)

            x["production_companies"] = x["production_companies"].apply(lambda x: [rf.clean(name) for name in x])
            x["production_companies"] = x["production_companies"].apply(rf.get_mean, variable_mean_dict=production_company_dict)

            x["release_month"] = x["release_month"].apply(rf.get_mean, variable_mean_dict=month_dict)
            x["release_weekday"] = x["release_weekday"].apply(rf.get_mean, variable_mean_dict=weekday_dict)

            x["keywords"] = x["keywords"].apply(lambda x: [rf.clean(name) for name in x])
            x["keywords"] = x["keywords"].apply(rf.get_mean, variable_mean_dict=keywords_dict)

            x["main_actor_genre"] = x["main_actor_genre"].apply(rf.get_mean, variable_mean_dict=cast_gender_dict)

            # applying Reves model

            x = x.drop(["title"], axis=1).values
            revenue = int(xgbo.predict(x)[0])
            if revenue<0:
                revenue=0
            else:
                revenue='{0:,}'.format(revenue)

            directors=(', '.join(directors))
            scriptwriters=(', '.join(scriptwriters))
            cast_names=(', '.join(cast_names))

            if main_actor_genre[0]=="2":
                main_actor_genre="Male"
            elif main_actor_genre[0]=="1":
                main_actor_genre="Female"
            else:
                main_actor_genre="No value"

            collection_name=collection_name[0]
            genres=(', '.join(genres))
            production_companies=(", ".join(production_companies))
            keywords = (", ".join(keywords))

            if language=="en":
                language="English"
            elif language=="no":
                language="Not English"

            if month[0]=="1":
                month="January"
            elif month[0]=="2":
                month="February"
            elif month[0]=="3":
                month="March"
            elif month[0]=="4":
                month="April"
            elif month[0]=="5":
                month="May"
            elif month[0]=="6":
                month="June"
            elif month[0]=="7":
                month="July"
            elif month[0]=="8":
                month="August"
            elif month[0]=="9":
                month="September"
            elif month[0]=="10":
                month="October"
            elif month[0]=="11":
                month="November"
            elif month[0]=="12":
                month="December"

            if weekday[0]=="1":
                weekday="Monday"
            elif weekday[0]=="2":
                weekday="Tuesday"
            elif weekday[0]=="3":
                weekday="Wednesday"
            elif weekday[0]=="4":
                weekday="Thursday"
            elif weekday[0]=="5":
                weekday="Friday"
            elif weekday[0]=="6":
                weekday="Saturday"
            elif weekday[0]=="7":
                weekday="Sunday"



    return render_template("get-the-number-result.html",
                           form=comment_form,
                           title=title,
                           directors=directors,
                           genres=genres,
                           scriptwriters=scriptwriters,
                           cast_names=cast_names,
                           main_actor_genre=main_actor_genre,
                           collection=collection,
                           collection_name=collection_name,
                           language=language,
                           planguage=planguage,
                           production_companies=production_companies,
                           runtime=runtime,
                           month=month,
                           weekday=weekday,
                           imax=imax,
                           d3=d3,
                           keywords=keywords,
                           revenue=revenue,
                           genres_count=genres_count,
                           companies_count=companies_count,
                           drama=drama,
                           comedy=comedy,
                           thriller=thriller,
                           action=action,
                           romance=romance,
                           adventure=adventure,
                           crime=crime,
                           science_fiction=science_fiction,
                           horror=horror,
                           family=family,
                           fantasy=fantasy,
                           mystery=mystery,
                           animation=animation,
                           history=history,
                           music=music,
                           war=war,
                           documentary=documentary,
                           western=western,
                           foreign=foreign,
                           tv=tv)

@app.route("/get-the-number.html",methods=["POST","GET"])

def get_the_number():
    comment_form = form.CommentForm(request.form)

    return render_template("get-the-number.html",form=comment_form)

@app.route("/reason-why.html")
def reason_why():
    return render_template("reason-why.html")

@app.route("/scriptwriters.html")
def scriptwriters():
    return render_template("scriptwriters.html")

@app.route("/how-to-use-reves.html")
def howtousereves():
    return render_template("how-to-use-reves.html")

@app.route("/structure.html")
def structure():
    return render_template("structure.html")

@app.route("/next-steps.html")
def nextsteps():
    return render_template("next-steps.html")

@app.route("/directors-index.html")
def directors():
    import pandas as pd
    directors=pd.read_pickle("./transformation/directors_dict.pickle")
    b=sorted(list(directors.keys()))
    c=len(b)
    return render_template("directors-index.html",directors=directors,b=b,c=c)

@app.route("/scriptwriters-index.html")
def scriptwritersindex():
    import pandas as pd
    scriptwriters=pd.read_pickle("./transformation/writers_dict.pickle")
    b=sorted(list(scriptwriters.keys()))
    c=len(b)
    return render_template("scriptwriters-index.html",scriptwriters=scriptwriters,b=b,c=c)

@app.route("/teacher-view.html")
def teacher():
    return render_template("teacher-view.html")

@app.route("/collections-index.html")
def collectionsindex():
    import pandas as pd
    collections =pd.read_pickle("./transformation/collection_dict.pickle")
    b=sorted(list(collections.keys()))
    c=len(b)
    return render_template("collections-index.html",collections=collections,b=b,c=c)

@app.route("/cast-index.html")
def castindex():
    import pandas as pd
    cast=pd.read_pickle("./transformation/cast_dict.pickle")
    b=sorted(list(cast.keys()))
    c=len(b)
    return render_template("cast-index.html",cast=cast,b=b,c=c)

@app.route("/keywords-index.html")
def keywordsindex():
    import pandas as pd
    keywords=pd.read_pickle("./transformation/keywords_dict.pickle")
    b=sorted(list(keywords.keys()))
    c = len(b)
    return render_template("keywords-index.html",keywords=keywords,b=b,c=c)

@app.route("/companies-index.html")
def companiesindex():
    import pandas as pd
    companies=pd.read_pickle("./transformation/production_company_dict.pickle")
    b=sorted(list(companies.keys()))
    c=len(b)
    return render_template("companies-index.html",companies=companies,b=b,c=c)

if __name__ == '__main__':
    app.run(debug=True)