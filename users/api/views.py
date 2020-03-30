from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Succesfully registered a user"
            data['name'] = user.name
            data['email'] = user.email
            data['username'] = user.username

        else:
            data = serializer.errors
        return Response(data)
