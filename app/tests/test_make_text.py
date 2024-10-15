import test_configuration
from build_row import __make_text__

text = "Teste ae flask 1ndteste pain aaaa pain aaaaaaaa pain pain pain AAAAAAAAAA cbol teste teste"
[['flask', ' 1nd'], ['1nd', 'teste pain'], ['pain', ' aaaa pain'], ['pain', ' aaaaaaaa pain'], ['pain', ' pain'], ['pain', ' pain'], ['pain', ' AAAAAAAAAA cbol'], ['cbol', ' teste test']]

lista = [['flask', [14, 18]], ['1nd', [18, 28]], ['pain', [28, 38]], ['pain', [38, 52]], ['pain', [52, 57]], ['pain', [57, 62]], ['pain', [62, 78]], ['cbol', [78, -1]]]

print(__make_text__(text, lista))