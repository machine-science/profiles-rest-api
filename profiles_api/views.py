from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View
        This creates a new class based on the APIView class that django
        rest_framework provides.
        And it allows us to define application logic for our endpoint that we
        assign to this view. (You define a URL)
    """
    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view, but specifically intended to use for APIs',
            'Gives you the most control over the application logic',
            'mapped manually to the URLs',
        ]
        # response should be list or dictionary
        return Response({'message' : 'Hello','an_apiview' : an_apiview})
