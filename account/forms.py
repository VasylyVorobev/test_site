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
