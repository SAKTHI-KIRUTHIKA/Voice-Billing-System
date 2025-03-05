from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")
db = client["voice_bill_db"]
collection = db["store_groceries"]

# API to get all items
@app.route("/api/bills", methods=["GET"])
def get_bills():
    bills = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ObjectId
    return jsonify(bills)

@app.route('/delete-bill', methods=['DELETE'])
def delete_bill():
    try:
        data = request.json
        item_name = data.get("ItemName")  # Identify the item by name

        if not item_name:
            return jsonify({"error": "ItemName is required"}), 400

        result = collection.delete_one({"ItemName": item_name})

        if result.deleted_count > 0:
            return jsonify({"message": "Deleted successfully!"}), 200
        else:
            return jsonify({"error": "Item not found!"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/edit-bill', methods=['PUT'])
def edit_bill():
    try:
        data = request.json
        item_name = data.get("ItemName")  # Identify item by name
        updated_data = {key: value for key, value in data.items() if key != "ItemName"}

        if not item_name or not updated_data:
            return jsonify({"error": "ItemName and at least one update field are required"}), 400

        result = collection.update_one(
            {"ItemName": item_name},  # Find item
            {"$set": updated_data}    # Update fields
        )

        if result.modified_count > 0:
            return jsonify({"message": "Updated successfully!"}), 200
        else:
            return jsonify({"error": "Item not found or no changes made!"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5002)  # Run MongoDB API on port 5002
