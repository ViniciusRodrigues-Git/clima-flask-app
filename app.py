import requests
from flask import Flask, render_template , request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
     if request.method == "POST":
             cidade = request.form.get("cidade")
             api_key = "13eb6ab9cd2b6550da7520ff68d5bbb9"
             url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

             resposta = requests.get(url)
             dados_clima = resposta.json()

             temp = dados_clima["main"]["temp"]
             desc = dados_clima["weather"][0]["description"]
             umid = dados_clima["main"]["humidity"]

             return render_template("index.html", temp=temp, desc=desc, umid=umid)   
     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)