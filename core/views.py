from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')


def info(request):
    context = {
        'curso': 'Programação web com Django FrameWork'
    }
    return render(request, 'info.html', context)


def dados(request, nome, idade):
    return HttpResponse('<h3>Dados ...</h3>'
                        '<h3> informação enviada pela URL <br>Nome: {}<br>Idade: {}</h3><br>'
                        '<a href="/">index</a>'.format(nome,idade))


def dados2(request, nome, idade):
    context = {
        'nome': nome,
        'idade' : idade,
    }
    return render(request, 'dados2.html', context)