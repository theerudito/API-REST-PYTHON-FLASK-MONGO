from flask import Flask,  request, jsonify
import data_base as dbase
from character import Characters
from bson.objectid import ObjectId

# CONECTION TO DATABASE
db = dbase.DB_CONNECTION()

app = Flask(__name__)


# ROUTE APP
@app.route('/', methods=['GET'])
def home():
    return '<h1>I am Backend </h1>'


#==================== GET ALL CHARACTERS =====================
@app.route('/characters', methods=['GET'])
def getCharacter():
    try:
        characters = db["naruto"]
        result = []
        for character in characters.find():
            print(character)
            result.append({
                "id": str(character["_id"]),
                'name': character['name'],
                'age': character['age'],
                'clan': character['clan'],
                'pic': character['pic']
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"message": "No Data: "})
#==================== GET ALL CHARACTERS =====================      
  


#==================== GET ONE CHARACTER ======================
@app.route('/characters/<id>', methods=['GET'])
def getOneCharacter(id):
    try:
        characters = db["naruto"]
        result = []
        for character in characters.find({"_id": ObjectId(id)}):
            result.append({
                "id": str(character["_id"]),
                'name': character['name'],
                'age': character['age'],
                'clan': character['clan']
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"message": "No Data: "})
#==================== GET ONE CHARACTER ======================



#==================== CREATE PRODUCT =========================
@app.route('/characters', methods=['POST'])    
def createCharacter():
  try:
    # access the database
    character = db["naruto"]
    # create a new character
    name: str = request.json['name']
    age: int = request.json['age']
    clan: str = request.json['clan']
    pic: str = request.json['pic']

    if name and age and clan:
        new_character = Characters(name, age, clan, pic)
        # insert the new character in the database
        character.insert_one(new_character.DBCollection())
        # return the new character
        return jsonify({"message": "Character created"})
    else:
        return jsonify({"message": "Error: Missing data"}) 
  except Exception as e:
    return jsonify({"message": "Error: " + str(e)})
#==================== CREATE PRODUCT =========================    
    


#==================== UPDATE CHARACTER =======================
@app.route('/characters/<id>', methods=['PUT'])
def updateCharacter(id):
  try:
      # access the database
    character = db["naruto"]
    # update the character
    name: str = request.json['name']
    age: int = request.json['age']
    clan: str = request.json['clan']

    if name and age and clan:
        character.update_one({"_id": ObjectId(id)}, {'$set': {'name': name, 'age': age, 'clan': clan}})
        return jsonify({"message": "Character updated"})
    else:
        return jsonify({"message": "Error: Missing data"})
  except Exception as e:
    return jsonify({"message": "Error: " + str(e)})      
#==================== UPDATE CHARACTER =======================
               


#==================== DELETE CHARACTER =======================
@app.route('/characters/<id>', methods=['DELETE'])
def deleteCharacter(id):
  try:
    # access the database
    character = db["naruto"]
    # delete the character
    character.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Character deleted"})
  except Exception as e:
    return jsonify({"message": "Error: " + str(e)})
#==================== DELETE CHARACTER =======================    
        


#==================== PAGE NOT FOUND =========================
@app.errorhandler(404)   
def page_not_found(e: None):
  message = {
    'status': 404,
    'message': 'Page Not Found: ' + request.url
  }
  return jsonify(message)  
#==================== PAGE NOT FOUND =========================  

# RUN APP
if __name__ == '__main__':
    app.run(debug=True, port=5000)

    
      

