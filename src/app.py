from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{'label':'My 1st task','done':False,'id':1}]

@app.route('/todos', methods=['GET'])
def send_todos():
    return jsonify(todos),200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    if request_body is None:
        return jsonify({'msg':'body is none'}), 400
    print("Incoming request with the following body", request_body)
    if request_body is not None:
        todos.append(request_body)
        return jsonify(todos),200
    
@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
        return jsonify({'msg':'Deleted','updated': todos}),200 
    else: return jsonify({'msg':'todo not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)