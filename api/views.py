""" Rest Framework's packages """
from rest_framework.authtoken.views import ObtainAuthToken # used for authentication
from rest_framework.settings import api_settings # used to render login API in browser
from rest_framework.views import APIView # APIView helper classes
from rest_framework.response import Response # Response Class to send response to requester

from books.models import Books 


class Login(ObtainAuthToken): # Extends ObtainAuthToken class
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # To render browsable API in browser


class BookView(APIView): # Extends APIView
    
    
    def get(self, request) :
        books = Books.objects.all()
        return Response(books.values())
        
                   


