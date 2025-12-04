from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import PingSerializer, HealthCheckSerializer, VersionSerializer, UploadSerializer
from imagekitio import ImageKit
from drf_spectacular.types import OpenApiTypes
import requests
import base64
from django.http import JsonResponse

#imagekit = ImageKit(
    #public_key='"public_h25G9MGlkxXsMj63Drey92giQEM=',
    #private_key='private_CBddGCKEuY8r/Y7MK6OmryhvB7Q=',
    #url_endpoint='https://ik.imagekit.io/nnatxct7i/'
#)

class HealthCheckView(APIView):
    @extend_schema(
        summary="Health check",
        description="Check if the API is alive.",
        responses={200: HealthCheckSerializer},
        tags=["HealthCheck"],
    )
    def get(self, request):
        return Response({"status": "ok"})


class VersionView(APIView):
    @extend_schema(
        summary="API version",
        description="Return the current version of the API.",
        responses={200: VersionSerializer},
        tags=["Version"],
    )
    def get(self, request):
        return Response({"version": "1.0.0"})


class PingView(APIView):
    @extend_schema(
        summary="Ping",
        description="Utility endpoint to check responses",
        responses={200: PingSerializer},
        tags=["Ping"],
    )
    def get(self, request):
        return Response({"message": "pong"})

class upload(APIView):
    @extend_schema(
        summary="upload",
        description="upload video",
        responses={200: PingSerializer},
        request=UploadSerializer,
        tags=["Upload"],

        # parameters=[
        #     OpenApiParameter(
        #         name="public_key",
        #         type=OpenApiTypes.STR,
        #         location=OpenApiParameter.HEADER,
        #         description="ImageKit public key"
        #     ),
        #     OpenApiParameter(
        #         name="private_key",
        #         type=OpenApiTypes.STR,
        #         location=OpenApiParameter.HEADER,
        #         description="ImageKit private key"
        #     ),
        #     OpenApiParameter(
        #         name="url_endpoint",
        #         type=OpenApiTypes.STR,
        #         location=OpenApiParameter.HEADER,
        #         description="ImageKit URL endpoint"
        #     ),
        # ],
    )

    
    def post(self, request):
       # file="https://ik.imagekit.io/nnatxct7i/sample-video_test_Kd8D0zWwK7.mp4?updatedAt=1764682393464",
       # file_name="video_ok.mp4", 
       #upload = imagekit.upload(file, file_name)
        # serializer = UploadSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # public_key = request.headers.get("public_key")
        # private_key =request.headers.get("private_key")
        # url_endpoint =request.headers.get("url_endpoint")
       
        # imagekit = ImageKit(
        # public_key, private_key, url_endpoint
        # )
    
        # file = request.data.get("file")
        # fileName =request.data.get("fileName")
        # upload = imagekit.upload(file, fileName)
        # return Response(upload.response_metadata.raw)
        #public_key = "public_h25G9MGlkxXsMj63Drey92giQEM="
        private_key = "private_CBddGCKEuY8r/Y7MK6OmryhvB7Q="

        auth_string = f"{private_key}:"
        auth_header = base64.b64encode(auth_string.encode()).decode()
        file = request.data.get("file")
        fileName =request.data.get("fileName")
        upload = ImageKit.upload(file, fileName)

        url = "https://upload.imagekit.io/api/v1/files/upload"

        #payload = "-----0110private_CBddGCKEuY8r/Y7MK6OmryhvB7Q=00010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fileName\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"publicKey\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"signature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expire\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"useUniqueFileName\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"folder\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isPrivateFile\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isPublished\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"customCoordinates\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"responseFields\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extensions\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhookUrl\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwriteFile\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwriteAITags\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwriteTags\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwriteCustomMetadata\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"customMetadata\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"transformation\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"checks\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"
        
        # files = {
        #         "file": open("https://ik.imagekit.io/nnatxct7i/women_in_red_a2pDcBwN-.jpg?updatedAt=1764760049197", "rb"),                 
        # }

        data = {
           # "file": "https://ik.imagekit.io/nnatxct7i/women_in_red_a2pDcBwN-.jpg?updatedAt=1764760049197",
            #"file": "https://ik.imagekit.io/nnatxct7i/sample-video_keys_XCdBUpr3R.mp4?updatedAt=1764767989481",
            #"fileName": "video_api_ok.mp4"
            #"fileName": "image_api_ok.jpg"
        }

        headers = {
            "Authorization": f"Basic {auth_header}"
        }

        response = requests.post(url, data=data, headers=headers)
        return JsonResponse(response.json(), safe=False)
        