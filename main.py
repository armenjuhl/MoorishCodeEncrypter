import os
from flask import Flask, request, render_template
import myCaesar 
import myVigenere

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/caesar", methods=['GET'])
def caesar():
    return render_template('caesar.html')

@app.route("/encrypted", methods=['POST'])    
def encrypt():
    rotation_number=int(request.form['rot'])
    phrase=request.form["text"]
    encryptedTxt = myCaesar.encrypt(phrase, rotation_number)
    return render_template('caesarEncrypted.html', encryptedTxt=encryptedTxt, rotation_number=rotation_number)

@app.route("/vigenere", methods=['GET'])
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=['POST'])
def vig_encrypt():
    text = request.form['vigText']
    key = request.form['vigKey']
    vigEncrypted = myVigenere.vigenere(text, key)
    return render_template('vigEncrypted.html', vig_encrypted=vigEncrypted, key=key)

# @app.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)

# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                      endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)

app.run()
# To Do: Incorporate index with base, 
# figure out background image, 
# structure, 
# styling














"""
form = 
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypted" method="post">
        Rotate by: 
        <input type="text" name="rot" value="0">
            <br>
            <textarea type"text" name="text">{0}</textarea>    
            <input type="submit" value="encrypt phrase">
        </form>

    </body>
</html>
@app.route("/", methods=['GET'])
def index():
    return form.format('')
"""
