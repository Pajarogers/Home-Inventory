import tkinter as tk

class InventoryLog:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_name, quantity):
        # Make the product name case-insensitive by converting it to lowercase.
        product_name = product_name.lower()
        
        if product_name in self.inventory:
            print(f"Product '{product_name}' already exists. Updating quantity.")
            self.inventory[product_name]['quantity'] += quantity
        else:
            self.inventory[product_name] = {'quantity': quantity}
            print(f"Added '{product_name}' to the inventory.")

    def remove_product(self, product_name, quantity):
        product_name = product_name.lower()
        if product_name in self.inventory:
            if self.inventory[product_name]['quantity'] >= quantity:
                self.inventory[product_name]['quantity'] -= quantity
                print(f"Removed {quantity} units of '{product_name}' from the inventory.")
            else:
                print(f"Insufficient quantity of '{product_name}' in the inventory.")
        else:
            print(f"Product '{product_name}' not found in the inventory.")

    def search_product(self, product_name):
        product_name = product_name.lower()
        if product_name in self.inventory:
            return f"Product: {product_name}, Quantity: {self.inventory[product_name]['quantity']}"
        else:
            return f"Product '{product_name}' not found in the inventory."


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("P&A Home Inventory Management")
        self.root.geometry("600x400")  # Set the initial size of the window.

        self.inventory_log = InventoryLog()

        self.product_name_label = tk.Label(root, text="Product Name:", font=("Arial", 16))
        self.product_name_label.pack()
        self.product_name_entry = tk.Entry(root, font=("Arial", 16))
        self.product_name_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:", font=("Arial", 16))
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root, font=("Arial", 16))
        self.quantity_entry.pack()

        self.add_button = tk.Button(root, text="Add Product", command=self.add_product, font=("Arial", 16))
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Product", command=self.remove_product, font=("Arial", 16))
        self.remove_button.pack()

        self.search_label = tk.Label(root, text="Search Product:", font=("Arial", 16))
        self.search_label.pack()
        self.search_entry = tk.Entry(root, font=("Arial", 16))
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_product, font=("Arial", 16))
        self.search_button.pack()

        self.clear_search_button = tk.Button(root, text="Clear Search", command=self.clear_search, font=("Arial", 16))
        self.clear_search_button.pack()

        self.search_result_label = tk.Label(root, text="", font=("Arial", 16))
        self.search_result_label.pack()

    def add_product(self):
        product_name = self.product_name_entry.get().strip()  # Remove leading and trailing spaces
        quantity = int(self.quantity_entry.get())
        self.inventory_log.add_product(product_name, quantity)
        self.clear_entry_fields()

    def remove_product(self):
        product_name = self.product_name_entry.get().strip()
        quantity = int(self.quantity_entry.get())
        self.inventory_log.remove_product(product_name, quantity)
        self.clear_entry_fields()

    def search_product(self):
        product_name = self.search_entry.get().strip()
        result = self.inventory_log.search_product(product_name)
        self.search_result_label.config(text=result)

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.search_result_label.config(text="")

    def clear_entry_fields(self):
        self.product_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

