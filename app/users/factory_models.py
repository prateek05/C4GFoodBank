from factory.django import DjangoModelFactory


class AgencySiteFactory(DjangoModelFactory):
    class Meta:
        model = "users.AgencySite"
        django_get_or_create = (
            "name",
            "latitude",
            "longitude",
            "address",
        )

    name = "test"
    latitude = 32.38
    longitude = -68.64
    address = "103 242, Wayne City, IL 62895"