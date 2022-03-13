import facotry

class CampaignUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.CampaignUser'
        django_get_or_create = ('name')

        name = "test"

class AgencySiteFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.AgencySite'
        django_get_or_create = ('name','latitude','longitude','address','point_of_contact')

    name = "test"
    latitude = 32.38
    longitude = -68.64
    address = "103 242, Wayne City, IL 62895"
    point_of_contact = factory.SubFactory(CampaignUserFactory)
