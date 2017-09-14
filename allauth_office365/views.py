from __future__ import unicode_literals

import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import Office365Provider


class Office365OAuth2Adapter(OAuth2Adapter):
    provider_id = Office365Provider.id
    authorize_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
    access_token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
    profile_url = 'https://graph.microsoft.com/v1.0/me'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

oauth2_login = OAuth2LoginView.adapter_view(Office365OAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(Office365OAuth2Adapter)
