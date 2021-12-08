import json
from flask import Flask
from flask import request
from collections import defaultdict

app = Flask(__name__)
db = defaultdict(list)

@app.route('/list/<list_id>')
def list(list_id, methods=['GET']):
    return json.dumps(db[list_id])

@app.route('/upload')
def upload(methods=['GET']):
    db[request.args['list_id']].append((request.args['ipfs_hash'], request.args['name']))
    return ''

if __name__ == "__main__":
    app.run()
