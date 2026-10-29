
# import httpx

# url = "https://jsonplaceholder.typicode.com/users/1"

# response = httpx.get(url, timeout=10.0)

# print(response.status_code)

# data = response.json()

# print(data)
import httpx
def get_user(user_id: int)->dict:
    if user_id<=0:
        raise ValueError("用户ID必须是整数")
    url=f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response=httpx.get(url,timeout=10.0)
        response.raise_for_status()
        data=response.json()
        if not isinstance(data,dict):
            raise ValueError("API返回的不是字典")

        return{
        "success":True,
        "data":{
            "name": data["name"],
            "email": data["email"],
            "company_name": data["company"]["name"],
        },
        "error":None}

    except httpx.HTTPStatusError as exc:
        return{
        "success":False,
        "data":None,
        "error":f"HTTP 请求失败：{exc.response.status_code}"
        }

    except httpx.RequestError as exc:
        return{
        "success":False,
        "data":None,
        "error":f"网络请求失败：{exc}"
        }

    except (ValueError, KeyError, TypeError) as exc:
        return {
            "success": False,
            "data": None,
            "error": f"API 返回的数据无效：{exc}"
        }
