from flask import Flask, jsonify
from flask_cors import CORS

import scraping_script
import selenium_script

app = Flask(__name__)
CORS(app)

@app.route('/api/get-random-book', methods=['GET'])
def get_random_book():
    random_book = selenium_script.get_random_book()
    return jsonify(random_book)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3425)