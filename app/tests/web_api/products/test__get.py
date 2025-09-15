import pytest
from uuid import uuid4


@pytest.mark.asyncio
async def test_get__then_200(client, product):
    # Act
    response = await client.get(f"/products/{product['id']}")

    # Assert
    assert response.status_code == 200

    assert response.json() == {
        'id': str(product['id']),
        'name': product['name'],
        'price': product['price']
    }


@pytest.mark.asyncio
async def test_get__non_existing_product__then_404(client):
    # Arrange
    fake_id = uuid4()

    # Act
    response = await client.get(f"/products/{fake_id}")

    # Assert
    assert response.status_code == 404
    assert response.json()['detail'] == f"Product {fake_id} not found"


@pytest.mark.asyncio
async def test_list__then_200(client, products):
    # Act
    response = await client.get('/products/')

    # Assert
    assert response.status_code == 200

    assert len(response.json()) == len(products)

    for p in products:
        assert any(resp_p['id'] == str(p['id']) for resp_p in response.json())


@pytest.mark.asyncio
async def test_list__when_empty__then_200(client):
    # Act
    response = await client.get('/products/')

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 0
