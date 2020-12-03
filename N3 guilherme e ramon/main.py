from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request, Flask, render_template
from app import app
from app import mongo
from classe_filmera import Filme

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/add', methods=['POST'])
def add_filme():

    _json = request.json
    filme = Filme(_json["filme"], _json["diretor"], _json["genero"])

    if filme.filme and filme.diretor and filme.genero and request.method == 'POST':

        id = mongo.db.filmeras.insert(
            {'filme': filme.filme, 'diretor': filme.diretor, 'genero': filme.genero})

        resp = jsonify("filme adicionado com sucesso")

        resp.status_code = 200

        return resp


@app.route('/view')
def listar_filmes():
    filmes = mongo.db.filmeras.find()
    resp = dumps(filmes)
    return resp


@app.route('/filmeras/<id>')
def pesquisar_filmeras(id):
    musica = mongo.db.filmeras.find_one({'_id': ObjectId(id)})
    resp = dumps(musica)
    return resp


@app.route('/delete/<id>', methods=['DELETE'])
def delete_filme(id):
    mongo.db.filmeras.delete_one({'_id': ObjectId(id)})
    resp = jsonify("filme deletado")

    resp.status_code = 200

    return resp


@app.route('/update/<id>', methods=['PUT'])
def update_filme(id):
    _id = id
    _json = request.json
    filme = Filme(_json["filme"], _json["diretor"], _json["genero"])


    if filme.filme and filme.diretor and filme.genero and _id and request.method == 'PUT':

        mongo.db.filmeras.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(
            _id)}, {'$set': {'filme': filme.filme, 'diretor': filme.diretor, 'genero': filme.genero}})

        resp = jsonify("filme atualizado")

        resp.status_code = 200

        return resp


if __name__ == "__main__":
    app.run(debug=True)
