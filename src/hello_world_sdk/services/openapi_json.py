from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class OpenapiJsonService(BaseService):

    @cast_models
    def get_openapi_json_openapi_json_get(self) -> any:
        """get_openapi_json_openapi_json_get

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/openapi-json",
                [self.get_access_token()],
            )
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
