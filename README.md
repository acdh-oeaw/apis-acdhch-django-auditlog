# Archived

This project is not needed/used anymore, we now use
[django-auditlog](https://pypi.org/project/django-auditlog/) instead, which is
way more flexible and powerful. Therefore this project is archived.

## apis_acdhch_django_auditlog

Auditlog integration for APIS apps at the ACDH-CH at the OEAW

## Installation

Add `apis_acdhch_django_auditlog` to your `INSTALLED_APPS`.
Include the apis-acdhch-django-auditlog urls in your `urls.py`:
```
urlpatterns += [path("", include("apis_acdhch_django_auditlog.urls")),]
```
