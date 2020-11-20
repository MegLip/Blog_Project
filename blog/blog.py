from flask import Flask
from blog.models import Entry, db
from faker import Faker


app = Flask(__name__)


def generate_entries(how_many=3):
    fake = Faker()

    for i in range(how_many):
        post = Entry(
            title=fake.sentence(),
            body='\n'.join(fake.paragraphs(15)),
            is_published=True
        )
        db.session.add(post)
    db.session.commit()
