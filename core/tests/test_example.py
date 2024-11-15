import pytest
from datetime import date
from core.models import TaskUser


@pytest.mark.django_db
def test_create_taskuser():
    user = TaskUser(
        email='test1@email.com',
        first_name='John',
        last_name='Doe',
        date_of_birth=date(2000, 1, 1)
    )
    user.save()
    assert user.email == 'test1@email.com'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.date_of_birth.isoformat() == '2000-01-01'

    assert TaskUser.objects.count() == 1