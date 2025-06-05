from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {} de {}! This is my first view.</h1>'.format(nome, idade))

def soma(request,num1,num2):
    resultado = num1 + num2
    return HttpResponse('<h1>Resultado da soma: {} + {} = {}</h1>'.format(num1,num2,resultado))

def multiplicacao(request,num1,num2):
    resultado = num1 * num2
    return HttpResponse('<h1>Resultado da multiplicação: {} * {} = {}</h1>'.format(num1,num2,resultado))

def divisao(request,num1,num2):
    if(num2==0):
        return HttpResponse('<h1>Divisao por zero')
    else:
        resultado = num1/num2
        return HttpResponse('<h1>Resultado da divisão: {} / {} = {}</h1>'.format(num1,num2,resultado))

def subtracao(request,num1,num2):
    resultado = num1 - num2
    return HttpResponse('<h1>Resultado da subtração: {} - {} = {}</h1>'.format(num1,num2,resultado))