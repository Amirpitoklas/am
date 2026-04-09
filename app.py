from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

@app.route('/')
def home():
    items = Item.query.all()
    return render_template('home.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    price = int(request.form['price'])
    db.session.add(Item(name=name, price=price))
    db.session.commit()
    return redirect('/')

@app.route('/bid/<int:id>', methods=['POST'])
def bid(id):
    item = Item.query.get(id)
    new_price = int(request.form['price'])

    if new_price > item.price:
        item.price = new_price
        db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
