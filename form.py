from wtforms import Form
from wtforms import TextAreaField, RadioField,TextField,FloatField,SelectField,BooleanField,IntegerField,SelectMultipleField
from wtforms import validators
import unicodedata



class CommentForm(Form):
    name=TextField("Hi! I'm Reves. What's your movie's name?*",
                   #[validators.length(min=1,max=200, message="Relax, I won't tell anyone. Type something.")]
                   )
    directors=TextField("Type directors' names separated by commas")
    scriptwriters=TextField("Type scriptwriters' names separated by commas")
    genres=SelectMultipleField("Select you movie's genres (Multiple Choice)",
                               choices=[("Drama","Drama"),
                                        ("Comedy","Comedy"),
                                        ("Thriller","Thriller"),
                                        ("Action","Action"),
                                        ("Romance","Romance"),
                                        ("Adventure","Adventure"),
                                        ("Crime","Crime"),
                                        ("Science Fiction","Science Fiction"),
                                        ("Horror","Horror"),
                                        ("Family","Family"),
                                        ("Fantasy","Fantasy"),
                                        ("Mystery","Mystery"),
                                        ("Animation","Animation"),
                                        ("History","History"),
                                        ("Music","Music"),
                                        ("War","War"),
                                        ("Documentary","Documentary"),
                                        ("Western","Western"),
                                        ("Foreign","Foreign"),
                                        ("TV Movie","TV Movie")])
    castnames=TextField("Type actors'/actresses' names separated by commas*")
    cast1gender=SelectField("Main character's gender",
                            choices=[(0,"Select"),
                                     (1,"male"),
                                     (2,"female")],
                            coerce=int)
    productionCompanies=TextField("Type Production Companies' names separated by commas",
                   #[validators.length(min=1,max=200, message="At least one company, please.")]
                                  )
    originalLanguage=SelectField("What is the movie's original language?",
                                 choices=[(0,"Select"),
                                          (1,"English"),
                                          (2,"Not English")],
                                 coerce=int)
    runtime=IntegerField("How much do you expect your movie to last? (minutes)")
    imax=SelectField("Are you launching an IMAX movie?",
                        #[validators.DataRequired(message="Please, select an option")],
                     choices=[(0,"Select"),
                              (1,"No"),
                              (2,"Yes")],
                     coerce=int)
    d3=SelectField("Are you launching a 3D movie?",
                   #[validators.DataRequired(message="Please, select an option")],
                   choices=[(0,"Select"),
                            (1,"No"),
                            (2,"Yes")],
                   coerce=int)
    month=SelectField("When are you planning on releasing the movie? (month)",
                        #[validators.DataRequired(message="Please, select a month")],
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
                        #[validators.DataRequired(message="Please, select a weekday")],
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
                                       #[validators.DataRequired(message="Please, select an option")],
                     choices=[(0, "Select"),
                              (1, "No"),
                              (2, "Yes")],
                     coerce=int)