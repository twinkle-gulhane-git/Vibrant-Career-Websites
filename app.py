from flask import Flask, render_template ,jsonify
app = Flask(__name__)

Jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs.15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco,USA',
    'salary':'$120,000'
  }
]
@app.route("/")
def hello():
    return render_template('home.html',jobs=Jobs,Company_name='Vibrant')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)

if __name__ == "__main__":
  app.run('0.0.0.0',debug=True)