import json

def load(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(text, file, indent=5)

def all_zap(text):
    for zapis in text:
        print("=" * 20, f"Номер записи: {zapis['id']}", "=" * 20)
        print(f"Название города: {zapis['name']} \nНазвание страны: {zapis['country']} \nЯвляется ли население города больше 100 000 человек: {zapis['is_big']} \nНаселение города: {zapis['people_count']}")

def zap_pole(text, pole):
    for zapis in text:
        if zapis['id'] == pole:
            return zapis
    return None

def add_zap(text):
    new = {}
    new['id'] = str(max(int(city['id']) for city in text) + 1 if text else "1")
    new['name'] = input("Введите название города: ")
    new['country'] = input("Введите название страны: ")

    while True:
        people_count = input("Введите население города: ")
        if people_count.isdigit():
            new['people_count'] = int(people_count)
            break
        else:
            print("Ошибка: население города должно быть числом.")
    
    new['is_big'] = new['people_count'] > 100000
    text.append(new)
    
    print("Запись добавлена")
    return text

def delete_zap(text, pole):
    for city in text:
        if city['id'] == pole:
            text.remove(city)
            print("Запись удалена")
            return text
    print("Запись не найдена")
    return text

def main():
    filename = "city.json"
    count = 0

    while True:
        print("1. Вывести все записи")
        print("2. Вывести запись по полю")
        print("3. Добавить запись")
        print("4. Удалить запись по полю")
        print("5. Выйти из программы")

        nomer = int(input("Выберите пункт: "))

        if nomer == 1:
            count += 1
            text = load(filename)
            all_zap(text)

        elif nomer == 2:
            count += 1
            pole = input("Введите поле для поиска: ")
            text = load(filename)
            zapis = zap_pole(text, pole)
            if zapis:
                all_zap([zapis])
            else:
                print("Запись не найдена")

        elif nomer == 3:
            count += 1
            text = load(filename)
            text = add_zap(text)
            save(filename, text)

        elif nomer == 4:
            count += 1
            pole = input("Введите поле для удаления: ")
            text = load(filename)
            text = delete_zap(text, pole)
            save(filename, text)

        elif nomer == 5:
            print(f"{count} выполненных операций")
            break

        else:
            print("Нет такого пункта")

main()

