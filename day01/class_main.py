from user_client import UserClient

client1=UserClient("https://jsonplaceholder.typicode.com",5)
client2=UserClient("https://jsonplaceholder.typicode.com",20)
print(f"用户1超时:{client1.timeout}秒")
print(f"用户2超时:{client2.timeout}秒")
post1=client1.get_post(1)
if post1["success"]:
    print("查询成功！")
    print(f"标题：{post1['data']['title']}")
    print(f"正文：{post1['data']['body']}")
else:
    print(f"查询失败：{post1['error']}")
post2 = client1.get_post(99999)
print(post2)
# # 第一步：创建对象
# client = UserClient(
#     "https://jsonplaceholder.typicode.com"
# )

# # 第二步：查看对象的属性
# print(client.base_url)
# print(client.timeout)

# # 第三步：调用对象的方法
# user = client.get_user(1)

# print(user["name"])