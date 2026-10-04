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

def main():
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()