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
def caes_encrypt():
    rotation_number=int(request.form['rot'])
    phrase=request.form["text"]
    session['caesKey'] = rotation_number
    session['caesText'] = phrase
    encryptedTxt = myCaesar.encrypt(phrase, rotation_number)
    return render_template('caesarEncrypted.html', encryptedTxt=encryptedTxt, rotation_number=rotation_number)

@app.route("/decrypt1", methods=['GET', 'POST'])
def decrypt1():
    if request.method== 'GET':        
        return render_template('decrypt1.html')
    elif request.method== 'POST':
        caesKey = request.form['decKey1']
        caesText = request.form['dec1-message']
        session['caesKey'] = caesKey
        session['caesText'] = caesText
        return redirect('/caesDecrypted')

@app.route("/caesDecrypted", methods=['GET'])
def caesDecrypted():
    caesText2 = session['caesText']
    key = session['caesKey']
    key = (key * -1) +1
    caesTextDecrypted = myCaesar.encrypt(caesText2, key)
    return render_template('caesDecrypted.html', caesTextDecrypted=caesTextDecrypted)

# VIGENEGER /////////////////// \/
@app.route("/vigenere", methods=['GET'])
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=['POST'])
def vig_encrypt():
    text = request.form['vigText']
    key = request.form['vigKey']
    session['vig-text'] = text
    session['vig-key'] = key
    vigEncrypted = myVigenere.vigenere(text, key)
    return render_template('vigEncrypted.html', vigEncrypted=vigEncrypted, key=key)

@app.route("/decrypt2", methods=['GET', 'POST'])
def decrypt2():
    if request.method== 'GET':        
        return render_template('decrypt2.html')
    elif request.method== 'POST':
        vigText = request.form['decKey2']
        session['vig-text'] = vigText
        vigKey = request.form['dec2-message']
        session['vig-key'] = vigKey
        return redirect('/vigDecrypted')

@app.route("/vigDecrypted", methods=['GET'])
def vigDecrypted():
    vigText = session['vig-text']
    vigKey = session['vig-key']
    # vigText
    vigDecrypted = myVigenere.decryptVigenere(vigText, vigKey)
    return render_template('vigDecrypted.html', vigDecrypted=vigDecrypted)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

app.run()