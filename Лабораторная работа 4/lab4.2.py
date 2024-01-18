import csv
import json

def convert_csv_to_json(csv_file_path, delimiter=",", newline="\n"):
    try:
        with open(csv_file_path, 'r', newline=newline, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            data = [row for row in reader]

        json_string = json.dumps(data, indent=4, ensure_ascii=False)

        return json_string

    except FileNotFoundError:
        print(f"Файл '{csv_file_path}' не найден.")
        return None
    except csv.Error as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return None


csv_file_path = "путь_к_вашему_файлу.csv"

result = convert_csv_to_json(csv_file_path)

if result is not None:
    print(result)
