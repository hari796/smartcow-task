import logging
from flask import Flask, jsonify
from flask_cors import CORS
import memory_profiler as mp   # <----

logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - "
                      "%(name)s:%(lineno)d [-] %(funcName)s- %(message)s")
logger.setLevel(logging.INFO)


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


@mp.profile
def health_check():
   return jsonify({"message": "success"})


app.add_url_rule(rule='/health', endpoint='health-check', 
    view_func=health_check, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=500)
