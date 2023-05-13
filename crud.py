"""CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_all_users():
    """Returns a list of all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Returns 1 user profile"""

    return User.query.get(user_id)

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie

def get_all_movies():
    """Returns a list of all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Returns 1 movie"""

    # return Movie.query.filter(Movie.movie_id==movie_id).first()

    return Movie.query.get(movie_id)
    
def create_rating(user, movie, score):
    """Create a new rating, given a User instance and a Movie instance."""

    rating = Rating(user=user, movie=movie, score=score)


    return rating

def add_to_database(new_entry):
    """Add new stuff to db"""

    db.session.add(new_entry)
    db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)