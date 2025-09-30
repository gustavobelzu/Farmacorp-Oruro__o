from django.contrib.auth.models import User

superusers = User.objects.filter(is_superuser=True)
for u in superusers:
    print(u.username, u.email)