"""
    Populating script
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django
django.setup()

import random
from faker import Faker
from first_app.models import AcessRecord, Topic, Webpage





FAKEGEN = Faker()

TOPICS = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic() -> Topic:
    """
    Get or Create Topic
    """
    t = Topic.objects.get_or_create(top_name=random.choice(TOPICS))[0]
    t.save()
    return t

def populate(N=5):
    """
    Get or Create Topic, Webpage and Access Record

    Keyword Arguments:
    N -- Iteractions to perform
    """
    for entry in range(N):
        top = add_topic()
        fake_url = FAKEGEN.url()
        fake_date = FAKEGEN.date()
        fake_name = FAKEGEN.company()

        webpb = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AcessRecord.objects.get_or_create(name=webpb, date=fake_date)

if __name__ == "__main__":
    print("Populating script")
    populate()
    print("Populating completed!")
