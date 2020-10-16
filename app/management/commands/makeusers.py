from django.core.management.base import BaseCommand, CommandError
from app.models import *

from django.contrib.auth.models import User, Permission


class Command(BaseCommand):
    help = 'Script para gerar users'

    def handle(self, *args, **options):
        superuser_data = {
            'username': 'caio',
            'first_name': 'Caio',
            'email': 'caiomarinho8@gmail.com',
            'password': 'oficinag3'
        }
        commonuser_data = {
            'username': 'usuario',
            'first_name': 'Usuario',
            'password': 'Admin123!'
        }
        try:
            User.objects.create_superuser(username=superuser_data['username'],
                                          email=superuser_data['email'],
                                          password=superuser_data['password'])

            User.objects.create_user(username=commonuser_data['username'], email=None,
                                     password='admin123')
            user = User.objects.get(username='usuario')
            user.is_staff = True
            user.user_permissions.add(Permission.objects.get(codename='add_recado'),
                                      Permission.objects.get(codename='view_recado'),
                                      Permission.objects.get(codename='change_recado'),
                                      Permission.objects.get(codename='delete_recado'),
                                      Permission.objects.get(codename='add_rsvp'),
                                      Permission.objects.get(codename='view_rsvp'),
                                      Permission.objects.get(codename='change_rsvp'),
                                      Permission.objects.get(codename='delete_rsvp'))
            user.save()
        except (Exception,):
            raise CommandError('Erro ao gerar usuarios')
        self.stdout.write(self.style.SUCCESS('Successfully users created'))
