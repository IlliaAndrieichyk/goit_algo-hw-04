def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        total = 0
        count = 0
        
        for line in lines:
            surname, salary = line.strip().split(',')
            total += int(salary)
            count += 1
        
        average = total / count if count != 0 else 0
        
        return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

path_to_file = "path/to/salary_file.txt"
total, average = total_salary(path_to_file)
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
