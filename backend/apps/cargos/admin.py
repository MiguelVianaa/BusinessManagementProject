from django.contrib import admin
from .models import Cargo

class AtivoFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'ativo'

    def lookups(self, request, model_admin):
        return [
            ('ativos', 'Ativos'),
            ('deletados', 'Removidos (soft delete)')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'ativos':
            return queryset.filter(deleted_at__isnull=True)
        if self.value() == 'deletados':
            return queryset.filter(deleted_at__isnull=False)
        return queryset

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    # Exibe os campos na ordem desejada na listagem
    list_display = ('id', 'nome', 'descricao', 'created_at', 'updated_at', 'deleted_at')

    # Ordernação da listagem
    orders = ('nome',)

    # Campos para pesquisa rápida
    search_fields = ('nome', 'descricao')

    # Filtros laterais
    list_filter = ('nome',)

    # Ordem dos campos ao editar no formulário admin
    fields = ('nome', 'descricao')

    # Campos somente leitura que não podem ser editados no formulário admin
    readonly_fields = ('created_at', 'updated_at')

    # Define quais campos serão links clicáveis para edição na listagem
    list_display_links = ('nome',)

    actions = ['restaurar']

    @admin.action(description='Restaurar selecionados')
    def restaurar(self, request, queryset):
        queryset.update(deleted_at=None)
