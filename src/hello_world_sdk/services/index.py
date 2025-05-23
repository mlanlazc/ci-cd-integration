from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import HelloResponse, HttpValidationError, Language


class IndexService(BaseService):

    @cast_models
    def hello_world(self, language: Language = SENTINEL) -> HelloResponse:
        """Returns a greeting message with timestamp and optional language specification. Supported languages: en (English), sr (Serbian), es (Spanish), fr (French)

        :param language: language, defaults to None
        :type language: Language, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: HelloResponse
        """

        Validator(Language).is_optional().validate(language)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/",
                [self.get_access_token()],
            )
            .add_query("language", language)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return HelloResponse._unmap(response)
