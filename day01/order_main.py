from order_tools import get_order
try:
    order_id=int(input("输入要查询的订单"))
    info=get_order(order_id)
    print(info)
except ValueError:
    print("输入错误：请输入整数订单编号")