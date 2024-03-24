"""
URL configuration for PortFolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib     import admin
from django.urls        import path
from my_app.views       import home, contattami, certificazioni, project, brainfuck, virus
from my_app.views       import pageError, compiler, pdf_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contattami/', contattami),
    path('certificazioni/', certificazioni),
    path('project/', project),
    path('brainfuck/', brainfuck),
    path('virus_c/', virus),
    path('NotAvailable/', pageError),
    path('compiler/', compiler),
    path('view-pdf/', pdf_view, name='pdf_view')
]
