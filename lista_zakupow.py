print("Lista zakupów")
grocery_list = {
    "piekarnia": ["chleb", "bułki", "pączek"], 
    "warzywniak": ["marchew", "seler", "rukola"]
}

for store, product in grocery_list.items():
    print(f"Idę do {store} i kupuję tam {product}")

