class Customer:
    def __init__(self, name, email):
        self.__name = name  # private name
        self.__email = email  # private email
        self.orders = []  # list to store customer orders

    def placeOrder(self, order):
        self.orders.append(order)  # order is an object. Add the given order to the orders list

    def getOrders(self):
        return self.orders  # returns a list of customer's orders

    def getName(self):
        return self.__name  # getter method to access private name

    def getEmail(self):
        return self.__email  # getter method to access private email

class Order:
    def __init__(self, orderId, products):
        self.__orderId = orderId  # order ID (private)
        self.products = products  # list of products in the order

    def getOrderId(self):
        return self.__orderId  # getter method to access private orderId

    def getTotalPrice(self):  # calculate the total price of products
        totalPrice = 0
        for product in self.products:
            totalPrice += product.getPrice()
        return totalPrice

class Product:
    def __init__(self, name, price):
        self.__name = name  # private product name
        self.__price = price  # private product price

    def getName(self):
        return self.__name  # getter method to access private product name

    def getPrice(self):
        return self.__price  # getter method to access private product price

customer1 = Customer("Pari", "pari@gmail.com")
product1 = Product("Samsung", 500)
product2 = Product("Nokia", 600)
order1 = Order(1, [product1, product2])
customer1.placeOrder(order1)
print("Customer Name:", customer1.getName())
print("Customer Email:", customer1.getEmail())
orders = customer1.getOrders()
for order in orders:
    print("Order ID =", order.getOrderId())
    print("Products:")
    for product in order.products:
        print(product.getName(), product.getPrice())
    print("Total Price:", order.getTotalPrice())
