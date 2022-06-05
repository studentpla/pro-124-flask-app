from flask import Flask,jsonify,request
app =  Flask(__name__)
contacts = [
    {
"id":1,
"number":"8817860316",
"name":"shanvika",
"done": False

},
 {
"id":2,
"number":"7000451220",
"name":"samiksha",
"done": False

}
]

@app.route("/adddata",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
        "status":"error",
        "message":"please provide the data!"

    },400)
    task = {
        'id': contacts[-1]['id'] + 1, 
        'number': request.json['number'], 
        'name': request.json.get('name', ""), 
        'done': False 
    }
    
    contacts.append(task) 
    return jsonify(
        {
             "status":"success",
            "message": "Task added succesfully!" 
            }
    )

@app.route("/get-data") 
def get_task(): 
    return jsonify({ 
        "data" : contacts
        })

if __name__ == "__main__":
    app.run(debug = True)