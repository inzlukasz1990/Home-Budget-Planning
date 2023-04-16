import six

def make_token(user):
    return (
        six.text_type(user.pk) + six.text_type(user.email) + six.text_type(user.is_active)
    )

def check_token(user, token):
   print(token)
   return (
       six.text_type(user.pk) + six.text_type(user.email) + six.text_type(user.is_active) == token
   )
