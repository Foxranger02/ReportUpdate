import pandas
from flask import Flask,render_template,jsonify,request,json,send_file
from df import result




app = Flask(__name__)

@app.route("/")
def home():
    if request.is_json :
        text = request.args.get("datau")
        df = pandas.read_csv("handwashing_report.csv")
        l = len(df)
        print(len(df))
        df = json.loads(df.to_json())
        return jsonify({"report":df,
        "l":l})


    return render_template("home.html",f=result[-1],s=result[-2],t=result[-3])
@app.route("/report")
def report():
    if request.is_json :
        text = request.args.get("datau")
        df = pandas.read_csv("handwashing_report.csv")
        l = len(df)
        print(len(df))
        df = json.loads(df.to_json())
        return jsonify({"report":df,
        "l":l})
    return render_template("report.html")

@app.route("/download")
def download_file():
    path = "handwashing_report.csv"
    return send_file(path,as_attachment=True)

@app.route("/instagram")
def insta():
    path = 'templates/img/instagram.png'
    return send_file(path)


@app.route("/first")
def first():
    path = r'templates\Images'

    return send_file(path+f'\{result[-1]}.jpg')

@app.route("/second")
def second():
    path = r'templates\Images'

    return send_file(path+f'\{result[-2]}.jpg')

@app.route("/third")
def third():
    path = r'templates\Images'

    return send_file(path+f'\{result[-3]}.jpg')

if __name__ == "__main__":
    app.run(debug=True)
