import uuid

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from geopy.geocoders import Nominatim
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response as APIResponse

from campaigns.models import Campaign, Response
from campaigns.serializers import SurveySerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


def is_valid_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


geolocator = Nominatim(user_agent="food_bank_survey")
post_request_body = openapi.Schema(
    title="SurveyResponse",
    description="Survey Response Data",
    type=openapi.TYPE_OBJECT,
    properties={
        "coordinates": openapi.Schema(type=openapi.TYPE_STRING),
        "question_id": openapi.Schema(type=openapi.TYPE_STRING),
        "value": openapi.Schema(type=openapi.TYPE_STRING),
        "language": openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=["coordinates", "question_id", "value", "language"],
)
get_response = openapi.Response("survey get response", SurveySerializer)
# then unit test and make script to seed data base

# Returns the survey data and stores the survey response
@swagger_auto_schema(method="get", responses={200: get_response, 400: "Bad request"})
@swagger_auto_schema(
    method="post",
    request_body=post_request_body,
    response={201: "", 400: "Bad request"},
)
@api_view(["GET", "POST"])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def survey(request, campaign_id, site_id) -> APIResponse:

    if request.method == "GET":
        if (
            campaign_id
            and site_id
            and is_valid_uuid(campaign_id)
            and is_valid_uuid(site_id)
        ):
            try:
                campaign = Campaign.objects.get(pk=campaign_id, active=True)
                if campaign.active and campaign.sites.filter(pk=site_id).exists():
                    questions = campaign.questions.filter(active=True)
                    serializer = SurveySerializer(questions, many=True)
                    return APIResponse(serializer.data)
            except:
                return APIResponse(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "POST":
        if (
            campaign_id
            and site_id
            and is_valid_uuid(campaign_id)
            and is_valid_uuid(site_id)
        ):
            request_body = JSONParser().parse(request)
            for response in request_body:
                if (
                    "coordinates" in response
                    and response.get("coordinates") != ""
                    and response.get("coordinates") != None
                ):
                    response.update(
                        {
                            "location": geolocator.reverse(
                                response.get("coordinates")
                            ).raw["address"]["county"]
                        }
                    )
                    del response["coordinates"]
                else:
                    response.update({"location": None})
                    del response["coordinates"]
                response.update({"site_id": site_id})
                print(response)
                Response.objects.create(**response)
            return APIResponse(status=status.HTTP_204_NO_CONTENT)
    return APIResponse(status=status.HTTP_400_BAD_REQUEST)
