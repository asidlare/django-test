import pytest


@pytest.mark.django_db
def test_create_taskuser(api_client) -> None:
    """
    Test the create task user API
    :param api_client:
    :return: None
    """
    payload = {
        "userEmail": "test1@email.com",
        "userFirstName": "John",
        "userLastName": "Doe",
        "userDateOfBirth": "2000-01-01",
    }

    # Create a task
    response_create = api_client.post("/task-users", data=payload, format="json")

    user_id = response_create.data["userId"]
    assert response_create.status_code == 201
    assert response_create.data["userEmail"]== payload["userEmail"]
    assert response_create.data["userFirstName"]== payload["userFirstName"]
    assert response_create.data["userLastName"]== payload["userLastName"]
    assert response_create.data["userDateOfBirth"]== payload["userDateOfBirth"]

    # Read the task
    response_read = api_client.get(f"/task-user/{user_id}", format="json")
    assert response_read.status_code == 200
    assert response_read.data["userEmail"]== payload["userEmail"]
    assert response_read.data["userFirstName"]== payload["userFirstName"]
    assert response_read.data["userLastName"]== payload["userLastName"]
    assert response_read.data["userDateOfBirth"]== payload["userDateOfBirth"]
