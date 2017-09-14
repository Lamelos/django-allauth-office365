from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import Office365Provider


class Office365Tests(OAuth2TestsMixin, TestCase):
    provider_id = Office365Provider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
        {
          "givenName": "James",
          "jobTitle": None,
          "userPrincipalName": "james.smith@company.com",
          "businessPhones": [],
          "mobilePhone": None,
          "surname": "Smith",
          "displayName": "James Smith",
          "mail": "james.smith@company.com",
          "preferredLanguage": "en-US",
          "id": "123456677890",
          "officeLocation": None,
          "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity"
        }
        """)
