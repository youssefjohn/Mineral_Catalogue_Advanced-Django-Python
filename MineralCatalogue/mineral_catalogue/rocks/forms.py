from django import forms




class Search_Form(forms.Form):
    name = forms.CharField(max_length=100)


