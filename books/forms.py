from django import forms

from books.models import Author


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean_sender(self):
        sender = self.cleaned_data.get("sender")
        
        if sender.split('@')[1] != "mugna.tech":
            raise forms.ValidationError("Sender should only be from a Mugna Organization.")
        
        return sender
    
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

