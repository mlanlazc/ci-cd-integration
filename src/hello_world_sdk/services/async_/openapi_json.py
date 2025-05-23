from typing import Awaitable
from .utils.to_async import to_async
from ..openapi_json import OpenapiJsonService


class OpenapiJsonServiceAsync(OpenapiJsonService):
    """
    Async Wrapper for OpenapiJsonServiceAsync
    """

    def get_openapi_json_openapi_json_get(self) -> Awaitable[any]:
        return to_async(super().get_openapi_json_openapi_json_get)()
