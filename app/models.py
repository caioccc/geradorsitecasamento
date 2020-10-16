#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from base64 import b64encode

import pyimgur


# Create your models here.

class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Rsvp(TimeStamped):
    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVP's"

    cerimonia = models.BooleanField()
    recepcao = models.BooleanField()
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    mensagem = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.nome)


class Recado(TimeStamped):
    class Meta:
        verbose_name = "Recado"
        verbose_name_plural = "Recados"

    nome = models.CharField(max_length=300)
    foto = models.URLField(blank=True, null=True, default='https://placehold.it/300x300')
    texto = models.TextField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return u'%s' % (self.nome)

    def __unicode__(self):
        return u'%s' % (self.nome)


class Noivo(TimeStamped):
    class Meta:
        verbose_name = "Noivo"
        verbose_name_plural = "Noivo"

    nome = models.CharField(max_length=255, blank=True, null=True)
    sobrenome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/300x300')
    file = models.FileField(blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        return super(Noivo, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.nome

    def __unicode__(self):
        return '%s' % self.nome


class Noiva(TimeStamped):
    class Meta:
        verbose_name = "Noiva"
        verbose_name_plural = "Noiva"

    nome = models.CharField(max_length=255, blank=True, null=True)
    sobrenome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/300x300')
    file = models.FileField(blank=True, null=True, verbose_name='Arquivo de Foto')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        return super(Noiva, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.nome

    def __unicode__(self):
        return '%s' % self.nome


class Endereco(TimeStamped):
    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"

    rua = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    ponto_referencia = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ponto de Referencia')

    def __str__(self):
        return '%s, %s, %s - %s, %s' % (self.rua, self.numero, self.bairro, self.cidade, self.estado)

    def __unicode__(self):
        return '%s, %s, %s - %s, %s' % (self.rua, self.numero, self.bairro, self.cidade, self.estado)


class Recepcao(TimeStamped):
    class Meta:
        verbose_name = "Recepcao"
        verbose_name_plural = "Recepcao"

    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, blank=True, null=True, on_delete=models.CASCADE)
    cor_casamento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.local)

    def __unicode__(self):
        return '%s' % (self.local)


class Pagina_Inicio(TimeStamped):
    class Meta:
        verbose_name = "Pagina de Inicio"
        verbose_name_plural = "Pagina de Inicio"

    frase = models.TextField(blank=True, null=True, default='Vamos nos casar!')
    foto_background_url = models.URLField(blank=True, null=True, default='https://i.imgur.com/jWXZF4z.jpg')
    file = models.FileField(blank=True, null=True, verbose_name='Foto Background')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_background_url = file
        except (Exception,):
            pass
        return super(Pagina_Inicio, self).save(*args, **kwargs)


class Habilitavel(models.Model):
    class Meta:
        abstract = True

    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Pagina_Noivos(Habilitavel):
    class Meta:
        verbose_name = "Pagina dos Noivos"
        verbose_name_plural = "Pagina dos Noivos"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='Os Noivos')


class Pagina_Frase(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Frase Principal"
        verbose_name_plural = "Pagina de Frase Principal"

    frase = models.TextField(blank=True, null=True,
                             default=u'Será uma honra ter você no momento mais incrível das nossas vidas, onde finalmente nos tornaremos um.')
    foto_background_url = models.URLField(blank=True, null=True, default='https://imgur.com/QnAo2qj.jpg')
    file = models.FileField(blank=True, null=True, verbose_name='Foto Background')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_background_url = file
        except (Exception,):
            pass
        return super(Pagina_Frase, self).save(*args, **kwargs)


class Pagina_Timeline(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Timeline"
        verbose_name_plural = "Pagina de Timeline"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='Nossa História')
    texto_historia = models.TextField(blank=True, null=True)


class ItemTimeline(TimeStamped):
    class Meta:
        verbose_name = "Item Timeline"
        verbose_name_plural = "Itens da Timeline"

    data = models.DateField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    timeline = models.ForeignKey(Pagina_Timeline, blank=True, null=True, on_delete=models.CASCADE)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/640x480')
    file = models.FileField(blank=True, null=True, verbose_name='Foto')

    def save(self, *args, **kwargs):
        self.timeline = Pagina_Timeline.objects.first()
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        return super(ItemTimeline, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.titulo)

    def __unicode__(self):
        return '%s' % (self.titulo)


class Pagina_Contador(Habilitavel):
    class Meta:
        verbose_name = "Contador"
        verbose_name_plural = "Contador"

    foto_background_url = models.URLField(blank=True, null=True, default='https://imgur.com/WvzW9gn.jpg')
    file = models.FileField(blank=True, null=True, verbose_name='Foto Background')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_background_url = file
        except (Exception,):
            pass
        return super(Pagina_Contador, self).save(*args, **kwargs)


class CategoriaGaleria(TimeStamped):
    class Meta:
        verbose_name = "Categoria de Galeria"
        verbose_name_plural = "Categorias de Galeria"

    titulo = models.CharField(max_length=255, blank=True, null=True, default=u'Família')

    def __str__(self):
        return '%s' % (self.titulo)

    def __unicode__(self):
        return '%s' % (self.titulo)


class Pagina_Galeria(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Galeria"
        verbose_name_plural = "Pagina de Galeria"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='Galeria de Fotos')
    texto = models.TextField(blank=True, null=True, default=u'Nada melhor do que fotos pra registrar tudo!')


class ItemGaleria(TimeStamped):
    class Meta:
        verbose_name = "Item da Galeria"
        verbose_name_plural = "Itens da Galeria"

    categoria = models.ForeignKey(CategoriaGaleria, blank=True, null=True, on_delete=models.CASCADE)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/640x480')
    file = models.FileField(blank=True, null=True, verbose_name='Foto')
    galeria = models.ForeignKey(Pagina_Galeria, blank=True, null=True, on_delete=models.CASCADE, )

    def save(self, *args, **kwargs):
        self.galeria = Pagina_Galeria.objects.first()
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        return super(ItemGaleria, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.foto_url)

    def __unicode__(self):
        return '%s' % (self.foto_url)


class Pagina_Padrinhos(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Padrinhos"
        verbose_name_plural = "Pagina de Padrinhos"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='Padrinhos')
    frase = models.TextField(blank=True, null=True)


class ItemPadrinho(TimeStamped):
    class Meta:
        verbose_name = "Item Padrinho"
        verbose_name_plural = "Padrinhos"

    nome = models.CharField(max_length=255, blank=True, null=True)
    pagina_padrinhos = models.ForeignKey(Pagina_Padrinhos, blank=True, null=True, on_delete=models.CASCADE)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/640x480')
    file = models.FileField(blank=True, null=True, verbose_name='Foto')

    def save(self, *args, **kwargs):
        self.pagina_padrinhos = Pagina_Padrinhos.objects.first()
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        return super(ItemPadrinho, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.nome)

    def __unicode__(self):
        return '%s' % (self.nome)


class Pagina_RSVP(Habilitavel):
    class Meta:
        verbose_name = "Pagina de RSVP"
        verbose_name_plural = "Pagina de RSVP"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='RSVP')
    texto = models.TextField(blank=True, null=True)


class Pagina_ListaPresentes(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Lista de Presentes"
        verbose_name_plural = "Pagina de Lista de Presentes"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='Lista de Presentes')
    texto = models.TextField(blank=True, null=True,
                             default=u'Abaixo, estão as listas que fizemos online. Qualquer dúvida, só entrar em contato com a gente!')
    foto_background_url = models.URLField(blank=True, null=True, default='https://imgur.com/UWpXoS1.jpg')
    file = models.FileField(blank=True, null=True, verbose_name='Foto Background')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_background_url = file
        except (Exception,):
            pass
        return super(Pagina_ListaPresentes, self).save(*args, **kwargs)


class ItemListaPresentes(TimeStamped):
    class Meta:
        verbose_name = "Item de Lista de Presentes"
        verbose_name_plural = "Itens de Lista de Presentes"

    nome = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    is_site = models.BooleanField(blank=True, null=True, default=True)
    iframe = models.TextField(blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/640x480')
    file = models.FileField(blank=True, null=True, verbose_name='Foto')
    pagina_listapresentes = models.ForeignKey(Pagina_ListaPresentes, blank=True, null=True,
                                              on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.pagina_listapresentes = Pagina_ListaPresentes.objects.first()
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        return super(ItemListaPresentes, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.nome)

    def __unicode__(self):
        return '%s' % (self.nome)


class Pagina_Mural(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Mural"
        verbose_name_plural = "Pagina de Mural"

    titulo_menu = models.CharField(max_length=255, blank=True, null=True, default='Mural')
    texto = models.TextField(blank=True, null=True,
                             default=u'Por favor, não saia deste site sem deixar um recado para nós. Sua mensagem é muito importante, e gostaríamos de recebê-la. Nós receberemos e publicaremos as melhores em nossa página.')


class Pagina_Footer(Habilitavel):
    class Meta:
        verbose_name = "Pagina de Footer"
        verbose_name_plural = "Pagina de Footer"

    frase = models.TextField(blank=True, null=True)
    foto_background_url = models.URLField(blank=True, null=True, default='https://imgur.com/nMHYQd9.jpg')
    file = models.FileField(blank=True, null=True, verbose_name='Foto Background')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.file.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_background_url = file
        except (Exception,):
            pass
        return super(Pagina_Footer, self).save(*args, **kwargs)
