from rest_framework.views import Response
from rest_framework.views  import APIView
from profiles_api import serializers
from rest_framework  import status

# Create your views here.

class HelloWorldAPIView(APIView):       #Innerited from API View class
    """Test  API View"""
    #Creating a temporary returnn response list
    #Response always expects list or dictionary and it converts the response to json n send
    #request is an django s request parameter
    serializer_class=serializers.HelloSerialiser

    def get(self,request,format=None):
        an_apiresponse=["Creating API View with HTTP  Methods (Put,Post,Get,Patch,Delete)",
                    "Learninng to create first API view",
                    "Will map to ann URL",
                    "Deploy n get the API view running"]
        return Response({"Message":"Hello","an_apiresponse":an_apiresponse})

    def post(self,request):
        """Creating a hellow world API with name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')  #name is the variale defined inn the serilizer.py file. can fetch any col we want
            message=f'Hello {name}'
            return Response({'message':message})
        return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
        )

    def put(self,request,pk=None):
        """Updating the  record"""
        return Response({"message":"put"})

    def patch(self,request,pk=None):
        """Partially Updating the  record"""
        return Response({"message":"patch"})

    def delete(self,request,pk=None):
        """Deleting the  record"""
        return Response({"message":"Delete"})
