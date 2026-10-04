tasks = []

def add_task():
    text = input("Введите текст задачи: ").strip()
    if text:
        tasks.append(text)
        print("Задача добавлена.")
    else:
        print("Пустая задача не добавлена.")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Введите номер задачи для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Задача «{removed}» удалена.")
        else:
            print("Задачи с таким номером нет.")
    except ValueError:
        print("Нужно ввести число.")

def main():
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()