from django import forms

from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        widgets = {
            'texx': forms.HiddenInput(),
        }
        fields = ('YourName','Phone','location', 'description', 'document', 'texx')
