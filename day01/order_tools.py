def get_order(order_id: int)-> dict:
    orders = {
    1001: {"product": "Book", "status": "shipped"},
    1002: {"product": "Laptop", "status": "pending"},
    1003: {"product": "Phone", "status": "delivered"}
}
    order=orders.get(order_id)
    if order is not None:
        return {
            "success":True,
            "data":order,
            "error":None}
    else:
        return {
            "success":False,
            "data":None,
            "error": "Order not found"}