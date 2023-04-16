from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from .tokens import account_activation_token

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def send_confirmation_email(user):
    subject = 'Please confirm your email address'
    message_template = 'accounts/email/activation_email.txt'
    from_email = 'noreply@example.com'

    # Generate a token for the user
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # Render the email message
    message = render_to_string(message_template, {
        'user': user,
        'domain': 'your-domain.com',  # Replace with your domain
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

