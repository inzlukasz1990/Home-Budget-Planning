from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import make_token, check_token

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def send_confirmation_email(user):
    subject = 'Please confirm your email address'
    message_template = 'accounts/email/activation_email.txt'
    from_email = 'budzet@fuszara.pl'

    # Generate a token for the user
    token = make_token(user)
    uid = user.pk

    # Render the email message
    message = render_to_string(message_template, {
        'user': user,
        'domain': 'budzet.fuszara.pl',  # Replace with your domain
        'uid': uid,
        'token': token,
    })

    # Send the email
    send_mail(subject, message, from_email, [user.email], fail_silently=False)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate the user until the email is confirmed
            user.save()
            send_confirmation_email(user)
            return HttpResponse('Please check your email to confirm your registration.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = uidb64
        print(uid)
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    print(user)

    if user is not None and check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/activation_invalid.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = PasswordChangeForm
    success_url = '/accounts/password_change_done/'

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    form_class = PasswordResetForm
    success_url = '/accounts/password_reset_done/'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = '/accounts/password_reset_complete/'

