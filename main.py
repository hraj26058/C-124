from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[{
    'id': 1,
    'title': u'Buy Grocery',
    'description': u'Milk,Cheese,Pizza,Vegetables,Fruits',
    'done': False
    },
    {
    'id': 2,
    'title': u'Learn Python',
    'description': u'Need to find good python tutorial online',
    'done': False
    }]
@app.route("/")
def hello_world():
    return "Hello World!"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)
    task={
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        'status': 'success',
        'message': 'Task added successfully'
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        'data': tasks
    })
if(__name__=="__main__"):
    app.run(debug=True)