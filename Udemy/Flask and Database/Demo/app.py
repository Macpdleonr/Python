from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test12345:app9flask@test12345.mysql.pythonanywhere-services.com/test12345$height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
  __tablename__ = 'data'
  id = db.Column(db.Integer, primary_key=True)
  email_ = db.Column(db.String(120), unique=True)
  height_ = db.Column(db.Integer)

  def __init__(self, email_, height_):
    self.email_ = email_
    self.height_ = height_

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
  global file
  if request.method == 'POST':

    file = request.files['file']
    file.save(secure_filename("uploaded_"+file.filename))

    with open("uploaded_"+file.filename, 'a') as file:
      file.write("This was added later")

    content = file.read().decode('utf-8')

    print(content)
    print(file)
    print(type(file))

    email = request.form['email_name']
    height = request.form['height_name']

    print(request.form)

    if db.session.query(Data).filter(Data.email_ == email).count() == 0:
      data = Data(email, height)
      db.session.add(data)
      db.session.commit()
      average_height = db.session.query(func.avg(Data.height_)).scalar()
      average_height = round(average_height, 1)
      count = db.session.query(Data.height_).count()

      send_email(email, height, average_height, count)
      print(average_height)

      return render_template('success.html')
    
    return render_template(
      'index.html',
      btn="download.html",
      text="Seems like we've got something from that email address already!"
      )
  
@app.route('/download')
def download():
  return send_file("uploaded_"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
  app.debug=True
  app.run()