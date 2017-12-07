from flask import Flask, request, render_template
import myCaesar 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/encrypted", methods=['POST'])    
def encrypt():
    rotation_number=int(request.form['rot'])
    phrase=request.form["text"]
    encryptedTxt = myCaesar.encrypt(phrase, rotation_number)
    return render_template('encrypted.html', encryptedTxt=encryptedTxt, rotation_number=rotation_number)

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
