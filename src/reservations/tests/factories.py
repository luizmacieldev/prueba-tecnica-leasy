from datetime import timedelta

import factory
from django.contrib.auth.models import Permission, User
from django.utils import timezone

from reservations.constants import RESERVATION_STATUS_REQUESTED
from reservations.models import Customer, Reservation, Room


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    is_active = True

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if not create:
            return
        self.set_password(extracted or "demo1234")
        self.save()


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    user = factory.SubFactory(UserFactory)
    display_name = factory.Sequence(lambda n: f"Customer {n}")


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    name = factory.Sequence(lambda n: f"Room {n}")
    floor = 1
    capacity = 4


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    customer = factory.SubFactory(CustomerFactory)
    room = factory.SubFactory(RoomFactory)
    status = RESERVATION_STATUS_REQUESTED
    starts_at = factory.LazyFunction(lambda: timezone.now() + timedelta(days=1))
    ends_at = factory.LazyAttribute(lambda obj: obj.starts_at + timedelta(hours=2))
    internal_note = ""


def grant_permission(*, user: User, codename: str) -> None:
    permission = Permission.objects.get(codename=codename)
    user.user_permissions.add(permission)
