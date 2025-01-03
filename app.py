from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///project.db"
app.config['SQLALCHEMY_RACK_MODIFICATIONs']=False
db=SQLAlchemy(app)

class Sql(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    BookName=db.Column(db.String(500), nullable=False)
    IssueDate=db.Column(db.String(500), nullable=False)
    MemberName=db.Column(db.String(500), nullable=False)
    Class=db.Column(db.String(500), nullable=False)
    def __repr__(self):
        return f"{self.sno} - {self.BookName } - {self.IssueDate}-{self.MemberName}"

@app.route("/")
def Library():
    sql=Sql(BookName="Python",IssueDate="20-03-2020",MemberName="Gautam")
    db.session.add(sql)
    db.session.commit()
    final = Sql.query.all()

    return render_template("index.html", final=final)
@app.route("/show")
def Library2():
    final=Sql.query.all()
    print(final)
@app.route('/update/<int:sno>')
def update(sno):
    final=Sql.query.filter_by(sno=sno)
    return render_template('index.html',final=final)
@app.route('/delete/<int:sno>')
def delete(sno):
    final=Sql.query.filter_by(sno=sno)
    db.session.delete(final)
    db.session.commit()

if __name__=="__main__":
    app.run(debug=True, port=5000)