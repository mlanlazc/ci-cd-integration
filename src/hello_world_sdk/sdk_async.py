from typing import Union
from .net.environment import Environment
from .sdk import HelloWorldSdk
from .services.async_.index import IndexServiceAsync
from .services.async_.openapi_json import OpenapiJsonServiceAsync


class HelloWorldSdkAsync(HelloWorldSdk):
    """
    HelloWorldSdkAsync is the asynchronous version of the HelloWorldSdk SDK Client.
    """

    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        super().__init__(access_token=access_token, base_url=base_url, timeout=timeout)

        self.index = IndexServiceAsync(base_url=self._base_url)
        self.openapi_json = OpenapiJsonServiceAsync(base_url=self._base_url)
