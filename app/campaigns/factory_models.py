import facotry
from users.factory_models import CampaignUserFactory, AgencySiteFactory

class QuestionFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'campaigns.Question'
        django_get_or_create = ('question','answer_choices','answer_template','language','active', 'additional_info', 'create_by')

    question = "test question"
    answer_choices = "Red,Blue,Green"
    answer_template='check'
    language = 'EN'
    active = True
    additional_info = ""
    create_by = factory.SubFactory(CampaignUserFactory)

class CampaignFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'campaigns.Campaign'
        django_get_or_create = ('name','create_by','active')

    name = "test campaign"
    

    @facotry.post_generation
    def questions(self,create,extracted):
        if not create:
            return
        if extracted:
            for question in extracted:
                self.questions.add(question)

    @facotry.post_generation
    def sites(self,create,extracted):
        if not create:
            return
        if extracted:
            for site in extracted:
                self.sites.add(site)

class QRCodeFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'campaigns.QRCode'
        django_get_or_create = ('slug','qr_code_path')

    slug = "32432/423423"
    qr_code_path = "code/path"
    

    @facotry.post_generation
    def campaigns(self,create,extracted):
        if not create:
            return
        if extracted:
            for campaign in extracted:
                self.campaigns.add(campaign)

    @facotry.post_generation
    def sites(self,create,extracted):
        if not create:
            return
        if extracted:
            for site in extracted:
                self.sites.add(site)

class ResponseFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'campaigns.Response'
        django_get_or_create = ('question','site','language','value','location')
    
    question = factory.SubFactory(QuestionFactory)
    site = factory.SubFactory(AgencySiteFactory)
    language = "EN"
    value = "value"
    value = "something county"


