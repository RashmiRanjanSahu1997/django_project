from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    """
    Displays the registration/signup page and handles the sign up action.
    """
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login, authenticate
    from .forms import SignUpForm

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('account:login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})
