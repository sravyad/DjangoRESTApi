from rest_framework import serializers

class HelloSerialiser(serializers.Serializer):
    """Serialiser for accepting name to the HelloWorldAPIView
    This not only helps in creating the field but also helps in validating. """

    name=serializers.CharField(max_length=10)
