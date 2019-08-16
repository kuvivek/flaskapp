from flask import Flask, request
import resources

app = Flask(__name__)

@app.route('/keys', methods=['GET', 'POST', 'DELETE'])
def ChoresList():

    if request.method == 'GET':
        return resources.get_chores()

    elif request.method == 'POST':
        chore = request.get_json()
        return resources.makeANewChore(chore)

    elif request.method == 'DELETE':
        return resources.deleteAllChores()

@app.route('/keys/<title>', methods=['HEAD', 'PUT', 'DELETE'])
def Chores(title):
    if request.method == 'HEAD':
        return resources.get_chore(title)

    elif request.method == 'PUT':
        chore = request.get_json()[title]
        return resources.updateChore(title, chore)

    elif request.method == 'DELETE':
        return resources.deleteAChore(title)

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=5000)
