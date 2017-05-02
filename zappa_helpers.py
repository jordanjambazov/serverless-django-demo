from django.contrib.auth.models import User


def create_superuser():
    User.objects.create_superuser('jordan', 'jordan@era.io', 'demodemo')
