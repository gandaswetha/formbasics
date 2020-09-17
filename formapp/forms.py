from django import forms

class formname(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    comments=forms.CharField(widget=forms.Textarea)
    phnno=forms.CharField()
