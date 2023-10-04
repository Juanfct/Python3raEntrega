from django import forms



class cursoFormulario (forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()