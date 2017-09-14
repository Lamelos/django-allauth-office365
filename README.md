# django-allauth-office365
django-allauth provider for office365

Usage:

add to installed_apps 'allauth_office365'

optionally use socialadapter

you can specify scope and which value to use as username

SOCIALACCOUNT_PROVIDERS = {
    'office365': {
      'SCOPE': ['User.read',],
      'USERNAME_FIELD': 'mail'
    }
}
