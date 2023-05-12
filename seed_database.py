"""Seed database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as file:
    movie_data = json.loads(file.read())

movies_in_db = []
for movie in movie_data:
    overview, poster_path, title = (movie["overview"], movie["poster_path"], movie["title"])
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    current_movie = crud.create_movie(overview=overview,poster_path=poster_path,release_date=release_date,title=title)
    movies_in_db.append(current_movie)


model.db.session.add_all(movies_in_db)
model.db.session.commit()

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email=email, password=password)

    model.db.session.add(user)
    model.db.session.commit()

    for n in range(10):
        rand_movie = choice(movies_in_db)
        score = randint(1,5)
        rating = crud.create_rating(user=user, movie=rand_movie, score=score)
        model.db.session.add(rating)
        model.db.session.commit()
