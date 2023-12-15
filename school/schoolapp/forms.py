from django import forms
from schoolapp.models import Student

class studentinputform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'