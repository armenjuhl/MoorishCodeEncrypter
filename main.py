import os
from flask import Flask, request, render_template, session, redirect
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
    session['vig-text'] = text
    key = request.form['vigKey']
    session['vig-key'] = key
    vigEncrypted = myVigenere.vigenere(text, key)
    return render_template('vigEncrypted.html', vigEncrypted=vigEncrypted, key=key)

# @app.route("/decrypt1", methods=['GET'])
#     return render_template('')

@app.route("/decrypt2", methods=['GET', 'POST'])
def decrypt2():
    if request.method== 'GET':        
        return render_template('decrypt2.html')
    elif request.method== 'POST':
        vigText = request.form['decKey2']
        session['vig-text'] = vigText
        vigKey = request.form['dec2-message']
        return redirect('/vigDecrypted')

@app.route("/vigDecrypted", methods=['GET'])
def vigDecrypted():
    vigText = session['vig-text']
    return render_template('vigDecrypted.html', vigText=vigText)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

app.run()