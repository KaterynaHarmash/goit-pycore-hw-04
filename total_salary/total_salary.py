from pathlib import Path

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    salary = line.strip().split(',')[1]
                    total += int(salary)
                    count += 1
                except (ValueError, IndexError):
                    print(f"Невірний формат рядка: {line.strip()}")

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)

    average = int(total / count) if count > 0 else 0
    return (total, average)


working_directory = Path(__file__).parent
result = total_salary(working_directory / "total_salary.txt")

print(
    f"Загальна сума заробітної плати: {result[0]}, "
    f"Середня заробітна плата: {result[1]}"
)