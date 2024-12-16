from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory store
contacts = [
    {"id": 1, "name": "Alice", "number": "+351123456789"},
    {"id": 2, "name": "Bob", "number": "+351987654321"}
]

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts), 200

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data or 'name' not in data or 'number' not in data:
        return jsonify({"error": "Bad request"}), 400
    new_id = max([c["id"] for c in contacts] or [0]) + 1
    new_contact = {
        "id": new_id,
        "name": data["name"],
        "number": data["number"]
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad request"}), 400

    for c in contacts:
        if c["id"] == contact_id:
            c["name"] = data.get("name", c["name"])
            c["number"] = data.get("number", c["number"])
            return jsonify(c), 200

    return jsonify({"error": "Not found"}), 404

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c["id"] != contact_id]
    return '', 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
