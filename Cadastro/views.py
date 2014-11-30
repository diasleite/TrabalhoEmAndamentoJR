# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from models import *
from Cadastro.forms import ContatoForm

def homepage(request):


       return render_to_response('homepage.html', locals())

def excluir_contato(request, contato_id=None):
    if contato_id:
        contato.objects.get(pk=contato_id).delete()

    return redirect('/contatos')


def edita_contato(request, contato_id=None):
        if contato_id:
            v_contato = contato.objects.get(pk=contato_id)
        else:
            v_contato = None

        if request.method == 'POST' :
            form =  ContatoForm(request.POST, instance = v_contato)

            if form.is_valid():
                resultado = form.save()
                if resultado:
                    return redirect('/contatos')
        else:
            form = ContatoForm(instance=v_contato)

        return render(request,'CadastroContatoNovo.html', locals())


def Contatos(request):
    v_contatos = contato.objects.all()

    return  render_to_response('MostrarContatos.html', locals())