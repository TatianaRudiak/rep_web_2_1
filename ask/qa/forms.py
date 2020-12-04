from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
            
    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(
                u'Вопрос введен не корректно', code=12
                )
        return text

    def save(self):
        return Question.objects.create(**self.cleaned_data)
    
class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
    
    def clean_question(self):
        question = self.cleaned_data['question']
        if not question:
            raise forms.ValidationError(
                u'Вопрос не выбран', code=12
                )
        return question

    def save(self):
        return Answer.objects.create(**self.cleaned_data)