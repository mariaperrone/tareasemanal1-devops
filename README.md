# Crear ambiente
python -m venv .venv

# Activar ambiente
.venv\Scripts\activate

# Instalar Flask
pip install flask

# Cómo correr la API:
python app.py

# Cómo usar las rutas - Buscar todos
En tu terminal, corre el siguiente comando:
curl -X GET http://127.0.0.1:5000/pokemons

# Cómo usar las rutas - Buscar por id
En tu terminal, corre el siguiente comando:
curl -X GET http://127.0.0.1:5000/pokemons/1

# Cómo usar las rutas - Crear
En tu terminal, corre el siguiente comando:
curl -X POST http://127.0.0.1:5000/pokemons -H "Content-Type: application/json" -d '{"id": 11, "nombre": "test pokemon"}'

# Cómo usar las rutas - Actualizar
En tu terminal, corre el siguiente comando:
curl -X PUT http://127.0.0.1:5000/pokemons/11 -H "Content-Type: application/json" -d '{"id": 11, "nombre": "updated pokemon"}'

# Cómo usar las rutas - Eliminar
En tu terminal, corre el siguiente comando:
curl -X DELETE http://127.0.0.1:5000/pokemons/11