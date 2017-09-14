from __future__ import unicode_literals

from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class Office365Account(ProviderAccount):

    def to_str(self):
        name = '{0} {1}'.format(self.account.extra_data.get('first_name', ''),
                                self.account.extra_data.get('last_name', ''))
        if name.strip() != '':
            return name
        return super(Office365Account, self).to_str()


class Office365Provider(OAuth2Provider):
    id = str('office365')
    name = 'Office365'
    account_class = Office365Account

    def get_scope(self, request):
        scope = set(super(Office365Provider, self).get_scope(request))
        scope.add('openid')
        return list(scope)

    def get_default_scope(self):
        return ['openid', 'User.read']

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        try:
            email = data.get('mail')
        except:
            email = None

        return dict(email=email,
                    username=data.get(self.get_settings().get('USERNAME_FIELD', 'displayName')),
                    last_name=data.get('surname'),
                    first_name=data.get('givenName'))


provider_classes = [Office365Provider]
