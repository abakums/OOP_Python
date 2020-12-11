def hit(type_hit):
    """Декоратор, возвращающий информацию об атаке бойца и остатке здоровья его соперника"""
    def outer(func):
        def wrapper(*args, **kwargs):
            result = "Попытка выполнить {0}\n".format(type_hit)
            result += func(*args, **kwargs)
            if args[0].health <= 0 and args[1].health <= 0:
                result += "\nБоевая ничья!\n\n"
            elif args[1].health <= 0:
                result += "\nВ этом бою проиграл {0}| у бойца {1} остаток здоровья: {2}\n\n"\
                    .format(args[1], args[0], args[0].health)
            return result
        return wrapper
    return outer


def verify_weight(func):
    def wrapper(*args, **kwargs):
        if args[1] > 300 or args[1] < 40:
            print("Некорректный вес бойца! Стоит проверить весы на неполадки.")
        else:
            func(*args, **kwargs)
    return wrapper


def verify_age(func):
    def wrapper(*args, **kwargs):
        if args[1] in range(8, 61):
            func(*args, **kwargs)
        else:
            print("Некорректный возраст бойца!")
    return wrapper
