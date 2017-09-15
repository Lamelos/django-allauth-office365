# django-allauth-office365
django-allauth provider for office365

Use https://apps.dev.microsoft.com/ to create your application token.

Callback url is: /accounts/office365/login/callback/

Add application_id and secret in admin.

Usage:

to install use pip:

```
pip install git+https://github.com/Lamelos/django-allauth-office365.git
```

or add to your requirements file:

```
git+https://github.com/Lamelos/django-allauth-office365.git
```

Then add to installed_apps 'allauth_office365'

```
INSTALLED_APPS += 'allauth_office365'
```

optionally use socialadapter
```
SOCIALACCOUNT_ADAPTER = 'allauth_office365.adapter.SocialAccountAdapter
```

and you could disable email verification
```
SOCIALACCOUNT_EMAIL_VERIFICATION = False
```

you can specify scope and which value to use as username (defaults to displayName, e.g. "John Smith")

```
SOCIALACCOUNT_PROVIDERS = {
    'office365': {
      'SCOPE': ['User.read',],
      'USERNAME_FIELD': 'mail'
    }
}
```
