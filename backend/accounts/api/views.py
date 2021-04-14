from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import BrowsableAPIRenderer,JSONRenderer

class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = [BrowsableAPIRenderer,JSONRenderer]

