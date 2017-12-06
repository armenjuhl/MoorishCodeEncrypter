from flask import Flask, request
import myCaesar 

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
        <form action="/" method="post">
        Rotate by: 
        <input type="text" name="rot"value="0"
            <br>
            <textarea type"text" name="text">{0}</textarea>    
            <input type="submit" value="encrypt phrase">
        </form>

    </body>
</html>
"""
@app.route("/", methods=['POST'])    

def encrypt():

    rotation_number=int(request.form['rot'])
    phrase=request.form["text"]
    encryptedTxt = myCaesar.encrypt(phrase, rotation_number)
    return form.format(encryptedTxt)
    
@app.route("/")    
def index():
    return form.format('')

app.run()