class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percentage):
        self.price * (1 - percentage / 100)

    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"{quantity} unit(s) sold. Remaining stock: {self.stock}")
        else:
            print("Out of stock.")

    def restock(self, quantity):
        self.stock += quantity
        print(f"Stock updated. New stock: {self.stock}")

    def is_available(self):
        return self.stock > 0
