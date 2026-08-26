#Different payment methods

class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class DebitCard:
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


# Payment Processor
class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def pay(self, amount):
        self.payment_method.pay(amount)


# Main program
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    payment = CreditCard()
elif choice == 2:
    payment = DebitCard()
elif choice == 3:
    payment = UPI()
else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(payment)
processor.pay(amount)