from flask import Flask, jsonify, request
app = Flask(__name__)

contacts = [
    {
        'Contact': 6364002187,
        'Name': u'Shwetha'
        #when u is used, all special characters within quotes dont have special meaning.
        'done': False,
        'id': 1    },
    { 'id':2,
      'Contact': 9108753006,
      'Name': u'Divya'
        #when u is used, all special characters within quotes dont have special meaning.
      'done': False,}
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods =["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "please provide the data!"
        }, 400)

    new_contact = {
            'id': contacts[-1]['id'] + 1,
            'Contact': request.json['Contact'],
            'Name': request.json.get('Name'),
            'done': False
        }
    contacts.append(new_contact)
    return jsonify({
        "status": "success" ,
        "message": "contact added successfully!"

    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })
if(__name__ == "__main__"):
    app.run(debug = True)


