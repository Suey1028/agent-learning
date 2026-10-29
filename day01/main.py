from api_practice import get_user
from storage import save_user
def main():
    try:
        user_id=int(input("请输入正确的用户ID:"))
        info=get_user(user_id)
        if info["success"]:
            saved_path=save_user(user_id,info["data"])
            print(f"保存成功：{saved_path}")
            print("查询成功")
            print(f"姓名：{info['data']['name']}")
            print(f"邮箱：{info['data']['email']}")
            print(f"公司：{info['data']['company_name']}")
        else:
            print(f"查询失败：{info['error']}")
    except ValueError as exc:
        print(f"输入错误:{exc}")
        
if __name__=="__main__":
    main()