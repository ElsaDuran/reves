from wtforms import Form
from wtforms import TextAreaField, RadioField,TextField,FloatField,SelectField,BooleanField,IntegerField
from wtforms import validators
import unicodedata



class CommentForm(Form):
    title=TextField("Hi! I'm Reves. What's your movie's name?*",
                   #[validators.length(min=1, message="Relax, I won't tell anyone. Type something.")]
                   )
    directors=TextField("Type directors' names separated by commas")
    scriptwriters=TextField("Type scriptwriters' names separated by commas")
    cast_names=TextField("Type actors'/actresses' names separated by commas")
    main_actor_genre=SelectField("Main character's gender",
                            #[validators.DataRequired(message="Please, select an option")],
                            choices=[(0,"Select"),
                                     (1,"female"),
                                     (2,"male")],
                            coerce=int)
    productionCompanies=TextField("Type Production Companies' names separated by commas",
                   #[validators.length(min=1, message="At least one company, please.")]
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
    drama=RadioField("Drama",choices=[("Drama","Drama")])
    comedy=RadioField("Comedy",choices=[("Comedy","Comedy")])
    thriller=RadioField("Thriller",choices=[("Thriller","Thriller")])
    action=RadioField("Action",choices=[("Action","Action")])
    romance=RadioField("Romance",choices=[("Romance","Romance")])
    adventure=RadioField("adventure",choices=[("Adventure","Adventure")])
    crime=RadioField("Crime",choices=[("Crime","Crime")])
    science_fiction=RadioField("Science Fiction",choices=[("Science Fiction","Science Fiction")])
    horror=RadioField("Horror",choices=[("Horror","Horror")])
    family=RadioField("Family",choices=[("Family","Family")])
    fantasy=RadioField("Fantasy",choices=[("Fantasy","Fantasy")])
    mystery=RadioField("Mystery",choices=[("Mystery","Mystery")])
    animation=RadioField("Animation",choices=[("Animation","Animation")])
    history=RadioField("History",choices=[("History","History")])
    music=RadioField("Music",choices=[("Music","Music")])
    war = RadioField("War", choices=[("War", "War")])
    documentary=RadioField("Documentary",choices=[("Documentary","Documentary")])
    western=RadioField("Western",choices=[("Western","Western")])
    foreign=RadioField("Foreign",choices=[("Foreign","Foreign")])
    tv=RadioField("TV Movie",choices=[("TV Movie","TV Movie")])


