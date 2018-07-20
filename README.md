[![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiSHhWQTd1eDdQNzNscDhLTFg0RXB3RjRzbnl4Y282dDR5MXFYTlExdVl2Yng3UGt4cmRqZUg5UUpKZVplcmp6cVYzdGw5WVhVNUd3OCtmRUpmeUxSTFhBPSIsIml2UGFyYW1ldGVyU3BlYyI6IlBhMVBnTUpmR3o4c1hVd1QiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)](https://console.aws.amazon.com/codebuild/home?region=us-east-1#/projects/django-celery-admin-ext/view)

This app adds the ability to manually run a periodic celery task from the Django Admin.  It requires *Django 1.3+* and
[ask/django-celery](http://github.com/ask/django-celery).

This app was forked from and inspired by [erussell/django-redis-status](http://github.com/erussell/django-redis-status).


Installation
---------

Put ``celery_admin`` in your ``INSTALLED_APPS``.

That's all. Only admin-users with ``superuser`` permission can see these stats.
