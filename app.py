from flask import Flask, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "title": 'Product 1',
        "price": 150 
    },
    {
        "id": 2,
        "title": 'Product 2',
        "price": 500 
    }
    ]

@app.route('/')
def hello():
    return '<h1>Hello World!<h1>'

@app.route('/second')
def another_route():
    return '<h1>This is another route!<h1>'

@app.route('/products')
def all_products():
    return products

# Get product with id == 1
@app.route('/products/<int:id>')
def one_product(id):
    # print(type(id))
    filtered_products = list(filter(lambda p: p['id'] == id, products))
    # print(list(filtered_products))
    return filtered_products[0]

@app.route('/can-vote')
def can_vote():
    age = int(request.args.get('age'))
    # age = 20
    if age >= 18:
        return {"message": 'You can vote!', "can_vote": True}
    else:
        return {"message": 'You''re not old enough to vote!', "can_vote": False}