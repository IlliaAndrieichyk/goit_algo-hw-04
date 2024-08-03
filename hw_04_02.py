def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        cats_info = []
        
        for line in lines:
            cat_id, name, age = line.strip().split(',')
            cat_info = {"id": cat_id, "name": name, "age": age}
            cats_info.append(cat_info)
        
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

path_to_file = "path/to/cats_file.txt"
cats_info = get_cats_info(path_to_file)
if cats_info is not None:
    print(cats_info)
