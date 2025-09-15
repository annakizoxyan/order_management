import pytest


@pytest.mark.asyncio
async def test_create__then_200(client, product_payload):
    # Act
    response = await client.post('/products/', json=product_payload)

    # Assert
    assert response.status_code == 200

    assert response.json()['name'] == product_payload['name']


@pytest.mark.asyncio
async def test_create__when_missing_fields__then_422(client):
    # Arrange
    payload = {'price': 9.99}

    # Act
    response = await client.post('/products/', json=payload)

    # Assert
    assert response.status_code == 422
