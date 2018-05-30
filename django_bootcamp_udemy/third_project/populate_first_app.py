import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'third_project.settings')

import django
django.setup()

import random
from first_app.models import WebPage, Topic, AccessRecord
from faker import Faker




faker_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        top = add_topic()

        fake_url = faker_gen.url()
        fake_date = faker_gen.date()
        fake_name = faker_gen.name()

        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populate start')
    populate(20)
    print('populate complete')
