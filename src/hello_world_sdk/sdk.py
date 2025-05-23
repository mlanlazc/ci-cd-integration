from typing import Union
from .services.index import IndexService
from .services.openapi_json import OpenapiJsonService
from .net.environment import Environment


class HelloWorldSdk:
    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        """
        Initializes HelloWorldSdk the SDK class.
        """

        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self.index = IndexService(base_url=self._base_url)
        self.openapi_json = OpenapiJsonService(base_url=self._base_url)
        self.set_access_token(access_token)
        self.set_timeout(timeout)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )

        self.index.set_base_url(self._base_url)
        self.openapi_json.set_base_url(self._base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.index.set_access_token(access_token)
        self.openapi_json.set_access_token(access_token)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.index.set_timeout(timeout)
        self.openapi_json.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
