from flask import Flask,request,render_template
app = Flask(__name__)

r=""
first_time = 1

@app.route("/",methods=["GET","POST"])
def index():
  return (render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
  name = request.form.get("r")
  return(render_template("main.html",r=r))

@app.route("/imageGPT",methods=["GET","POST"])
def imageGPT():
  return(render_template("imageGPT.html"))

@app.route("/end",methods=["GET","POST"])
def end():
  first_time =1
  return(render_template("end.html"))



if __name__ == "__main__":
  app.run()
