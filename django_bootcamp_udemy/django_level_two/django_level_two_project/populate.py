import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_level_two_project.settings')
import django
django.setup()
from users.models import Users
from faker import Faker


faker_gen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_first_name = faker_gen.first_name()
        fake_last_name = faker_gen.last_name()
        fake_email = faker_gen.email()

        user = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name,
                                           email=fake_email)[0]


if __name__ == '__main__':
    print('populate start')
    populate(20)
    print('populate complete')
