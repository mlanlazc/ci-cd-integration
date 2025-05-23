from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .language import Language


@JsonMap({})
class HelloResponse(BaseModel):
    """HelloResponse

    :param message: The greeting message
    :type message: str
    :param timestamp: When the greeting was generated, defaults to None
    :type timestamp: str, optional
    :param language: language, defaults to None
    :type language: Language, optional
    """

    def __init__(
        self,
        message: str,
        timestamp: str = SENTINEL,
        language: Language = SENTINEL,
        **kwargs,
    ):
        """HelloResponse

        :param message: The greeting message
        :type message: str
        :param timestamp: When the greeting was generated, defaults to None
        :type timestamp: str, optional
        :param language: language, defaults to None
        :type language: Language, optional
        """
        self.message = message
        if timestamp is not SENTINEL:
            self.timestamp = timestamp
        if language is not SENTINEL:
            self.language = self._enum_matching(language, Language.list(), "language")
        self._kwargs = kwargs
