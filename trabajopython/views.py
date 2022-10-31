from django.shortcuts import render
from django.http import HttpResponse
from sys import getsizeof
import re
import numpy as np
import cgi, os
edades = []

with open("Direcciones.txt",'r') as file:
        for line in file:
            grade_data = line.strip().split(',')
            newString = line.replace("'[","")     
            edades.append(newString) 
            

def home(request):
    return render(request,'home.html')

def crearArchivo(request):
    archivo = open("Prueba.txt","a")
    direccionValue = request.POST['direccion']
    cadena_tres = direccionValue.replace(" ","")
    print (cadena_tres)
    archivo.write(cadena_tres + '\n')    
    archivo.close()
    return render(request,'home.html', {
        
        'direccionValue':direccionValue,
        
 })

def leerArchivo(request):

    
    email = re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',request.POST['email'])
    emailValue = request.POST['email']

    nombre = re.search('^([a-zA-ZÀ-ÿ\u00f1\u00d1]{2,50}\s?){1,3}$',request.POST['nombre'])
    nombreValue = request.POST['nombre']

    apellido = re.search('^([a-zA-ZÀ-ÿ\u00f1\u00d1]{2,50}\s?){1,3}$',request.POST['apellidos'])
    apellidoValue = request.POST['apellidos']

    fechaNacimiento = re.search('^([12]\d{3})\/(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])$',request.POST['fechaNacimiento'])
    fechaNacimientoValue = request.POST['fechaNacimiento']

    celular = re.search('^[3]\d{9}$',request.POST['celular'])
    celularValue = request.POST['celular']

    fijo = re.search('^[0-9]{7}$',request.POST['telefonoFijo'])
    fijoValue = request.POST['telefonoFijo']

    direccion = re.search('(^[a-zA-Z]+\s\d+\s#\s?[0-9]+\-[0-9]+$)|(^[a-zA-Z]+[0-9]#[0-9]\-[0-9]\s?[a-zA-Z]\s?[a-zA-Z]*$)|(^[a-zA-Z 0-9]+$)',request.POST['direccion'])
    direccionValue = request.POST['direccion']

    for m in edades:
        if direccionValue in m:
           print(m)
           
    regexZip = re.compile(r'[0-9]{6}|([0-9]{5}\s?\-\s?[0-9]{5})')
    zip = regexZip.fullmatch(request.POST['zip'])
    zipValue = request.POST['zip']



    return render(request,'home.html', {
        'email': bool(email),
        'nombre': bool(nombre),
        'apellido': bool(apellido),
        'fechaNacimiento': bool(fechaNacimiento),
        'celular': bool(celular),
        'fijo': bool(fijo),
        'direccion': bool(direccion),
        'zip': bool(zip),
        'emailValue': emailValue,
        'nombreValue':nombreValue,
        'apellidoValue':apellidoValue,
        'fechaNacimientoValue':fechaNacimientoValue,
        'celularValue':celularValue,
        'fijoValue':fijoValue,
        'direccionValue':direccionValue,
        'm':m,
        'zipValue':zipValue,
    })

