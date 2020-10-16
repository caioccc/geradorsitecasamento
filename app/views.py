# -*- coding: UTF-8 -*-

from django.http import JsonResponse, Http404
# Create your views here.
from django.views.generic import TemplateView

from app.models import Rsvp, Recado, Pagina_Inicio, Pagina_Noivos, Pagina_Frase, Pagina_Timeline, Pagina_Contador, \
    Pagina_Galeria, Pagina_Padrinhos, Pagina_RSVP, Pagina_ListaPresentes, Pagina_Mural, Pagina_Footer, Noivo, Noiva, \
    Recepcao, CategoriaGaleria


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
