from hello_world_sdk import HelloWorldSdk
from hello_world_sdk.models import Language

sdk = HelloWorldSdk(access_token="YOUR_ACCESS_TOKEN", timeout=10000)

result = sdk.index.hello_world(language="en")

print(result)
