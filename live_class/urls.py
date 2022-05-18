"""live_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.http import HttpResponse

from django.contrib import admin
from django.urls import path
from live_class.views import (hello_world,
segunda_vista_,
DiaDeHoy,
miNombreEs,
calculate_birth_year,
ProbandoTemplate,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('segundavista/', segunda_vista_),
    path('diaDeHoy/',DiaDeHoy),
    path('miNombreEs/<name>/<age>',miNombreEs),
    path('calculate_birth_year/<age>',calculate_birth_year),
    path('ProbandoTemplate/', ProbandoTemplate)

]