print("Lista zakupów")
grocery_list = {
    "piekarnia": ["chleb", "bułki", "pączek"], 
    "warzywniak": ["marchew", "seler", "rukola"]
}

for store, product in grocery_list.items():
    print(f"Idę do {store.capitalize()} i kupuję tam {[k.capitalize() for k in product]}")

