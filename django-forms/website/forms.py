from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
CHOICES = [('1', 'First'), ('2', 'Second')]

class CrearAlumnoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del alumno', max_length=100,
                             widget=forms.TextInput(attrs={'class': 'special'}))
    password = forms.CharField(widget=forms.PasswordInput())
    activo = forms.BooleanField()
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

from .models import *
class AlumnoModelForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre"]
