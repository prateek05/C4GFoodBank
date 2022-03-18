from campaigns.models import Campaign, Question
from users.models import AgencySite, CampaignUser

def run():
    user = CampaignUser.objects.update_or_create(name="test3", username="test3", is_superuser=True, is_staff=True)[0]
    try:
        user.set_password("test2")
        user.save()
    except:
       pass
    site = AgencySite.objects.update_or_create(site_id="1417fcf4-b7e0-49b3-ae9c-89f125b3973f",name="testSite", latitude=53.62, longitude=17.27, address = "Some place in Florida", point_of_contact=user)[0]
    question1 = Question.objects.update_or_create(question_id="5338d28c-8485-4033-a541-d5675745646e", question="How satisfied with the packaging of the food that you received?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question2 = Question.objects.update_or_create(question_id="130ae8f1-25c9-4981-bdb8-231054696095", question="How would you rate the quality of the food you received?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question3 = Question.objects.update_or_create(question_id="a5e92553-b690-4c68-b3c2-d4ea0b34b4e2", question="How satisfied with the amount of food that you received?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question4 = Question.objects.update_or_create(question_id="b2d78961-1787-4608-b993-999dc02f9b60", question="How satisfied with the agency that supplied you with food?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question5 = Question.objects.update_or_create(question_id="cc7f91ea-a81c-422f-8760-d916f16e9981", question="How satisfied with the staff at the agency that supported you?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question6 = Question.objects.update_or_create(question_id="c0fa6034-b32e-4696-8222-137fee107f7c", question="How respectable was the staff at the agency?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question7 = Question.objects.update_or_create(question_id="6d5beaf1-092a-49ba-b109-e040417d42ae", question="How likely would you be to return to this agency?", answer_choices="Satisfied,Neither satisfied nor dissatisfied,Dissatisfied", answer_template="radio", language="EN",active=True, create_by=user )[0]
    question8 = Question.objects.update_or_create(question_id="1f075a18-db47-405a-9d05-ab64738d535b", question="[Optional] Anything else you’d like to add?", answer_choices="", answer_template="text", language="EN",active=True, create_by=user )[0]
    campaign = Campaign.objects.update_or_create(campaign_id="22581882-8786-4558-b1af-54cbb9736b6a", name="TestCampaign", create_by=user, actor_type="client", active=True)[0]
    campaign.sites.add(site)
    campaign.questions.add(question1, question2, question3, question4, question5, question6, question7, question8)
    campaign.save()