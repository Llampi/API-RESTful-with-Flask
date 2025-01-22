from flask import Flask, jsonify, request
from api.users import usuarios_blueprint
app = Flask(__name__)
app.register_blueprint(usuarios_blueprint)

if __name__ == '__main__':
    app.run(debug=True)