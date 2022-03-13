from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response as APIResponse
from rest_framework.parsers import JSONParser

from campaigns.models import Campaign, Response
import uuid
from campaigns.serializers import SurveySerializer
from geopy.geocoders import Nominatim

def is_valid_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

geolocator = Nominatim(user_agent="food_bank_survey")

# Returns the survey data and stores the survey response
@api_view(["GET", "POST"])
def survey(request,campaign_id,site_id) -> APIResponse:
    if request.method == "GET":
        if campaign_id and site_id and is_valid_uuid(campaign_id) and is_valid_uuid(site_id):
            try:
                campaign = Campaign.objects.get(pk=campaign_id,active=True)
                if campaign.active and campaign.sites.filter(pk=site_id).exists():
                    questions = campaign.questions.filter(active=True)
                    serializer = SurveySerializer(questions, many=True)
                    return APIResponse(serializer.data)
            except:
                return APIResponse(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "POST":
        if campaign_id and site_id and is_valid_uuid(campaign_id) and is_valid_uuid(site_id):
            response_data = JSONParser().parse(request)
            for response in response_data:
                question_id = response.get("question_id")
                location = geolocator.reverse(response.get("coordinates")).raw['address']['county']
                language = response.get("language")
                value = response.get("value")
                Response.objects.create(question_id=question_id,location=location,language=language,value=value, site_id=site_id)
            return APIResponse(status=status.HTTP_204_NO_CONTENT)
    return APIResponse(status=status.HTTP_400_BAD_REQUEST)
