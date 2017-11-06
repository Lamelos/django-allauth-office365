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
    _authorize_url_template = 'https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/authorize'
    _access_token_url_template = 'https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/token'
    profile_url = 'https://graph.microsoft.com/v1.0/me'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

    def _get_o365_tenant(self):
        # https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols#endpoints        
        """ 
        Available tenant values: common, organizations, consumers, contoso.onmicrosoft.com.
        """        
        from allauth.socialaccount import app_settings
        _settings = app_settings.PROVIDERS.get(self.get_provider().id, {})
        return _settings.get('TENANT', 'common')

    @property
    def authorize_url(self):        
        """Define the tenant's available for SocialLogin authorize (common, organizations, consumers, contoso.onmicrosoft.com)"""
        return self._authorize_url_template.format(TENANT=self._get_o365_tenant())

    @property
    def access_token_url(self):
        """Define the tenant's available for SocialLogin token (common, organizations, consumers, contoso.onmicrosoft.com)"""
        return self._access_token_url_template.format(TENANT=self._get_o365_tenant())


oauth2_login = OAuth2LoginView.adapter_view(Office365OAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(Office365OAuth2Adapter)
