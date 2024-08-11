from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Drawings data
drawings = [
    {'id': 1, 'title': 'Sunset Bliss', 'price': 1499, 'image': 'baby.jpg'},
    {'id': 2, 'title': 'Mountain Peace', 'price': 1999, 'image': 'bg.jpg'},
    {'id': 3, 'title': 'Ocean Waves', 'price': 1999, 'image': 'dog.jpg'},
    {'id': 4, 'title': 'Forest Calm', 'price': 3999, 'image': 'family.jpg'},
    {'id': 5, 'title': 'Desert Mirage', 'price': 1999, 'image': 'kiss.jpg'},
    {'id': 6, 'title': 'Desert Mirage', 'price': 1999, 'image': 'love.jpg'},
    {'id': 7, 'title': 'Desert Mirage', 'price': 1499, 'image': 'pelli.jpg'},
    {'id': 8, 'title': 'Desert Mirage', 'price': 1499, 'image': 'romace.jpg'},
    {'id': 9, 'title': 'Desert Mirage', 'price': 1999, 'image': 'wed.jpg'},
    {'id': 10, 'title': 'Desert Mirage', 'price': 1999, 'image': 'wedding.jpg'}
]

# Cart data
shopping_cart = []

@app.route('/')
def home():
    return render_template('home.html', drawings=drawings)

@app.route('/add-to-cart/<int:drawing_id>')
def add_to_cart(drawing_id):
    drawing = next((d for d in drawings if d['id'] == drawing_id), None)
    if drawing:
        shopping_cart.append(drawing)
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=shopping_cart)

@app.route('/buy-now/<int:drawing_id>')
def buy_now(drawing_id):
    add_to_cart(drawing_id)
    return redirect(url_for('view_cart'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/create-account')
def create_account():
    return render_template('create_account.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
