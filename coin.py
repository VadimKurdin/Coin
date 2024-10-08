from flask import Flask
import random
app = Flask(__name__)

facts = ['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
         'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
          'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
          'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.']

coin = ['орёл','решка']

@app.route("/ff")
def f():
    random_facts = random.choice(facts)
    return f'<h1>{random_facts}</h1>'

@app.route("/f")
def random_coins():
    random_coin ='Выпало: ' + random.choice(coin)
    return f'<h1>{random_coin}</h1>'

@app.route("/")
def dialog():
    dialog_text = '<a href="/f">Нажмите чтобы подбросить монетку</a>'
    dialog_text +='</p> <a href="/ff">Посмотреть случайный факт!</a>'
    return dialog_text

app.run(debug=True)
