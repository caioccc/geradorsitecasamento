from django.core.management.base import BaseCommand, CommandError
from app.models import *
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Script para deletar Template Base'

    def handle(self, *args, **options):
        try:
            pi = Pagina_Inicio.objects.all().delete()
            pn = Pagina_Noivos.objects.all().delete()
            noivo = Noivo.objects.all().delete()
            noiva = Noiva.objects.all().delete()
            pf = Pagina_Frase.objects.all().delete()
            pt = Pagina_Timeline.objects.all().delete()
            pc = Pagina_Contador.objects.all().delete()
            pg = Pagina_Galeria.objects.all().delete()
            pp = Pagina_Padrinhos.objects.all().delete()
            pr = Pagina_RSVP.objects.all().delete()
            pl = Pagina_ListaPresentes.objects.all().delete()
            pm = Pagina_Mural.objects.all().delete()
            pfo = Pagina_Footer.objects.all().delete()
            recep = Recepcao.objects.all().delete()
            cat = CategoriaGaleria.objects.all().delete()
            users = User.objects.all().delete()
        except (Exception,):
            raise CommandError('Erro ao deletar Paginas')
        self.stdout.write(self.style.SUCCESS('Successfully deleted'))
