from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll", "marks"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "roll": forms.NumberInput(attrs={"class": "form-control"}),
            "marks": forms.NumberInput(attrs={"class": "form-control"}),
        }
