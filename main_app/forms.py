from django import forms
from django.shortcuts import get_object_or_404

from .models import Profile


class SelectionTeacherForm(forms.Form):
    PURP_CHOICE = [
        (1, 'Для переезда'),
        (2, 'Для школы'),
        (3, 'Для работы'),
        (4, 'Для переезда'),
    ]

    TIME_CHOICE = [
        (1, '1-2 часа в неделю'),
        (2, '3-5 часов в неделю'),
        (3, '5-7 часов в неделю'),
        (4, '7-10 часов в неделю'),
    ]
    purpose = forms.ChoiceField(
        label='Какая цель занятий?',
        choices=PURP_CHOICE,
        widget=forms.RadioSelect,
    )
    time = forms.ChoiceField(label='Сколько времени есть?', choices=TIME_CHOICE, widget=forms.RadioSelect,)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, label='Вас зовут')
    number = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Ваш телефон')


class BookingForm(forms.ModelForm):
    client_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, label='Вас зовут')
    number = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Ваш телефон')

    class Meta:
        model = Profile
        fields = ('img', 'name', 'free_time')
