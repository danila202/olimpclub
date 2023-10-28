from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'sport_section', 'position', 'password1', 'password2']

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))

    patronymic = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите отчество'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))

    sport_section = forms.Select(attrs={'class': 'form-control'})

    position = forms.Select(attrs={'class': 'form-control'})

    password1 = forms.CharField(widget=forms.PasswordInput())

    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password_confirmed')

        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')


class UserLoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите  email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))



