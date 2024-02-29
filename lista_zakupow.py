print("Lista zakupów")
grocery_list = {
    "piekarnia": ["chleb", "bułki", "pączek"], 
    "warzywniak": ["marchew", "seler", "rukola"],
    "mięsny": ["wieprzowina", "wołowina", "kurczak"]
}

grocery_list["warzywniak"].append("pietruszka")
print(grocery_list)

l = 0
for store, product in grocery_list.items():
    l = l + len(product)
    print(f"Idę do {store.capitalize()} i kupuję tam {[k.capitalize() for k in product]}")

print(f"W sumie kupuję {l} produktów")
