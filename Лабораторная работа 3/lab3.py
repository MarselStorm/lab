def find_first_occurrence(products, target_product):
    for index, product in enumerate(products):
        if product == target_product:
            return index
    return None


product_list = ["item1", "item2", "item3", "item1", "item4",  "item5"]
target_item = "item3"

result = find_first_occurrence(product_list, target_item)

if result is not None:
    print(f"Индекс первого вхождения товара '{target_item}': {result}")
else:
    print(f"Товар '{target_item}' не найден в списке.")
