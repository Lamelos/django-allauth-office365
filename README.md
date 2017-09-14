# django-allauth-office365
django-allauth provider for office365

Usage:

add to installed_apps 'allauth_office365'

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

you can specify scope and which value to use as username

```
SOCIALACCOUNT_PROVIDERS = {
    'office365': {
      'SCOPE': ['User.read',],
      'USERNAME_FIELD': 'mail'
    }
}
```
