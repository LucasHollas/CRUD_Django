from django.db.models import fields
from django.forms import ModelForm
from app.models import cargos


class CargosForm(ModelForm):
    class Meta:
        model = cargos
        fields = ["cargo"]
