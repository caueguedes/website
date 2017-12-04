from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from megasolucoes.forms import CarregaVariaveis
from django.core.urlresolvers import reverse

# # Create your views here.
# def home(request):
#     form = CarregaVariaveis()
#     return render(request, 'megasolucoes/home.html', form)


def home(request):
    form = CarregaVariaveis(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return redirect(request, 'megasolucoes/info.html', {'form': form})
    else:
        form = CarregaVariaveis()

    return render(request, 'megasolucoes/home.html', {'form': form})


def info(request):
    form = CarregaVariaveis(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        context = {'base': 0}
        z, linhas = {}, {}

        aux = form.cleaned_data['nVariaveis']
        for var in enumerate(range(aux), start=1):
            string = 'var' + str(var[0])
            context[string] = 0
            z[string] = 0

        aux = form.cleaned_data['nRegras']

        for var in enumerate(range(aux), start=1):
            string = 'Regra' + str(var[0])
            context[string] = 0

        context['sinal'] = '=>'
        context['b'] = 0

        for linha in enumerate(range(aux), start=1):
            string = 'Linha' + str(linha[0])
            linhas[string] = dict(context)
            linhas[string]['base'] = 'Regra' + str(linha[0])

        nIteracoes = form.cleaned_data['nIteracoes']

        print(not(bool(form.cleaned_data["optSimplex"])))

        opcao = bool (form.cleaned_data['optSimplex'])

        return render(request, 'megasolucoes/info.html', {
            'context': context,
            'opcao': opcao,
            'nIteracoes': nIteracoes,
            'z': z,
            'linhas': linhas,
            }
        )

    return redirect('megasolucoes:home')


def show(request):
    # form = request.POST
    # if request.method == 'POST':
    #     if form.is_valid():
    #         print(form.cleaned_data.as_p())
    #         return render(request, 'megasolucoes/show.html', {'form': form})

    # return redirect('megasolucoes:home')
    return render(request, 'megasolucoes/show.html')
