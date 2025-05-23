from typing import Awaitable, Union
from .utils.to_async import to_async
from ..index import IndexService
from ...models.utils.sentinel import SENTINEL
from ...models import HelloResponse, Language


class IndexServiceAsync(IndexService):
    """
    Async Wrapper for IndexServiceAsync
    """

    def hello_world(self, language: Language = SENTINEL) -> Awaitable[HelloResponse]:
        return to_async(super().hello_world)(language)
