from django import forms

from books.models import Author, Book, Publisher, Classification


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean_sender(self):
        sender = self.cleaned_data.get("sender")

        if sender.split("@")[1] != "mugna.tech":
            raise forms.ValidationError(
                "Sender should only be from a Mugna Organization."
            )

        return sender


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        exclude = ["user"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "email"]


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "authors", "publisher", "classification"]


class PublisherUpdateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [
            "name",
            "address",
            "city",
            "state_province",
            "country",
            "website",
        ]


class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        exclude = ["user"]


class BookDeleteForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "authors", "publisher", "classification"]


class PublisherDeleteForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [
            "name",
            "city",
            "country",
            "website",
        ]
