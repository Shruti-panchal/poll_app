from django.forms import ModelForm
from .models import poll


class CreatePollForm(ModelForm):
    class Meta:
        model = poll
        fields = ['question', 'option1', 'option2', 'option3', 'option4']
