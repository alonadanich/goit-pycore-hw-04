
def total_salary(salaries):
    try:
        total = 0
        count = 0

        with open("salaries.txt", "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1
        if count == 0:
            return (0, 0)
        average_salary = total / count
        return (total, average_salary)
    except FileNotFoundError:
        print(f"Файл за шляхом {salaries} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") 

