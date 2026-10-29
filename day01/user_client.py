
import httpx


class UserClient:

    def __init__(self, base_url: str, timeout: float = 10.0):
        self.base_url = base_url
        self.timeout = timeout

    def get_user(self, user_id: int) -> dict:
        url = f"{self.base_url}/users/{user_id}"

        response = httpx.get(
            url,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def get_post(self,post_id:int) ->dict:
        url=f"{self.base_url}/posts/{post_id}"
        try:
            response=httpx.get(url,timeout=self.timeout)
            response.raise_for_status()
            data=response.json()
            return {
                "success":True,
                "data":{
                    "userId":data["userId"],
                    "id":data["id"],
                    "title":data["title"],
                    "body":data["body"]
                },
                "error":None
            }
        except httpx.HTTPStatusError as exc:
            return{
                "success":False,
                "data":None,
                "error":f"http请求失败，状态码：{exc.response.status_code}"
            }
        except httpx.RequestError as exc:
            return{
                "success":False,
                "data":None,
                "error":f"网络请求失败:{exc}"
            }


