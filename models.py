from flask_sqlalchemy  import SQLAlchemy
import datetime

db=SQLAlchemy()

#cada atributo de class será una columna en la base de datos
class movies(db.Model):
    __tablename__="movies_database"
    id=db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    title=db.Column(db.String(80))
    directors=db.Column(db.String)
    scriptwriters=db.Column(db.String)
    collection_name=db.Column(db.String)
    genres=db.Column(db.String)
    language=db.Column(db.String(10))
    production_companies=db.Column(db.String)
    runtime=db.Column(db.Integer)
    keywords=db.Column(db.String)
    month=db.Column(db.String(20))
    weekday=db.Column(db.String(20))
    cast_names=db.Column(db.String)
    companies_count=db.Column(db.Integer)
    genres_count=db.Column(db.Integer)
    main_actor_genre=db.Column(db.String(10))
    revenue=db.Columns(db.Float)

