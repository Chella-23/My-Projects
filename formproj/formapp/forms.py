from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()