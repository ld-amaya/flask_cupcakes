from flask import Flask, request, render_template, jsonify, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Cupcake, db, connect_db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'iamlou'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    """Returns the homepage"""
    return render_template("index.html")

####### API GET REQUESTS #######################################################


@app.route("/api/cupcakes")
def display_cupcakes():
    """Handles cupcake api request"""
    cupcakes = [cupcake.serialized() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:id>")
def display_a_cupcake(id):
    """Handles single cupcake request based on ID"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialized())


####### API POST REQUESTS #######################################################

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcakes():
    """Handles API Post Request to add new Cupcake"""

    data = request.json
    cupcake = Cupcake(
        flavor=data['flavor'],
        size=data['size'],
        rating=data['rating'],
        image=data['image'] or None)
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialized()), 201)


####### API PATCH REQUESTS #######################################################


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def edit_cupcake(id):
    """Handles patch api request based on cupcake id"""
    data = request.json
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialized()))


####### API DELETE REQUESTS #######################################################
@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """Handles delete api request based on cupcake ID"""

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
