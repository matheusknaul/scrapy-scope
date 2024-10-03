import test_configuration
from segregate_text import __search__
from format_list import organizar_indices
from build_table import __build__
from build_text_scope import __build_text__
from configuration import produtos_1, produtos_2, classes_1, area_atividade_1, area_atividade_2

texto = __build_text__('app/escopo.pdf')
lista = __search__(texto, produtos_2)
print('etapa do search', lista)
lista_new = organizar_indices(lista)
print('etapa do do organizar indices', lista_new)
lista_segregada = __build__(lista_new)
print('etapa do segregar elementos',lista_segregada)

