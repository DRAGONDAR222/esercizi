
# Punto di ingresso di Flask
from flask import Flask, request, url_for, jsonify
from classi.dog import Dog
from classi.cat import Cat
from classi.shelter import Shelter

app = Flask(__name__)

# Rifugio globale
rifugio = Shelter()

# Creazione animali
cane1 = Dog("d1", "Rex", 3, 20.5, "Labrador", False)
cane2 = Dog("d2", "Astrid", 2, 21.5, "Pitbull", True)

gatto1 = Cat("c1", "Micia", 2, 4.3, False, "palla")
gatto2 = Cat("c2", "Luce", 5, 6, True, "Tubo")

# Aggiunta al rifugio
for animale in [cane1, cane2, gatto1, gatto2]:
    rifugio.add(animale)


# -------------------- ROUTE home --------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Animal Shelter API",
        "links": {
            "list_animals": "/animals",
            "sample_dog": "/animals/d1",
            "sample_cat": "/animals/c1",
            "dog_food": "/animals/d1/food",
            "dog_adoption": "/animals/d1/adoption"
        } 
    })

# -------------------- ROUTE  GET --------------------

@app.get("/animals")
def list_animals():
    lista = []
    for animale in rifugio.list_all():
        lista.append(animale.info())
    return jsonify(lista), 200

@app.get("/animals/<animal_id>")
def info(animal_id):
    animale = rifugio.get(animal_id)
    if animale is None:
        return jsonify({"error": "Animal not found"}), 404
    return jsonify(animale.info()), 200

@app.get("/animals/<animal_id>/food")
def daily_food(animal_id):
    animale = rifugio.get(animal_id)
    if animale is None:
        return jsonify({"error": "Animal not found"}), 404
    return jsonify({
        "id":animale.id,
        "daily_food_grams":animale.daily_food_grams()
    }), 200

@app.get("/animals/<animal_id>/adoption")
def adoption(animal_id):
    animale = rifugio.get(animal_id)
    if animale is None:
        return jsonify({"error": "Animal not found"}), 404
    
    if rifugio.is_adopted(animal_id):
        adopter_name = rifugio.adoptions[animal_id]
        return jsonify({
            "id": animale.id,
            "adopted": True,
            "adopter_name": adopter_name
        }), 200
    else:
        return jsonify({
            "id": animale.id,
            "adopted": False
        }), 200

# -------------------- ROUTE POST --------------------

@app.post("/animals/add")
def add_animal():
    data = request.get_json()

    if "type" not in data:
        return jsonify({"error: Missing 'type' field"}), 400
    
    animal_type = data["type"]

    if animal_type != "dog" and animal_type != "cat":
        return jsonify({"error": "Invalid animal type"}), 400
    
    required_fields = ["id", "name", "age_years", "weight_kg"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    animal_id = data["id"]

    if rifugio.get(animal_id) is not None:
        return jsonify({"error": f"Animal with ID {animal_id} already exists"}), 400

    if animal_type == "dog":
        dog_fields = ["breed", "is_trained"]
        for field in dog_fields:
            if field not in data:
                return jsonify({"error": f"Missing field for dog: {field}"}), 400
                
        animale = Dog(
            data["id"],
            data["name"],
            data["age_years"],
            data["weight_kg"],
            data["breed"],
            data["is_trained"]
        )

    else:
        cat_fields = ["indoor_only", "favorite_toy"]
        for field in cat_fields:
            if field not in data:
                return jsonify({"error": f"Missing field for cat: {field}"}), 400

        animale = Cat(
            data["id"],
            data["name"],
            data["age_years"],
            data["weight_kg"],
            data["indoor_only"],
            data["favorite_toy"]
        )

    rifugio.add(animale)

    return jsonify({
        "status": "ok",
        "added": {
            "id": animale.id,
            "species": animale.species()
        }
    }), 200

@app.post("/animals/<animal_id>/adopt")
def animal_adopted(animal_id):
    animale = rifugio.get(animal_id)
    if animale is None:
        return jsonify({"error": "Animal not found"}), 404
    data = request.get_json()
    if not data or "adopter_name" not in data:
        return jsonify({"error": "Missing 'adopter_name' in request"}), 400

    adopter_name = data["adopter_name"]

    if rifugio.is_adopted(animal_id):
        return jsonify({
            "error": "Animal already adopted",
            "id": animal_id,
            "adopter_name": rifugio.adoptions[animal_id]
        }), 400

    rifugio.set_adopted(animal_id, adopter_name)


    return jsonify({
        "id": animal_id,
        "adopted": True,
        "adopter_name": adopter_name
    }), 200

# ----------------------- RUN ------------------------

app.run(debug=True)