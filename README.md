django-bootstrap-admin
======================
Bootstrap Themed Django Admin. 

*THIS PROJECT IS UNDER ACTIVE DEVELOPMENT*

To install run
    
    pip install django-bootstrap-admin

Add "bootstrap" to your INSTALLED_APPS settings before `django.contrib.admin` like this:

    INSTALLED_APPS = (
      'bootstrap',
      'django.contrib.admin',
    )

If you want to add custom css to the admin you can override the custom.css file by adding a file at `admin/css/custom.css` in your apps static directory.
