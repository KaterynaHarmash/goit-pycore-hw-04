
from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)

    if not file_path.is_absolute():
        file_path = Path(__file__).parent / file_path

    cats_info = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cats_info.append({
                        "id": id,
                        "name": name,
                        "age": int(age) 
                    })
                except (ValueError, IndexError):
                    print(f"Невірний формат рядка: {line.strip()}")

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")

    return cats_info


result = get_cats_info(r"A:\Github\goit-pycore-hw-04\get_cats_info\cats_info.txt")
print("Інформація про котів:", result)