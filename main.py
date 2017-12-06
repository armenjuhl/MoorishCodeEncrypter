from flask import Flask, request, redirect, render_template, session, flash, json
import myCaesar 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def caesar():
    return render_template('caesar.html')

@app.route("/encrypted", methods=['GET', 'POST'])    
def encrypt():
    rotation_number = int(request.form['rotateBy'])
    phrase = str(request.form['encryption'])
    encryptedTxt = myCaesar.encrypt(rotation_number, phrase)
    return render_template('encrypted.html', encryptedTxt=encryptedTxt, rotation_number=rotation_number, phrase=phrase)
    

app.secret_key = 'asdA8975dhj/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == '__main__':
    app.run()