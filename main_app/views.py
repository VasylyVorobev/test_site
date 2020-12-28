from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Profile, Category
from django.views.generic.list import View
from django.views.generic.detail import DetailView
from .forms import SelectionTeacherForm, BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfilesList(View):

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        profile = Profile.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            profile = Profile.objects.filter(category=category)
        context = {'category': category, 'categories': categories, 'profile': profile}

        return render(request, '[sharewood.biz] index.html', context)


class ProfilesDetail(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ProfilesDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class SelectionTeacherView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = SelectionTeacherForm()
        return render(request, 'request.html', context={'form': form})

    def post(self, request):
        form = SelectionTeacherForm(request.POST)
        sent = False
        cd_time, cd_purp = None, None
        if form.is_valid():
            cd = form.cleaned_data
            cd_time = form.TIME_CHOICE[int(cd["time"]) - 1][1]
            cd_purp = form.PURP_CHOICE[int(cd["purpose"]) - 1][1]
            subject = f'Есть запрос от {cd["name"]}, с номером {cd["number"]}'
            message = f'предпочтения: время: {cd_time}, для чего: {cd_purp}'
            send_mail(subject, message, 'kurma.kurma1801@gmail.com', ['kurma.kurma@yandex.ru'])
            sent = True
        return render(request, 'request_done.html', context={
            'form': form, 'sent': sent, 'cd_time': cd_time, 'cd_purp': cd_purp
        })


class BookingView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        profile = get_object_or_404(Profile, id=pk)
        form = BookingForm()
        return render(request, 'booking.html', {'form': form, 'profile': profile})

    def post(self, request, pk):
        form = BookingForm(request.POST)

        return render(request, 'booking_done.html', {'form': form})
