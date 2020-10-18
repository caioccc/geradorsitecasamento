# -*- coding: UTF-8 -*-

from django.http import JsonResponse, Http404
# Create your views here.
from django.views.generic import TemplateView, FormView

from app.forms import FormUploadFile
from app.models import Rsvp, Recado, Pagina_Inicio, Pagina_Noivos, Pagina_Frase, Pagina_Timeline, Pagina_Contador, \
    Pagina_Galeria, Pagina_Padrinhos, Pagina_RSVP, Pagina_ListaPresentes, Pagina_Mural, Pagina_Footer, Noivo, Noiva, \
    Recepcao, CategoriaGaleria, ItemPadrinho, ItemGaleria, ItemListaPresentes, ItemTimeline, Endereco
import pandas as pd
import datetime


class UploadView(FormView):
    template_name = 'upload.html'
    success_url = '/'
    form_class = FormUploadFile

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
            if 'nan' not in str(arr[i]) or not len(str(arr[i])) == 3:
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
        if 'nan' not in str(arr[23]) or not len(str(arr[23])) == 3:
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

    def handle_csv(self, csv_file):
        df = pd.read_csv(csv_file)
        arr = df.values[0][1:]
        self.initialize()
        self.generate_noivo(arr)
        self.generate_noiva(arr)
        self.generate_recepcao(arr)
        self.generate_footer(arr)
        self.generate_timeline(arr)
        self.generate_lista_presentes(arr)
        self.generate_galeria(arr)
        self.generate_padrinhos(arr)

    def form_valid(self, form):
        csv_file = self.request.FILES['file']
        self.handle_csv(csv_file)
        return super(UploadView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(UploadView, self).form_invalid(form)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['recados'] = Recado.objects.filter(aprovado=True)
        pi = Pagina_Inicio.objects.first()
        pn = Pagina_Noivos.objects.first()
        pf = Pagina_Frase.objects.first()
        pt = Pagina_Timeline.objects.first()
        pc = Pagina_Contador.objects.first()
        pg = Pagina_Galeria.objects.first()
        pp = Pagina_Padrinhos.objects.first()
        pr = Pagina_RSVP.objects.first()
        pl = Pagina_ListaPresentes.objects.first()
        pm = Pagina_Mural.objects.first()
        pfo = Pagina_Footer.objects.first()
        context['inicio'] = pi
        context['noivos'] = pn
        context['frase'] = pf
        context['timeline'] = pt
        context['contador'] = pc
        context['galeria'] = pg
        context['padrinhos'] = pp
        context['rsvp_page'] = pr
        context['presentes'] = pl
        context['mural'] = pm
        context['footer'] = pfo
        context['noivo'] = Noivo.objects.first()
        context['noiva'] = Noiva.objects.first()
        context['recepcao'] = Recepcao.objects.first()
        context['categorias_galeria'] = CategoriaGaleria.objects.all()
        return self.render_to_response(context)


def submit_rsvp(request):
    data = request.POST
    name = data.get('name')
    if 'cerimonia' in data:
        cerimonia = True
    else:
        cerimonia = False
    if 'recepcao' in data:
        recepcao = True
    else:
        recepcao = False
    message = data.get('message')
    email = data.get('email')
    try:
        objeto = Rsvp(nome=name, email=email, cerimonia=cerimonia, recepcao=recepcao, mensagem=message)
        objeto.save()
        # messages.success(request, u'Confirmação realizada com sucesso!')
        return JsonResponse({'message': u'Confirmação realizada com sucesso!'})
    except:
        # messages.error(request, u'Houve algum erro no formulário.')
        raise Http404


def submit_recado(request):
    data = request.POST
    name = data.get('name')
    texto = data.get('message')
    # foto = data.get('photo')
    try:
        objeto = Recado(nome=name, texto=texto)
        objeto.save()
        # messages.success(request, u'Confirmação realizada com sucesso!')
        return JsonResponse({'message': u'Seu recado passará por aprovação dos noivos! Obrigado.'})
    except:
        # messages.error(request, u'Houve algum erro no formulário.')
        raise Http404
