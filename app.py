import os, jsonpickle
from flask import Flask, request, Response
from waitress import serve

from tf import Model
from loadimage import Gambar

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
mime = ['image/jpeg', 'image/png']

def post_image(img_file):
    """ post image and return the response """
    img = open(img_file, 'rb').read()
    response = requests.post(URL, data=img, headers=headers)
    return response
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file'].read()
        img = Gambar(img)
        mdl = Model()

        img.load()
        mdl.compile()

        pred = mdl.predict_model(img.shape())


        response = {'prediction': f'{pred}' }
        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=200, mimetype="application/json")
    else:
        response = {'error':  'no file'}
        return Response(response=response, status=400, mimetype="application/json")


# start flask app
if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port=5000)
    serve(app, host='0.0.0.0', port=8080)
