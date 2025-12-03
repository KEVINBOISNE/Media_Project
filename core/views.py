from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .serializers import PingSerializer, HealthCheckSerializer, VersionSerializer
from imagekitio import ImageKit

imagekit = ImageKit(
    public_key='public_h25G9MGlkxXsMj63Drey92giQEM=',
    private_key='private_CBddGCKEuY8r/Y7MK6OmryhvB7Q=',
    url_endpoint = 'https://ik.imagekit.io/nnatxct7i'
)

class HealthCheckView(APIView):
    @extend_schema(
        summary="Health check",
        description="Check if the API is alive.",
        responses={200: HealthCheckSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"status": "ok"})


class VersionView(APIView):
    @extend_schema(
        summary="API version",
        description="Return the current version of the API.",
        responses={200: VersionSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"version": "1.0.0"})


class PingView(APIView):
    @extend_schema(
        summary="Ping",
        description="Utility endpoint to check responses",
        responses={200: PingSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"message": "pong"})

class upload(APIView):
    @extend_schema(
        summary="upload",
        description="upload video",
        responses={200: PingSerializer},
        tags=["core"],
    )
    def post(self, request):
        upload = imagekit.upload(
        file="https://ik.imagekit.io/nnatxct7i/sample-video_test_Kd8D0zWwK7.mp4?updatedAt=1764682393464",
        file_name="video_ok_testt.mp4",
    )

        return Response(upload.response_metadata.raw)
     

   