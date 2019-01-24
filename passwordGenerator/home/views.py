from django.core.serializers import json
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.PasswordGenerator import PasswordGenerator
from home.forms import HomeForm, CreatePinForm, PasswordCreationForm
from home.models import Post, Password

def home(request):
    template_name = 'home/create_new_password.html'
    vehicle1 = request.GET.get('vehicle1', None)
    vehicle2 = request.GET.get('vehicle2', None)
    vehicle3 = request.GET.get('vehicle3', None)
    vehicle4 = request.GET.get('vehicle4', None)
    Length = request.GET.get('Length', None)
    new_pin = ""


    if not Length:
        Length = "8"
        if not vehicle1 and not vehicle2 and not vehicle3 and not vehicle4:
            new_pin = ''
        else:
            new_pin = PasswordGenerator(int(Length), vehicle1, vehicle2, vehicle3, vehicle4)
    else:
        if not vehicle1 and not vehicle2 and not vehicle3 and not vehicle4:
            new_pin = ''
        else:
            new_pin = PasswordGenerator(int(Length), vehicle1, vehicle2, vehicle3, vehicle4)


    form = CreatePinForm(initial={'passwordGenerator': new_pin})
    args = {'passwordGenerator': new_pin, 'form': form}

    # data = {
    #     #     'new_pin': new_pin
    #     # }
    #return JsonResponse(data)

    if request.method == 'POST':
        form = CreatePinForm(request.POST)
        if form.is_valid():
            password = form.save(commit=False)
            password.user = request.user
            password.save()

            text = form.cleaned_data['website']
            form = CreatePinForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, template_name, args)

    return render(request, 'home/create_new_password.html', args)


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        passwords = Password.objects.all()
        args = {
            'form': form, 'passwords': passwords
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

class CreatePassword(TemplateView):

    template_name = 'home/create_new_password.html'

    def get(self, request):
        form = CreatePinForm()
        passwords = Password.objects.all()

        args = {'form': form, 'password': passwords}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CreatePinForm(request.POST)
        if form.is_valid():
            password = form.save(commit=False)
            password.user = request.user
            password.save()

            text = form.cleaned_data['website']
            form = CreatePinForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
