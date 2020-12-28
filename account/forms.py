from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("")
        user = User.objects.filter(username=username).first()
        # user = User.objects.get(username=username)
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("")

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input-group'}), required=False)

    def clean_email(self):

        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain not in ['com', 'ru', 'edu', 'su']:
            raise forms.ValidationError(f'Указан неверный домен: {domain}')
        if User.objects.filter(email=email).exists():
            forms.ValidationError(f'Пользователь с почтой {email} уже существует')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с ником {username} уже существует')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if len(password) < 8:
            raise forms.ValidationError('Пароль должен содержать не менее 8 символов')

        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = [
            'username', 'password', 'confirm_password', 'first_name', 'last_name', 'phone', 'email', 'profile_pic'
        ]

