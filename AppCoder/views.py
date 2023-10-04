from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import cursoFormulario




def inicio(request):
   
    return render (request, "Appcoder/inicio.html")


def curso (request): 

    cur1 = Curso(nombre="Python", camada= 2176)
    cur1.save()

    return render(request, "AppCoder/cursos.html")

    return HttpResponse (f"El curso que he creado es: {cur1.nombre}")
    pass

def estudiante(request):

    return render(request, "AppCoder/estudiante.html")


def profesores(request):

    return render(request, "AppCoder/profesores.html")

def entregables(request):

    return render(request, "AppCoder/entregables.html")







def cursoFormulario(request):
 
    if request.method == "POST":

        formulario1 = cursoFormulario(request.POST)

        if formulario1.is_valid():
            
            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info ["camada"])

            curso.save() 

            return render(request, "Appcoder/inicio.html")
    
        else:
            formulario1 = cursoFormulario()

    return render (request, "AppCoder/cursoFormulario.html", {"form1":formulario1})

def busquedaCamada(request):
    
    return render(request, "Appcoder/inicio.html")

def resultados(request):

    if request.GET ["camada"]: 



        camada=request.GET["camada"]
        cursos=Curso.objects.filter(camada__iexact=camada)



        return render (request, "Appcoder/inicio.html", {"cursos":cursos, "camada":camada})
    
    else:
        respuesta = "No enviaste datos." 

    return HttpResponse(respuesta)
    



def buscar_profes (request):
    
    return render (request, "Appcoder/buscar_profes.html")

def resultado_profes (request):

    return HttpResponse(f"Estoy buscando el profesor de apellido: {request.GET['apellido']}")



