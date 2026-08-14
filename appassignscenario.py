#cricketmatch
class Player:
    def __init__(self, name, jersey, runs):
        self.name = name
        self.jersey = jersey
        self.runs = runs

    def category(self):
        if self.runs >= 500:
            return "Excellent"
        elif self.runs >= 250:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Name:", self.name)
        print("Jersey Number:", self.jersey)
        print("Runs:", self.runs)
        print("Category:", self.category())
        print("----------------------")


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print("CRICKET TEAM DETAILS")
        print("====================")
        for player in self.players:
            player.display()


# Create team
team = Team()

# Add players
team.add_player(Player("Virat", 18, 650))
team.add_player(Player("Rohit", 45, 400))
team.add_player(Player("Rahul", 1, 150))

# Display all players
team.display_players()

#inventory system
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category())
        print("-------------------")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("PRODUCT INVENTORY")
        print("=================")
        for product in self.products:
            product.display()


# Create inventory
inventory = Inventory()

# Add products
inventory.add_product(Product(101, "Laptop", 50000))
inventory.add_product(Product(102, "Mouse", 500))
inventory.add_product(Product(103, "Headphones", 1500))

# Display products
inventory.display_products()