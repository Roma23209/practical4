def main():
    try:
        number = int(input())
        if not (1000 <= number <= 9999):
            print("Ошибка: число должно быть четырёхзначным.")
            return
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        units = number % 10
        print(f"Цифра в позиции тысяч равна {thousands}")
        print(f"Цифра в позиции сотен равна {hundreds}")
        print(f"Цифра в позиции десятков равна {tens}")
        print(f"Цифра в позиции единиц равна {units}")
    except ValueError:
        print("Ошибка: введено не целое число.")
if __name__ == "__main__":
    main()
