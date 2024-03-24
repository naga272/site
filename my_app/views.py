
from django.shortcuts                       import render, redirect
from django.http                            import HttpResponse, FileResponse, Http404, HttpResponseNotFound
from django.views                           import View

from django.core.files.storage              import FileSystemStorage


# Create your views here.
from .models                                import TracciaDB   # tabelle DB
from .forms                                 import SendRequest
from ip2geotools.databases.noncommercial    import DbIpCity                 # pip install ip2geotools -> localizzazione
from datetime                               import datetime

import platform
import time
import sys
import os


def home(request):
    log_spostamento(request, 'index.html')
    return render(request, 'index.html')


def contattami(request):
    if request.method == 'POST':
        form = SendRequest(request.POST)
        if form.is_valid():
            print("form valido (=")
            richiesta = form.save()
            return HttpResponse("<h3>Grazie per avermi contattato</h3>")
    else:
        form = SendRequest()
    
    log_spostamento(request, 'contatto.html')
    context = {"form" : form}
    return render(request, "contatto.html", context) 


def project(request):
    log_spostamento(request, 'project.html')
    return render(request, 'project.html')


def brainfuck(request):
    log_spostamento(request, 'brainfuck.html')
    return render(request, 'brainfuck.html')


def virus(request):
    log_spostamento(request, 'virus_c.html')
    return render(request, 'virus_c.html')


#certificazioni project
def certificazioni(request):
    log_spostamento(request, 'certificazioni.html')
    return render(request, 'certificazioni.html')


def pageError(request):
    log_spostamento(request, 'NotAvailable.html')
    return render(request, 'NotAvailable.html')


def compiler(request):
    log_spostamento(request, 'compiler.html')
    return render(request, 'compiler.html')


def pdf_view(request):
    fs = FileSystemStorage()
    filename = './templates/bastianello_federico_CV.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=".pdf"' #user will be prompted display the PDF in the browser
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


def log_spostamento(request:object, page_html:str):

    # creo oggetto per registrare gli accessi dell'utente
    posizione_user = DbIpCity.get(request.META.get("REMOTE_ADDR"), api_key = "free")

    utente = TracciaDB(
        ip                  = request.META.get("REMOTE_ADDR"), #  Ottiene l'indirizzo IP dell'utente
        timestamp           = str(time.time()),
        normalTime          = datetime.now(),
        name                = os.environ.get("USERNAME", "Nome utente sconosciuto"),  # Gestione se l'ambiente non ha USERNAME
        operative_system    = platform.system(),
        page_name           = page_html,
        city                = str(posizione_user.city),
        region              = str(posizione_user.region),
        country             = str(posizione_user.country),
        type_method         = str("POST" if request.method == "POST" else "GET")
    )
    utente.save() # salvo l'utente all'interno della tabella del database
