from httpx import AsyncClient


async def test_users_get(client: AsyncClient) -> None:
    response = await client.get("localhost:8000/users")
    assert response.status == 200
    assert response.json() == {
        "result_count": 2,
        "total_count": 2,
        "data": [
            {

            },
            {

            },
        ],
    }
