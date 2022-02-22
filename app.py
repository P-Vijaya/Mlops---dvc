from flask import Flask,render_template,request,jsonify
import os
import numpy as np


webapp_root = "webapp"

static_dir = os.path.join(webapp_root,"static")
template_dir = os.path.join(webapp_root,"templates")

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        try:
            pass
        except Exception as e:
            print(e)
            error = {"error":"Something went wrong!! Try again"}
            return render_template("404.html",error=error)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)