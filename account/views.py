from django.shortcuts import render
from django.views.generic.base import View

from .forms import LoginForm


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'account/login.html', context)

