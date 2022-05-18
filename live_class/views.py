from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def hello_world(request):
    return HttpResponse("Hello, world. You're at the Django - CoderHouse first view.")
def segunda_vista_(request):
    return HttpResponse("<br><br><br> Ya entendimos esto, es muy simple ")
def DiaDeHoy(request):

        dia = datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"

        return HttpResponse(documentoDeTexto)
def miNombreEs(self, name, age):
    age = int(age)
    documentoDeTexto = f"Mi nombre es: <br><br>  {name} <br><br> Mi edad es: {age}"

    return HttpResponse(documentoDeTexto)
def calculate_birth_year(self, age):
    current_year = datetime.now().year
    birth_year = current_year - int(age)
    return HttpResponse (f"<br><br> My birth year is: {birth_year}")
def ProbandoTemplate(self):

    miHtml = open("C:/Users/rafif/Desktop/CODER/live_class/live_class/templates/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)
