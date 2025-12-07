import csv
from datetime import datetime

def log_error(row: list, error: str):
    with open("errors.log", "a", encoding="utf-8") as file:
        file.write(f"{row} - {error}\n")

date_revenue = {}
store_revenue = {}
store_purchase_quantity = {}
product_quantity = {}
product_revenue = {}
month_revenue = {}

product_avg_price = {}
store_avg_purchase = {}

most_sold_product = None
store_highest_revenue = None
day_biggest_revenue = None
top_3_product_by_revenue = []
top_3_product_by_quantity = []

with open("predaje.csv", "r", newline="") as file:
    data = csv.DictReader(file)

    for row in data:
        include_row = True

        try:
            datetime.strptime(row["datum"], "%Y-%m-%d")

            if not row["obchod"] or not row["produkt"]:
                raise ValueError("Missing required field")
            
            int(row["ks"])
            float(row["cena"])            

        except Exception as e:
            log_error(row, str(e))
            include_row = False
    
        if include_row:
            date = row["datum"]
            store = row["obchod"]
            product = row["produkt"]
            quantity = int(row["ks"])
            price = float(row["cena"])

            date_revenue.setdefault(date, 0)
            date_revenue[date] += quantity * price

            store_revenue.setdefault(store, 0)
            store_revenue[store] += quantity * price

            product_quantity.setdefault(product, 0)
            product_quantity[product] += quantity

            product_revenue.setdefault(product, 0)
            product_revenue[product] += quantity * price

            month = date[5:7]
            month_revenue.setdefault(month, 0)
            month_revenue[month] += quantity * price

            store_purchase_quantity.setdefault(store, 0)
            store_purchase_quantity[store] += 1

            if day_biggest_revenue is None or day_biggest_revenue[1] < (quantity * price):
                day_biggest_revenue = (date, quantity * price)

for product in product_revenue:
    product_avg_price[product] = product_revenue[product] / product_quantity[product]

for store in store_revenue:
    store_avg_purchase[store] = store_revenue[store] / store_purchase_quantity[store]

most_sold_product = max(product_quantity.items(), key=lambda x: x[1])
store_highest_revenue = max(store_revenue.items(), key=lambda x: x[1])
top_3_product_by_revenue = sorted(product_revenue.items(), key=lambda x: x[1], reverse=True)[0:3]
top_3_product_by_quantity = sorted(product_quantity.items(), key=lambda x: x[1], reverse=True)[0:3]

with open("vysledok.txt", "w") as file:

    file.write("Total revenues are:\n")
    for date, revenue in date_revenue.items():
        file.write(f"{date} {revenue:.2f}\n")
    
    file.write(f"\nThe most sold product was {most_sold_product[0]} -> {most_sold_product[1]} times.\n")

    file.write("\nStores' purchase quantities are:\n")
    for store, quantity in store_purchase_quantity.items():
        file.write(f"{store} {quantity}\n")

    file.write("\nAverage products' average prices:\n")
    for product, avg_price in product_avg_price.items():
        file.write(f"{product} {avg_price:.2f}\n")

    file.write("\nProducts' quantity:\n")
    for product, quantity in product_quantity.items():
        file.write(f"{product} {quantity}\n")

    file.write("\nProducts' revenues:\n")
    for product, revenue in product_revenue.items():
        file.write(f"{product} {revenue:.2f}\n")
    
    file.write("\nStores' revenues are:\n")
    for store, revenue in store_revenue.items():
        file.write(f"{store} {revenue:.2f}\n")
    
    file.write(f"\nStore with the biggest revenue is {store_highest_revenue[0]} -> {store_highest_revenue[1]:.2f}\n")

    file.write("\nMonths' revenues are:\n")
    for month, revenue in month_revenue.items():
        file.write(f"{month} {revenue:.2f}\n")
    
    file.write("\nThe top 3 products by revenu are: " + ", ".join([product[0] for product in top_3_product_by_revenue]) + "\n")
    file.write("\nThe top 3 products by quantity are: " + ", ".join([product[0] for product in top_3_product_by_quantity]) + "\n")

    file.write("\nShops' average value per purchase are:\n")
    for store, avg_purchase in store_avg_purchase.items():
        file.write(f"{store} {avg_purchase:.2f}\n")
    
    file.write(f"\nThe day with biggest revenue is {day_biggest_revenue[0]} -> {day_biggest_revenue[1]:.2f}")