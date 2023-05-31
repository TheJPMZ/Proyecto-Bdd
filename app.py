from flask import Flask, render_template, request, redirect, url_for

import memes

app = Flask(__name__)

current_user = None


# Página de inicio
@app.route('/')
def home():
    # Obtener datos de las películas desde el backend
    peliculas = obtener_peliculas()
    series = memes.get_series()
    cortos = memes.get_cortos()

    # Obtener datos de las recomendaciones desde el backend
    recomendaciones = [...]  # Lista de recomendaciones obtenidas del backend

    return render_template('index.html', peliculas=peliculas, recomendaciones=recomendaciones, series=series, cortos=cortos)


# Página de preferencias
@app.route('/preferencias', methods=['GET', 'POST'])
def preferencias():
    if request.method == 'POST':
        # Obtener las preferencias enviadas por el formulario
        generos = request.form.getlist('generos')
        actores = request.form.getlist('actores')
        # Procesar las preferencias y guardarlas en la base de datos o en una sesión
        # Aquí puedes agregar la lógica para almacenar las preferencias en el backend
        # redirigir a la página de recomendaciones
        return redirect(url_for('recomendaciones'))
    return render_template('preferencias.html')


# Página de recomendaciones
@app.route('/recomendaciones')
def recomendaciones():
    # Aquí puedes agregar la lógica para obtener las recomendaciones del backend
    # y pasarlas a la plantilla para mostrarlas en la página de recomendaciones
    # Lista de recomendaciones obtenidas del backend
    peliculas_recomendadas = obtener_peliculas_recomendadas()
    return render_template('recomendaciones.html', peliculas=peliculas_recomendadas)

@app.route('/create_film')
def create_film():
    return render_template('createfilm.html', series=memes.get_series(), movies=memes.get_peliculas())


# Ruta y función de vista para la página de actores
@app.route('/actores')
def actores():
    # Lógica para obtener la lista de actores
    actores = obtener_actores()

    # Renderiza el template 'actores.html' y pasa la lista de actores como argumento
    return render_template('actores.html', actores=actores)


# Ejemplo de función para obtener la lista de actores
def obtener_actores():
    # Lógica para obtener la lista de actores desde tu base de datos o cualquier otra fuente de datos
    actores = memes.get_actores()

    return actores


def obtener_peliculas():
    # Lógica para obtener la lista de películas desde tu base de datos o cualquier otra fuente de datos
    peliculas = memes.get_peliculas()
    
    return peliculas


def obtener_peliculas_recomendadas():
    # Lógica para obtener la lista de películas recomendadas desde tu base de datos o cualquier otra fuente de datos
    peliculas_recomendadas = memes.get_peliculas()
    return peliculas_recomendadas






@app.route('/like', methods=['POST'])
def like_movie():
    titulo = request.form.get('titulo')
    
    memes.like(current_user["Email"], titulo, request.form.get('rating'))
    
    print(titulo, "recibió like por", current_user["Name"])
    print("Película que recibió like:", titulo)
    return "¡Like registrado con éxito!"

@app.route('/login', methods=['POST'])
def process_text():
    global current_user
    text = request.form.get('text')
    print("Received text:", text)
    
    mem = memes.get_login_user(text)
    if mem:
        current_user = mem
        return "Logged in! Welcome, " + mem["Name"] + "!"
    else:
        return "User not found! Try Again."
    
@app.route('/film_creation', methods=['POST'])
def film_creation():
    name = request.form.get('name')
    release_year = request.form.get('release_year')
    genre = request.form.get('genre')
    film_type = request.form.get('film_type')
    
    memes.create_film(name, release_year, genre, film_type)
    
    return "Film created! " + name + " " + release_year + " " + genre + " " + film_type


@app.route('/film_edition', methods=['POST'])
def film_edition():
    name = request.form.get('name')
    seasons = request.form.get('seasons')
    episodes = request.form.get('episodes')
    avgvotes = request.form.get('avgvote')
    
    memes.edit_film(name, seasons, episodes, avgvotes)
    
    return "Film edited! " + name + " " + seasons + " " + episodes + " " + avgvotes

@app.route('/film_deletion', methods=['POST'])
def film_deletion():
    name = request.form.get('name')
    
    memes.delete_movie(name)
    
    return "Film deleted! " + name

@app.route('/node_prop_del', methods=['POST'])
def node_prop_del():
    name = request.form.get('name')
    property = request.form.get('prop')
    
    memes.delete_property(name, property)
    
    return "Property deleted! " + name + " " + property


@app.route('/unrate', methods=['POST'])
def unrate():
    global current_user
    titulo = request.form.get('titulo')
    print("Received text:", titulo)
    
    memes.unrate(current_user["Email"], titulo)
    
    return "Deleted the rating for " + titulo + " by " + current_user["Name"] + "!"

@app.route('/rate', methods=['POST'])
def rate():
    global current_user
    titulo = request.form.get('titulo')
    print("Received text:", titulo)
    
    memes.rate(current_user["Email"], titulo, request.form.get('rating'))
    
    return "Rated " + titulo + " by " + current_user["Name"] + "!"


if __name__ == '__main__':
    app.run(debug=True)
