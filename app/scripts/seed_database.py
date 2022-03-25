from campaigns.models import Campaign, Question, AnswerChoice
from users.models import AgencySite, CampaignUser

def run():
    user = CampaignUser.objects.update_or_create(username="test3", defaults=dict(name="test3", is_superuser=True, is_staff=True))[0]
    try:
        user.set_password("test2")
        user.save()
    except:
       pass
    site = AgencySite.objects.update_or_create(site_id="1417fcf4-b7e0-49b3-ae9c-89f125b3973f",defaults=dict(name="testSite", latitude=53.62, longitude=17.27, address = "Some place in Florida", point_of_contact=user))[0]
    answer_choice1 = AnswerChoice.objects.update_or_create(answer_id="5e6fec5a-519b-4857-b550-f67e17c5d263", defaults=dict(answer_value="Satisfied"))[0]
    answer_choice2 = AnswerChoice.objects.update_or_create(answer_id="16db0e8e-6bbd-42d3-8a63-e0f233f46c97", defaults=dict(answer_value="Neither satisfied nor dissatisfied"))[0]
    answer_choice3 = AnswerChoice.objects.update_or_create(answer_id="9b7f504f-b513-4c5a-ac02-093f921a54e5", defaults=dict(answer_value="Dissatisfied"))[0]
    question1 = Question.objects.update_or_create(question_id="5338d28c-8485-4033-a541-d5675745646e", defaults=dict(question="How satisfied with the packaging of the food that you received?", answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question2 = Question.objects.update_or_create(question_id="130ae8f1-25c9-4981-bdb8-231054696095", defaults=dict(question="How would you rate the quality of the food you received?",  answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question3 = Question.objects.update_or_create(question_id="a5e92553-b690-4c68-b3c2-d4ea0b34b4e2", defaults=dict(question="How satisfied with the amount of food that you received?", answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question4 = Question.objects.update_or_create(question_id="b2d78961-1787-4608-b993-999dc02f9b60", defaults=dict(question="How satisfied with the agency that supplied you with food?", answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question5 = Question.objects.update_or_create(question_id="cc7f91ea-a81c-422f-8760-d916f16e9981", defaults=dict(question="How satisfied with the staff at the agency that supported you?", answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question6 = Question.objects.update_or_create(question_id="c0fa6034-b32e-4696-8222-137fee107f7c", defaults=dict(question="How respectable was the staff at the agency?", answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question7 = Question.objects.update_or_create(question_id="6d5beaf1-092a-49ba-b109-e040417d42ae", defaults=dict(question="How likely would you be to return to this agency?", answer_template="radio", language="EN",active=True, create_by=user ))[0]
    question8 = Question.objects.update_or_create(question_id="1f075a18-db47-405a-9d05-ab64738d535b", defaults=dict(question="[Optional] Anything else you’d like to add?", answer_template="text", language="EN",active=True, create_by=user ))[0]
    question1.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question1.save()
    question2.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question2.save()
    question3.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question3.save()
    question4.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question4.save()
    question5.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question5.save()
    question6.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question6.save()
    question7.answer_choices.add(answer_choice1,answer_choice2,answer_choice3)
    question7.save()
    campaign = Campaign.objects.update_or_create(campaign_id="22581882-8786-4558-b1af-54cbb9736b6a", defaults=dict(name="TestCampaign", create_by=user, actor_type="client", active=True))[0]
    campaign.sites.add(site)
    campaign.questions.add(question1, question2, question3, question4, question5, question6, question7, question8)
    campaign.save()