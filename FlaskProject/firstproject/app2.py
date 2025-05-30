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
    data = read_json_from_file("attrval.json")

    # Validate JSON structure
    if "values_lists" not in data or not isinstance(data["values_lists"], list):
        return jsonify({"error": "Invalid JSON format"}), 400

    values_lists = data["values_lists"]

    # Get pagination parameters
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("size", 10))

    if page < 1 or page_size < 1:
        return jsonify({"error": "page and size must be positive integers"}), 400

    total_items = len(values_lists)
    total_pages = (total_items + page_size - 1) // page_size

    # Pagination
    start = (page - 1) * page_size
    end = start + page_size
    paginated_data = values_lists[start:end]

    response_data = {
        "page_info" : {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        },
        "values_lists": paginated_data
    }

    return Response(json.dumps(response_data, indent=4), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
