from flask import Flask, Response, jsonify, request
import json

app = Flask(__name__)

def read_json_from_file(filename):
    """Reads JSON data from a file and returns it as a dictionary."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        return {"error": str(e)}

@app.route('/get-json', methods=['GET'])
def send_json():
    data = read_json_from_file("cats.json")

    # Validate JSON structure
    if "hierarchies" not in data or not isinstance(data["hierarchies"], list):
        return jsonify({"error": "Invalid JSON format"}), 400

    hierarchies = data["hierarchies"]

    # Get pagination parameters
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("size", 10))

    if page < 1 or page_size < 1:
        return jsonify({"error": "page and size must be positive integers"}), 400

    total_items = len(hierarchies)
    total_pages = (total_items + page_size - 1) // page_size

    # Pagination
    start = (page - 1) * page_size
    end = start + page_size
    paginated_data = hierarchies[start:end]

    response_data = {
        "page_info" : {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        },
        "hierarchies": paginated_data
    }

    return Response(json.dumps(response_data, indent=4), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
