from .models import Projects
from django.forms import ModelForm, TextInput, Textarea


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите описание"
             })}
