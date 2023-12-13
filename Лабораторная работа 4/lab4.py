import json

def calculate_product_sum(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        product_sum = sum(item["score"] * item["weight"] for item in data)
        rounded_sum = round(product_sum, 3)

        return rounded_sum

    except FileNotFoundError:
        print(f"Файл '{json_file_path}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON в файле '{json_file_path}'.")
        return None

