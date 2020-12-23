from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
image_default = "https://tinyurl.com/demo-cupcake"


class CupCake(db.Model):
    """Creates the cupckate table"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                     nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.Text,
                      nullable=False)

    def image_url(self):
        """Handles image URL""""

        return self.image or image_default

    def serialized(self):
        """Handles serializing SQLAlchemy Response"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }


def connect_db(app):
    """"Connect to database""""

    db.app = app
    db.init_app(app)
