from django import forms

from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class OptionForm(forms.Form):
    option_1 = forms.CharField(max_length= 200)
    explanation_1 = forms.CharField(max_length= 200)
    is_correct_1 = forms.BooleanField(required=False)
    option_2 = forms.CharField(max_length= 200)
    explanation_2 = forms.CharField(max_length= 200)
    is_correct_2 = forms.BooleanField(required=False)
    option_3 = forms.CharField(max_length= 200)
    explanation_3 = forms.CharField(max_length= 200)
    is_correct_3 = forms.BooleanField(required=False)
