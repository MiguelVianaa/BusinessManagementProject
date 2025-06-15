from django.contrib import admin
from .models import Colaborador

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

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    # Exibe os campos na ordem desejada na listagem
    list_display = ('id', 'nome', 'telefone', 'empresa', 'setor', 'cargo' , 'created_at', 'updated_at', 'deleted_at')

    # Campos para pesquisa rápida
    search_fields = ('nome', 'telefone', 'empresa__nome')

    # Filtros laterais
    list_filter = ('setor', 'empresa', 'cargo', 'genero', 'deleted_at')

    # Ordem dos campos ao editar no formulário admin
    fields = ('nome', 'idade', 'genero', 'telefone', 'email', 'setor', 'empresa', 'cargo')

    # Campos somente leitura que não podem ser editados no formulário admin
    readonly_fields = ('created_at', 'updated_at')

    # Define quais campos serão links clicáveis para edição na listagem
    list_display_links = ('nome',)

    # Ações personalizadas na tela de cadastro e edição
    actions = ['restaurar']

    list_filter = (AtivoFilter,)

    @admin.action(description='Restaurar selecionados')
    def restaurar(self, request, queryset):
        queryset.update(deleted_at=None)