====
Bootstrap
=====

Bootstrap is an app for django that adds Twitter Bootstrap and other nicities to the Django admin.

Quick start
-----------

1. Add "bootstrap" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'bootstrap',
      )

2. Include the bootstrap URLconf in your project urls.py like this::

      url(r'^admin/', include('bootstrap.urls')),

3. Run `python manage.py migrate` to create the models.

4. Visit http://127.0.0.1:8000/admin/ to check it out.
