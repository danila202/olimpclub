from django.shortcuts import render, redirect
from.forms import RegistrationForm, UserLoginForm
from django.contrib import messages, auth


def login_of_user(request):
    if request.method == 'POST':
        form_login = UserLoginForm(request.POST)

        if form_login.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user:
                auth.login(request,user)
                return redirect('new:home')

        else:
            print(form_login.error_messages)

    form_login = UserLoginForm()
    return render(request, 'html/login.html', {'form_login': form_login})


def registration_of_user(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Вы успешно зарегестрировались')
            return redirect('new:home')
        else:
            messages.error(request, "Регистрация не удалась ")
            print(user_form.error_messages)
    else:
        user_form = RegistrationForm()

    return render(request,'html/registration.html',context={'registration_form': user_form})







