from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data scientist',
    'location': 'Bengalaru, India',
    'salary': 'R$ 10,000, 00'
  },
  {
    'id': 2,
    'title': 'Data engener',
    'location': 'New York, EUA',
    'salary': 'R$ 15,000, 00'
  },
  {
    'id': 3,
    'title': 'Frontend developer',
    'location': 'Sao Paulo, Brasi',
    'salary': 'R$ 8,000, 00'
  }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
  
  
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)