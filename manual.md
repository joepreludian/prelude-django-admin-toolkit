# Installation instructions

On settings.py
1. Remove django.contrib.admin from installed apps;
2, Instead, install the prelude_django_admin_toolkit;

    'prelude_django_admin_toolkit',
    'prelude_django_admin_toolkit.apps.PrlAdminConfig',

3. Create a prelude_admin_class
4. Configure the admin_class into settings.py
5. Override admin under urls

    from prelude_django_admin_toolkit import admin
