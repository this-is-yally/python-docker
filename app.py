from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data store (in-memory dictionary)
data_store = {
    '1': {'name': 'John', 'age': 30},
    '2': {'name': 'Alice', 'age': 25},
    '3': {'name': 'Bob', 'age': 35}
}

@app.route('/')
def hello_world():
    return 'Hello, my dear viewer/recruiter! This is a more complex Flask example.'

# Route to retrieve a specific user by ID
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_store.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Route to create a new user
@app.route('/user', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json or 'age' not in request.json:
        return jsonify({'error': 'Invalid data format'}), 400

    user_id = str(len(data_store) + 1)
    new_user = {
        'name': request.json['name'],
        'age': request.json['age']
    }
    data_store[user_id] = new_user
    return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201

# Route to update an existing user by ID
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in data_store:
        return jsonify({'error': 'User not found'}), 404

    if not request.json:
        return jsonify({'error': 'Invalid data format'}), 400

    user = data_store[user_id]
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    data_store[user_id] = user

    return jsonify({'message': 'User updated successfully', 'user': user})

# Route to delete a user by ID
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in data_store:
        return jsonify({'error': 'User not found'}), 404

    del data_store[user_id]
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
