from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import Office365Provider


urlpatterns = default_urlpatterns(Office365Provider)
