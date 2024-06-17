from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import random

app = Flask(__name__)
CORS(app)

def getMovieList():
  movies = []

  with open('imdbtop1000.csv', 'r') as movieListFile:
    reader = csv.DictReader(movieListFile, delimiter=';')
    for row in reader:
      movies.append(row)

  return movies

@app.route('/get_random_movie', methods=['GET'])
def pickMovie():
  movies = getMovieList()
  chosenMovie = random.choice(movies)
  return jsonify(chosenMovie)

# Example URL:
# http://192.168.254.40:4908/get_user_movie?userMovie=The%20Godfather
# spaces are replaced by "%20"
@app.route('/get_user_movie', methods=['GET'])
def getUserMovie():
  userMovie = request.args.get('userMovie').lower()
  
  movies = getMovieList()
  for movie in movies:
    if movie['Series_Title'].lower() == userMovie:
      return movie

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4908, debug=True)