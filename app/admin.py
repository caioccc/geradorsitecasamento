#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

from app.models import ItemTimeline, ItemGaleria, ItemPadrinho, ItemListaPresentes


class ItemTimelineInline(admin.TabularInline):
    model = ItemTimeline


class ItemGaleriaInline(admin.TabularInline):
    model = ItemGaleria


class ItemPadrinhoInline(admin.TabularInline):
    model = ItemPadrinho


class ItemListaPresentesInline(admin.TabularInline):
    model = ItemListaPresentes


def approve_selected(modeladmin, request, queryset):
    queryset.update(is_approved=True)


def desapprove_selected(modeladmin, request, queryset):
    queryset.update(is_approved=False)


approve_selected.short_description = "Aprovar itens selecionados"
desapprove_selected.short_description = "Desaprovar itens selecionados"


class PaginaTimelineAdmin(admin.ModelAdmin):
    inlines = [ItemTimelineInline, ]

    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.name in ['estado', 'cidade', 'status',
                                                                                         'tipo_pagamento',
                                                                                         'forma_pagamento',
                                                                                         'active',
                                                                                         'cupom',
                                                                                         'enviado', 'is_online',
                                                                                         'valor_a_combinar'
                                                                                         'is_approved', 'categoria',
                                                                                         'disponivel', ]]
        self.search_fields = [field.name for field in model._meta.fields if
                              field.name in ['cpf', 'cnpj', 'nome', 'username', 'email',
                                             'name', 'phone', 'titulo', 'descricao', 'telefone', 'telefone_1', ]]
        if len([field.name for field in model._meta.fields if field.name in ['is_approved', ]]) > 0:
            self.actions = [approve_selected, desapprove_selected]
        super(PaginaTimelineAdmin, self).__init__(model, admin_site)

class PaginaGaleriaAdmin(admin.ModelAdmin):
    inlines = [ItemGaleriaInline, ]

    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.name in ['estado', 'cidade', 'status',
                                                                                         'tipo_pagamento',
                                                                                         'forma_pagamento',
                                                                                         'active',
                                                                                         'cupom',
                                                                                         'enviado', 'is_online',
                                                                                         'valor_a_combinar'
                                                                                         'is_approved', 'categoria',
                                                                                         'disponivel', ]]
        self.search_fields = [field.name for field in model._meta.fields if
                              field.name in ['cpf', 'cnpj', 'nome', 'username', 'email',
                                             'name', 'phone', 'titulo', 'descricao', 'telefone', 'telefone_1', ]]
        if len([field.name for field in model._meta.fields if field.name in ['is_approved', ]]) > 0:
            self.actions = [approve_selected, desapprove_selected]
        super(PaginaGaleriaAdmin, self).__init__(model, admin_site)

class PaginaPadrinhoAdmin(admin.ModelAdmin):
    inlines = [ItemPadrinhoInline, ]

    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.name in ['estado', 'cidade', 'status',
                                                                                         'tipo_pagamento',
                                                                                         'forma_pagamento',
                                                                                         'active',
                                                                                         'cupom',
                                                                                         'enviado', 'is_online',
                                                                                         'valor_a_combinar'
                                                                                         'is_approved', 'categoria',
                                                                                         'disponivel', ]]
        self.search_fields = [field.name for field in model._meta.fields if
                              field.name in ['cpf', 'cnpj', 'nome', 'username', 'email',
                                             'name', 'phone', 'titulo', 'descricao', 'telefone', 'telefone_1', ]]
        if len([field.name for field in model._meta.fields if field.name in ['is_approved', ]]) > 0:
            self.actions = [approve_selected, desapprove_selected]
        super(PaginaPadrinhoAdmin, self).__init__(model, admin_site)

class PaginaListaPresentesAdmin(admin.ModelAdmin):
    inlines = [ItemListaPresentesInline, ]

    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.name in ['estado', 'cidade', 'status',
                                                                                         'tipo_pagamento',
                                                                                         'forma_pagamento',
                                                                                         'active',
                                                                                         'cupom',
                                                                                         'enviado', 'is_online',
                                                                                         'valor_a_combinar'
                                                                                         'is_approved', 'categoria',
                                                                                         'disponivel', ]]
        self.search_fields = [field.name for field in model._meta.fields if
                              field.name in ['cpf', 'cnpj', 'nome', 'username', 'email',
                                             'name', 'phone', 'titulo', 'descricao', 'telefone', 'telefone_1', ]]
        if len([field.name for field in model._meta.fields if field.name in ['is_approved', ]]) > 0:
            self.actions = [approve_selected, desapprove_selected]
        super(PaginaListaPresentesAdmin, self).__init__(model, admin_site)

class CategoriaGaleriaAdmin(admin.ModelAdmin):
    inlines = [ItemGaleriaInline, ]

    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.name in ['estado', 'cidade', 'status',
                                                                                         'tipo_pagamento',
                                                                                         'forma_pagamento',
                                                                                         'active',
                                                                                         'cupom',
                                                                                         'enviado', 'is_online',
                                                                                         'valor_a_combinar'
                                                                                         'is_approved', 'categoria',
                                                                                         'disponivel', ]]
        self.search_fields = [field.name for field in model._meta.fields if
                              field.name in ['cpf', 'cnpj', 'nome', 'username', 'email',
                                             'name', 'phone', 'titulo', 'descricao', 'telefone', 'telefone_1', ]]
        if len([field.name for field in model._meta.fields if field.name in ['is_approved', ]]) > 0:
            self.actions = [approve_selected, desapprove_selected]
        super(CategoriaGaleriaAdmin, self).__init__(model, admin_site)


class ListAdminMixin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.name in ['estado', 'cidade', 'status',
                                                                                         'tipo_pagamento',
                                                                                         'forma_pagamento',
                                                                                         'active',
                                                                                         'cupom',
                                                                                         'enviado', 'is_online',
                                                                                         'valor_a_combinar'
                                                                                         'is_approved', 'categoria',
                                                                                         'disponivel', ]]
        self.search_fields = [field.name for field in model._meta.fields if
                              field.name in ['cpf', 'cnpj', 'nome', 'username', 'email',
                                             'name', 'phone', 'titulo', 'descricao', 'telefone', 'telefone_1', ]]
        if len([field.name for field in model._meta.fields if field.name in ['is_approved', ]]) > 0:
            self.actions = [approve_selected, desapprove_selected]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        if model.__name__ == 'Pagina_Timeline':
            admin_class = type('PaginaTimelineAdmin', (PaginaTimelineAdmin, admin.ModelAdmin), {})
            admin.site.register(model, admin_class)
        elif model.__name__ == 'Pagina_Galeria':
            admin_class = type('PaginaGaleriaAdmin', (PaginaGaleriaAdmin, admin.ModelAdmin), {})
            admin.site.register(model, admin_class)
        elif model.__name__ == 'Pagina_Padrinhos':
            admin_class = type('PaginaPadrinhoAdmin', (PaginaPadrinhoAdmin, admin.ModelAdmin), {})
            admin.site.register(model, admin_class)
        elif model.__name__ == 'Pagina_ListaPresentes':
            admin_class = type('PaginaListaPresentesAdmin', (PaginaListaPresentesAdmin, admin.ModelAdmin), {})
            admin.site.register(model, admin_class)
        elif model.__name__ == 'CategoriaGaleria':
            admin_class = type('CategoriaGaleriaAdmin', (CategoriaGaleriaAdmin, admin.ModelAdmin), {})
            admin.site.register(model, admin_class)
        else:
            admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
