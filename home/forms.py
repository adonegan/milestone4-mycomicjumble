from django import forms


class ContactForm(forms.Form):
    """
    Form that visitors can use to contact site owner
    """
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    class Meta:
        fields = ['subject', 'message', 'email']
