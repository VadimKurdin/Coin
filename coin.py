from flask import Flask
import random
app = Flask(__name__)

coin = ['орёл','решка']

@app.route("/f")
def f():
    random_coin ='Выпало: ' + random.choice(coin)
    return f'<h1>{random_coin}</h1>'
    
@app.route("/")
def hello_world():
    return '<a href="/f">Нажмите чтобы подбросить монетку</a>'

app.run(debug=True)
