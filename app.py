from flask import Flask,render_template,request,redirect

app = Flask(__name__)

graphs = [
        {"id": "testgraph", "graph": "a -> b -> c;", "urgency": "EXTREME"},
        {"id": "testgraph2", "graph": "a -> d -> c;", "urgency": "MINOR"},
        {"id": "testgraph3", "graph": "a -> e -> c;", "urgency": "MODERATE"},
        {"id": "testgraph4", "graph": "a -> g -> c;", "urgency": "MAJOR"}
        ]

@app.route('/')
def index_route():
  return render_template("index.html",data=graphs)

@app.route('/add', methods=["GET","POST"])
def add_route():
  if request.method == "GET":
    return render_template("add_new.html")
  elif request.method == "POST":
    graphs.append({"id": request.form["id"], "graph": request.form["graph"], "urgency": request.form["urgency"]})
    return redirect("/")

if __name__ == "__main__":
  app.run()
