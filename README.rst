====
Bootstrap
=====

Bootstrap is an app for django that adds Twitter Bootstrap and other nicities to the Django admin.

Quick start
-----------

1. Add "bootstrap" to your INSTALLED_APPS settings before "django.contrib.admin" like this:

      INSTALLED_APPS = (
          ...
          'bootstrap',
          'django.contrib.admin',
      )

2. If you want to add custom css to the admin you can override the custom.css file by adding a file at admin/css/custom.css in your apps static directory.

3. Visit http://127.0.0.1:8000/admin/ to check it out.
