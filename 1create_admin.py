import os
import os.path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectFinance.settings')

import django
django.setup()

from django.contrib.auth.models import User
from django.db import transaction

if __name__ == '__main__':
    with transaction.atomic():
        username = 'admin'
        password = "admin@123"
        email = 'admin@getnada.com'
        first_name = 'Admin'
        admin_user = User(
            username=username,
            email=email,
            first_name=first_name,
            is_superuser=True,
            is_active=True,
            )
        admin_user.set_password(password)
        admin_user.full_clean()
        admin_user.save()
        print ("Admin User Created Sucessfully!!!")