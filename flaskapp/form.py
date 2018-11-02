from wtforms import Form
from wtforms import TextAreaField, RadioField,TextField,FloatField,SelectField,BooleanField,IntegerField
from wtforms import validators


class CommentForm(Form):
    name=TextField("Hi! I'm Reves. What's your movie's name?",
                   [validators.length(min=1,max=200, message="Type something!")])
    directors=TextField("Type directors' names separated by commas")
    screenplayers=TextField("Type screeenplayers' names separated by commas")
    cast1name=TextField("1st Actor/Actress' Name")
    cast1gender=SelectField("Gender",
                            choices=[(0,"Select"),
                                     (1,"male"),
                                     (2,"female")],
                            coerce=int)
    cast2name=TextField("2nd  Actor/Actress' Name")
    cast2gender=SelectField("Gender",
                            choices=[(0,"Select"),
                                     (1,"male"),
                                     (2,"female")],
                            coerce=int)
    cast3name=TextField("3rd Actor/Actress' Name")
    cast3gender=SelectField("Gender",
                            choices=[(0,"Select"),
                                     (1,"male"),
                                     (2,"female")],
                            coerce=int)
    cast4name=TextField("4th Actor/Actress' Name")
    cast4gender=SelectField("Gender",
                            choices=[(0,"Select"),
                                     (1,"male"),
                                     (2,"female")],
                            coerce=int)
    productionCompanies=TextField("Type Production Companies' names separated by commas")
    originalLanguage=SelectField("What is the movie's original language?",
                                 choices=[(0,"Select"),
                                          (1,"English"),
                                          (2,"Not English")],
                                 coerce=int)
    runtime=IntegerField("How much do you expect your movie to last? (minutes)")
    imax=SelectField("Are you launching an IMAX movie?",
                     choices=[(0,"Select"),
                              (1,"No"),
                              (2,"Yes")],
                     coerce=int)
    d3=SelectField("Are you launching an 3D movie?",
                   choices=[(0,"Select"),
                            (1,"No"),
                            (2,"Yes")],
                   coerce=int)
    month=SelectField("When are you planning on releasing the movie? (month)",
                    choices=[(0,"Select"),
                             (1,"January"),
                             (2,"February"),
                             (3,"March"),
                             (4,"April"),
                             (5,"May"),
                             (6,"June"),
                             (7,"July"),
                             (8,"August"),
                             (9,"September"),
                             (10,"October"),
                             (11,"November"),
                             (12,"December")],
                             coerce=int)

    weekday=SelectField("When are you planning on releasing the movie? (weekday)",
                      choices=[(0,"Select"),
                               (1,"Monday"),
                               (2,"Tuesday"),
                               (3,"Wednesday"),
                               (4,"Thursday"),
                               (5,"Friday"),
                               (6,"Saturdat"),
                               (7,"Sunday")],
                      coerce=int)
    keywords=TextAreaField("Type keywords separated by commas")
    collectionName=TextField("Type the collection's name")
    bellongsToCollection = SelectField("Does the movie belong to a collection?",
                     choices=[(0, "Select"),
                              (1, "No"),
                              (2, "Yes")],
                     coerce=int)