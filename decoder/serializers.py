from rest_framework import serializers

class VINDecoderInputSerializer(serializers.Serializer):
    vin = serializers.CharField(max_length=17)
