from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user id" : user_id,
        "email" : "john@gmail.com"
    }
    
    name = request.args.get("name")
    if name:
        user_data["name"] = name
        
    return jsonify(user_data),200

if __name__ == "__main__":
    app.run(debug=True)