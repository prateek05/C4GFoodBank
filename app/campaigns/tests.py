# from django.test import TestCase

# from rest_framework import status
# from rest_framework.reverse import reverse
# from rest_framework.test import APIClient

# from campaigns.factory_models import QuestionFactory, CampaignFactory, QRCodeFactory
# from users.factory_models import CampaignUserFactory, AgencySiteFactory


# class TestGetSurvey(TestCase):
#     def setUp(self):
#         self.

#     def test_get_by_user_id(self):
#         user = CampaignUser.objects.create(name="fake", email="fake3@fake.com")
#         client = APIClient()
#         response = client.get(reverse("user"), dict(user_id=str(user.id)))
#         assert response.status_code == status.HTTP_200_OK
#         assert user.id == response.data["id"]

#     def test_get_by_name_and_email(self):
#         user = CampaignUser.objects.create(name="fake", email="fake5@fake.com")
#         client = APIClient()
#         response = client.get(reverse("user"), dict(name=user.name, email=user.email))
#         assert user.id == response.data["id"]

#     def test_get_create_user(self):
#         client = APIClient()
#         response = client.get(
#             reverse("user"), dict(name="new_fake", email="new_fake@fake.com")
#         )
#         assert response.status_code == status.HTTP_201_CREATED
#         user = User.objects.get(name="new_fake", email="new_fake@fake.com")
#         assert user.id == response.data["id"]

