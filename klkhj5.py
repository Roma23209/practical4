def main():
    try:
        # На вход программе подаётся целое число – количество минут
        total_minutes = int(input())

        if total_minutes < 0:
            print("Ошибка: количество минут не может быть отрицательным.")
            return

        # Расчет часов и оставшихся минут (в 1 часе = 60 минут)
        hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        # Вывод текста в строгом соответствии с шаблоном задачи
        print(f"{total_minutes} минуты - это {hours} час {remaining_minutes} минут.")

    except ValueError:
        print("Ошибка: входные данные должны быть целым числом.")


if __name__ == "__main__":
    main()
