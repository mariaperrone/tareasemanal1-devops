from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

@app.route("/pokemons", methods=["GET"])
def getPokemons():
    with open("./api.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/pokemons", methods=["POST"])
def createPokemons():
    with open("./api.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    new_pokemon = request.get_json()
    data.append(new_pokemon)

    with open("./api.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return jsonify(new_pokemon)

@app.route("/pokemons/<int:id>", methods=["GET"])
def getPokemon(id):
    with open("./api.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    pokemon = next((item for item in data if item['id'] == id), None)
    
    if pokemon is None:
        return jsonify({"error": "no se encontró el pokemón"}), 404
    
    return jsonify(pokemon)

@app.route("/pokemons/<int:id>", methods=["PUT"])
def updatePokemon(id):
    with open("./api.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    pokemon = next((item for item in data if item['id'] == id), None)
    
    if pokemon is None:
        return jsonify({"error": "no se encontró el pokemón"}), 404

    new_pokemon = request.get_json()
    if new_pokemon.get('id') != id:
        return jsonify({"error": "el ID dado no corresponde con el id de la solicitud"}), 400

    for index, item in enumerate(data):
        if item['id'] == id:
            data[index] = new_pokemon
            break
        
    with open("./api.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return jsonify(new_pokemon)

@app.route("/pokemons/<int:id>", methods=["DELETE"])
def deletePokemon(id):
    with open("./api.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    pokemon = next((item for item in data if item['id'] == id), None)
    
    if pokemon is None:
        return jsonify({"error": "no se encontró el pokemón"}), 404

    data.remove(pokemon)
        
    with open("./api.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return jsonify({ "resultado": "el pokemón " + str(id) + " ha sido eliminado"})

if __name__ == '__main__':
    app.run(debug=True)