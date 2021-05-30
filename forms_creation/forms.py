from django import forms

class create(forms.Form):
    name=forms.CharField(label="name",max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    roll=forms.CharField(label="roll",max_length=14,min_length=14,widget=forms.TextInput(attrs={'class': "form-control"}))
    branch=forms.CharField(label="branch",max_length=50,widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.CharField(label="email",max_length=50,widget=forms.TextInput(attrs={'class': "form-control"}))
    phone=forms.CharField(label="phone",max_length=10,widget=forms.TextInput(attrs={'class': "form-control"}))