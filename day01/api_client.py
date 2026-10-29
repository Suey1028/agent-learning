import httpx


def get_user(user_id: int) -> dict:
    if user_id <= 0:
        raise ValueError("ID 必须是正整数")

    response = httpx.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        timeout=10.0,
    )
    response.raise_for_status()
    return response.json()