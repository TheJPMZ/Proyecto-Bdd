from neo4j import GraphDatabase
import datetime

# Create a driver instance
driver = GraphDatabase.driver("neo4j+s://15cbcf73.databases.neo4j.io", auth=("neo4j", "PflAMMLvQkfX9Ilac14Avqks4w70r379ClnorOANdhs"))
current = datetime.datetime.now()


# Open a session
with driver.session() as session:
    # Use the session to execute queries
    # Movies
    result = session.run("MATCH (n:Movie) RETURN n")
    movies = []
    for record in result:
        movies.append(record)
        
    peliculas = []
    for x in movies:
        node = x["n"]
        
        peliculas.append({
            'titulo': node["Name"],
            'genero': node["Genre"],
            'duracion': f'{node["Duration"]} minutos',
            'calificacion': node["AvgVote"],
            'año': node["ReleaseYear"]
        })
        
    # Series
    result = session.run("MATCH (n:Series) RETURN n")
    series = []
    for record in result:
        series.append(record)
        
    lista_series = []
    for x in series:
        node = x["n"]
        
        lista_series.append({
            'titulo': node["Name"],
            'genero': node["Genre"],
            'duracion': f'{node["Duration"]} minutos',
            'calificacion': node["AvgVote"],
            'año': node["ReleaseYear"]
        })
    
    # Cortos
    result = session.run("MATCH (n:ShortFilm) RETURN n")
    cortos = []
    for record in result:
        cortos.append(record)
        
    lista_cortos = []
    for x in cortos:
        node = x["n"]
        
        lista_cortos.append({
            'titulo': node["Name"],
            'genero': node["Genre"],
            'duracion': f'{node["Duration"]} minutos',
            'calificacion': node["AvgVote"],
            'año': node["ReleaseYear"]
        })
                
    # Actors
    result = session.run("MATCH (n:Actor) RETURN n")
    actors = []
    for record in result:
        actors.append(record)
    
    actores = []
    for x in actors:
        node = x["n"]
        birth = node["BirthDate"]
        actores.append({
            'nombre': node["Name"],
            'nacionalidad': node["Nationality"],
            'edad': current.year - node["BirthDate"].year,
            'genero': 'Masculino',
            'nacimiento': "{2}/{1}/{0}".format(*birth.year_month_day)
        })
    
    
def get_login_user(email):
    with driver.session() as session:
        result = session.run("MATCH (n:User {Email: $email}) RETURN n", email=email)
        
        record = result.single()
        if record:
            return record["n"]
        else:
            return None
    

def like(user, film, rating = 5):
    with driver.session() as session:
        
        session.run("MATCH (u:User {Email: $user_node})-[r:Disliked]->(f:Film {Name: $film_name}) DELETE r",
                    user_node=user, film_name=film)
        
        session.run("MATCH (u:User {Email: $user_node}), (f:Film {Name: $film_name}) "
                    "CREATE (u)-[:Liked {rating: $rating, RateDates: $date}]->(f)",
                    user_node=user, film_name=film, rating=rating, date=current)
        print("Like registrado con éxito!")


def create_film(name, release_year, genre, film_type):
    print(name, release_year, genre, film_type)
    with driver.session() as session:
        if film_type == "Movie":
            session.run("CREATE (f:Film:Movie {Name: $name, ReleaseYear: $release_year, Genre: $genre})",
                        name=name, release_year=release_year, genre=genre)
        elif film_type == "Series":
            session.run("CREATE (f:Film:Series {Name: $name, ReleaseYear: $release_year, Genre: $genre})",
                        name=name, release_year=release_year, genre=genre)
        elif film_type == "ShortFilm":
            session.run("CREATE (f:Film:ShortFilm {Name: $name, ReleaseYear: $release_year, Genre: $genre})",
                        name=name, release_year=release_year, genre=genre)

def edit_film(name, seasons, episodes, avgvotes):
    with driver.session() as session:
        session.run("MATCH (s:Series {Name: $name}) SET s.Seasons = $seasons, s.Episodes = $episodes, s.AvgVote = $avgvotes",
                    name=name, seasons=int(seasons), episodes=int(episodes), avgvotes=int(avgvotes))

def delete_movie(name):
    with driver.session() as session:
        session.run("MATCH (f:Movie {Name: $name}) DETACH DELETE f", name=name)

def delete_property(name, property):
    print(property)
    with driver.session() as session:
        if property == "Episodes":
            session.run("MATCH (f:Film {Name: $name}) REMOVE f.Episodes", name=name)
        elif property == "Seasons":
            session.run("MATCH (f:Film {Name: $name}) REMOVE f.Seasons", name=name)
        elif property == "Genre":
            session.run("MATCH (f:Film {Name: $name}) REMOVE f.Genre", name=name)
        elif property == "Type":
            session.run("MATCH (f:Film {Name: $name}) REMOVE f.Type", name=name)
        elif property == "ID":
            session.run("MATCH (f:Film {Name: $name}) REMOVE f.ID", name=name)
            
def unrate(name, film):
    with driver.session() as session:
        session.run("MATCH (u:User {Email: $user_node})-[r:Liked]->(f:Film {Name: $film_name}) SET r.rating = NULL",
                    user_node=name, film_name=film)
        session.run("MATCH (u:User {Email: $user_node})-[r:Disliked]->(f:Film {Name: $film_name}) SET r.rating = NULL",
                    user_node=name, film_name=film)
        
        print("Deleted the property successfully!")
        
def rate(name, film, rating):
    with driver.session() as session:
        session.run("MATCH (u:User {Email: $user_node})-[r:Liked]->(f:Film {Name: $film_name}) SET r.rating = $rating",
                    user_node=name, film_name=film, rating=rating)
        session.run("MATCH (u:User {Email: $user_node})-[r:Disliked]->(f:Film {Name: $film_name}) SET r.rating = $rating",
                    user_node=name, film_name=film, rating=rating)
        
        print("Deleted the property successfully!")
       
      



      
def get_actores():
    return actores

def get_peliculas():
    return peliculas

def get_series():
    return lista_series

def get_cortos():
    return lista_cortos