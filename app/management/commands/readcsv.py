from django.core.management.base import BaseCommand, CommandError
from app.models import *
import pandas as pd
import datetime


class Command(BaseCommand):
    help = 'Script para preencher dados'

    PATH = './repo.csv'

    def add_arguments(self, parser):
        parser.add_argument('-csv')

    def read_csv(self, path):
        return pd.read_csv(path)

    def handle(self, *args, **options):
        if 'csv' in options:
            self.PATH = options['csv']
        df = self.read_csv(self.PATH)
        arr = df.values[0][1:]
        self.initialize()
        try:
            self.generate_noivo(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar noivo')
        try:
            self.generate_noiva(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar noiva')
        try:
            self.generate_recepcao(arr)
            self.generate_footer(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar recepcao')
        try:
            self.generate_timeline(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar timeline')
        try:
            self.generate_lista_presentes(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar lista de presentes')
        try:
            self.generate_galeria(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar galeria')
        try:
            self.generate_padrinhos(arr)
        except (Exception,):
            raise CommandError('Erro ao gerar padrinhos')
        self.stdout.write(self.style.SUCCESS('Successfully started'))

    def generate_padrinhos(self, arr):
        padrinhos = Pagina_Padrinhos()
        padrinhos.frase = ''
        padrinhos.save()
        for j in range(56, 62):
            if 'nan' not in str(arr[j]) or not len(str(arr[j])) == 3:
                padrinho = ItemPadrinho()
                padrinho.nome = arr[j]
                padrinho.foto_url = self.get_image_url(arr[j + 6])
                padrinho.pagina_padrinhos = padrinhos
                padrinho.save()

    def generate_galeria(self, arr):
        galeria = Pagina_Galeria()
        galeria.save()
        if False in [str(k).find('nan') != -1 for k in arr[44:48]]:
            categoria = CategoriaGaleria()
            categoria.titulo = 'Amigos'
            categoria.save()
            for i in range(44, 48):
                if 'nan' not in str(arr[i]):
                    foto = ItemGaleria()
                    foto.categoria = categoria
                    foto.foto_url = self.get_image_url(arr[i])
                    foto.galeria = galeria
                    foto.save()
        if False in [str(k).find('nan') != -1 for k in arr[48:52]]:
            categoria_2 = CategoriaGaleria()
            categoria_2.titulo = 'Família'
            categoria_2.save()
            for i in range(48, 52):
                if 'nan' not in str(arr[i]):
                    foto_2 = ItemGaleria()
                    foto_2.categoria = categoria_2
                    foto_2.foto_url = self.get_image_url(arr[i])
                    foto_2.galeria = galeria
                    foto_2.save()
        if False in [str(k).find('nan') != -1 for k in arr[52:56]]:
            categoria_3 = CategoriaGaleria()
            categoria_3.titulo = 'Diversos'
            categoria_3.save()
            for i in range(52, 56):
                if 'nan' not in str(arr[i]):
                    foto_3 = ItemGaleria()
                    foto_3.categoria = categoria_3
                    foto_3.foto_url = self.get_image_url(arr[i])
                    foto_3.galeria = galeria
                    foto_3.save()

    def generate_lista_presentes(self, arr):
        lista_presentes = Pagina_ListaPresentes()
        lista_presentes.save()
        for i in range(41, 44):
            item_lista = ItemListaPresentes()
            if 'nan' not in str(arr[i]):
                self.check_lista_presentes(arr[i], item_lista, lista_presentes)

    def generate_timeline(self, arr):
        timeline = Pagina_Timeline()
        timeline.texto_historia = arr[24]
        timeline.save()
        for i in range(25, 41, 4):
            if 'nan' not in str(arr[i]):
                item_timeline = ItemTimeline()
                item_timeline.timeline = timeline
                item_timeline.titulo = arr[i]
                item_timeline.foto_url = self.get_image_url(arr[i + 1])
                item_timeline.data = datetime.datetime.strptime(arr[i + 2], '%d/%m/%Y').strftime('%Y-%m-%d')
                if 'nan' in str(arr[i + 3]):
                    arr[i + 3] = ''
                item_timeline.descricao = arr[i + 3]
                item_timeline.save()

    def generate_footer(self, arr):
        footer = Pagina_Footer()
        footer.frase = arr[23]
        footer.save()

    def generate_recepcao(self, arr):
        recepcao = Recepcao()
        recepcao.local = arr[14]
        recepcao.data = datetime.datetime.strptime(arr[15], '%d/%m/%Y').strftime('%Y-%m-%d')
        recepcao.hora = arr[16]
        endereco = Endereco()
        endereco.rua = arr[17]
        if 'nan' in str(arr[18]):
            arr[18] = 'S/N'
        endereco.numero = arr[18]
        endereco.bairro = arr[19]
        endereco.cidade = arr[20]
        endereco.estado = arr[21]
        endereco.save()
        recepcao.endereco = endereco
        if '#' in str(arr[22]):
            recepcao.cor_casamento = arr[22]
        recepcao.save()

    def generate_noiva(self, arr):
        noiva = Noiva()
        noiva.nome = arr[7]
        noiva.sobrenome = arr[8]
        noiva.descricao = arr[9]
        noiva.facebook = arr[10]
        noiva.instagram = arr[11]
        noiva.email = arr[12]
        noiva.foto_url = self.get_image_url(arr[13])
        noiva.save()

    def generate_noivo(self, arr):
        noivo = Noivo()
        noivo.nome = arr[0]
        noivo.sobrenome = arr[1]
        noivo.descricao = arr[2]
        noivo.facebook = arr[3]
        noivo.instagram = arr[4]
        noivo.email = arr[5]
        noivo.foto_url = self.get_image_url(arr[6])
        noivo.save()

    def initialize(self):
        inicio = Pagina_Inicio()
        inicio.save()
        pn = Pagina_Noivos()
        pn.save()
        pf = Pagina_Frase()
        pf.save()
        pc = Pagina_Contador()
        pc.save()
        pr = Pagina_RSVP()
        pr.texto = ''
        pr.save()
        pm = Pagina_Mural()
        pm.save()

    def get_image_url(self, param):
        return str(param).replace('open', 'uc')

    def check_lista_presentes(self, param, item_lista, pagina):
        if 'http' in str(param):
            item_lista.nome = param
            item_lista.is_site = True
            item_lista.link_url = param
            item_lista.pagina_listapresentes = pagina
        else:
            item_lista.nome = param
            item_lista.is_site = None
            item_lista.pagina_listapresentes = pagina
        item_lista.save()
