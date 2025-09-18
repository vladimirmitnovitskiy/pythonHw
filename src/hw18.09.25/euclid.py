def fullgcd(a, b):

    #базовый случай 
    if b == 0:
        return a, 1, 0 #возвращаем НОД x и y
        
    else:
        
        gcd, x, y = fullgcd(b, a % b)

        #отматываем действия
        new_x = y

        new_y = x - y * (a // b)

        return gcd, new_x, new_y



print(fullgcd(48,42)) #пример
