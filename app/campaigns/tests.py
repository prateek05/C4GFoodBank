from django.test import TestCase

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from campaigns.models import Question, Campaign
from users.factory_models import AgencySiteFactory


class TestGetSurvey(TestCase):

    def test_get_campaign(self):
        site = AgencySiteFactory.create()
        client = APIClient()
        campaign = Campaign.objects.create(name="test", actor_type = "Client",active = True)
        campaign.sites.add(site)
        campaign.save()
        response = client.get(reverse("survey", kwargs=dict(campaign_id=campaign.campaign_id,site_id=site.site_id)))
        assert response.status_code == status.HTTP_200_OK
    
    def test_post_campaign(self):
        site = AgencySiteFactory.create()
        client = APIClient()
        campaign = Campaign.objects.create(name="test", actor_type = "Client",active = True)
        campaign.sites.add(site)
        campaign.save()
        response = client.post(reverse("survey", kwargs=dict(campaign_id=campaign.campaign_id,site_id=site.site_id)), dict(language="en",value="value", coordinates=None), format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_error(self):
        client = APIClient()
        response = client.get(reverse("survey", kwargs=dict(campaign_id="89890",site_id="80989")))
        assert response.status_code == status.HTTP_400_BAD_REQUEST


