from django import forms


class ChatForm(forms.Form):
    attrs = {
        'rows': 4, 'cols': 50,
        'placeholder': 'Введите сообщение...',
        'name': 'message', 'id': 'message-text',
        'class': 'text-holder',
    }
    message = forms.CharField(widget=forms.Textarea(attrs=attrs))
