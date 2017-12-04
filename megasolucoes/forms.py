from django import forms


class CarregaVariaveis(forms.Form):
    nIteracoes = forms.IntegerField(label='Numero de Iterações', initial=1, min_value=1)
    nVariaveis = forms.IntegerField(label="Numero de Variaveis", initial=1, min_value=1)
    nRegras = forms.IntegerField(label="Numero de Regras", initial=1, min_value=1)
    Choises = [(0, 'Maximizar'), (1, 'Minimizar')]
    optSimplex = forms.ChoiceField(
        label='Opções',
        choices=Choises,
        widget=forms.RadioSelect())
