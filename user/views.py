from django.shortcuts import render, redirect
from.forms import RegistrationForm
from django.contrib import messages


def display_user_form(request):
    return render(request,'html/registration.html')


def registration_of_user(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Вы успешно зарегестрировались')
            return redirect('new:home')

        else:
            messages.error(request, "Регистрация не удалась ")

    else:
        user_form = RegistrationForm()

    return render(request,'html/registration.html',context={'registration_form': user_form})







