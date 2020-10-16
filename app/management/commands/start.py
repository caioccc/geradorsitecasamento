from django.core.management.base import BaseCommand, CommandError
from app.models import *


class Command(BaseCommand):
    help = 'Script para gerar Template Base'

    def handle(self, *args, **options):
        try:
            pi = Pagina_Inicio()
            pi.save()
            pn = Pagina_Noivos()
            pn.save()
            pf = Pagina_Frase()
            pf.save()
            pt = Pagina_Timeline()
            pt.save()
            pc = Pagina_Contador()
            pc.save()
            pg = Pagina_Galeria()
            pg.save()
            pp = Pagina_Padrinhos()
            pp.save()
            pr = Pagina_RSVP()
            pr.save()
            pl = Pagina_ListaPresentes()
            pl.save()
            pm = Pagina_Mural()
            pm.save()
            pfo = Pagina_Footer()
            pfo.save()
        except (Exception,):
            raise CommandError('Erro ao gerar Paginas')
        self.stdout.write(self.style.SUCCESS('Successfully started'))
