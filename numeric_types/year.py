def year(x):
    if x <= 1582: #в 1582 году страны начали переходить на григорианский календарь
        if x % 4 == 0: 
            return "високосный"
        else:
            return "не високосный"
    else:
        if ((x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)):
            return "високосный"
        else:
            return "не високосный"