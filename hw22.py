
def get_cats_info(cats):
    cats_info = []
    try:
        with open("cats.txt", "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age}
                cats_info.append(cat_info)
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {cats} не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []
    
cats_info = get_cats_info("cats.txt")

print(cats_info)

