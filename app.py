from flask import Flask,render_template,request
import requests
api_key = "7a375a390722b1d7dd53daa4ebd8d683"
url = "http://data.fixer.io/api/latest?access_key=" + api_key
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")

        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue / firstValue) * float(amount)
        currencyinfo = dict()
        currencyinfo["firstCurrency"] = firstCurrency
        currencyinfo["secondCurrency"] = secondCurrency
        currencyinfo["amount"] = amount
        currencyinfo["result"] = result


        return render_template("index.html",info = currencyinfo)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)