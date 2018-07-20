[![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRjZDaVR5K1BXVnFPdmJWdFgrWUFFVmJpT3ZWMmJ2SjE1YWJEeEo2VUpYeC81T0ZaeFVxODJVdUYxUUxyY1B4TnUwejNqY2hOdFg2a3J6TjE1djducVk4PSIsIml2UGFyYW1ldGVyU3BlYyI6IjBtakttMys2QU91Rm5QODMiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)](https://console.aws.amazon.com/codebuild/home?region=us-east-1#/projects/vendored_django-celery-admin-ext/view)

This app adds the ability to manually run a periodic celery task from the Django Admin.  It requires *Django 1.3+* and
[ask/django-celery](http://github.com/ask/django-celery).

This app was forked from and inspired by [erussell/django-redis-status](http://github.com/erussell/django-redis-status).


Installation
---------

Put ``celery_admin`` in your ``INSTALLED_APPS``.

That's all. Only admin-users with ``superuser`` permission can see these stats.
