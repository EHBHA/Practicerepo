from flask import Flask, Response, request, jsonify
import json

app = Flask(__name__)

def read_json_from_file(filename):
    """Reads JSON data from a file and returns it as a dictionary."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        return {"error": str(e)}

@app.route('/receive-data', methods=['POST'])
def receive_data():
    try:

        tenant_id = request.headers.get("x-tenant-id")
        client_id = request.headers.get("x-client-id")
        business_group_id = request.headers.get("x-business-group-id")
        auth_token = request.headers.get("Authorization")


        if not all([tenant_id, client_id, business_group_id, auth_token]):
            return jsonify({"error": "Missing required headers"}), 400


        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400


        response_data = read_json_from_file("inventory.json")

        return Response(json.dumps(response_data, indent=4), mimetype='application/json')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
