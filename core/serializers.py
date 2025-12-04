from rest_framework import serializers

class PingSerializer(serializers.Serializer):
    message = serializers.CharField()

class HealthCheckSerializer(serializers.Serializer):
    status = serializers.CharField()

class VersionSerializer(serializers.Serializer):
    version = serializers.CharField()

class UploadSerializer(serializers.Serializer):
    file = serializers.CharField()
    fileName = serializers.CharField()


    def validate_uploadSerializer(self, data):
        if not isinstance(data.get("file"), str) :
            raise serializers.ValidationError({"file":"file isn't valide" })
        if not isinstance(data.get("fileName"), str) :
            raise serializers.ValidationError({"fileName":"filename isn't valide" })
