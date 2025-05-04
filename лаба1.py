
def hamming_distance(s, t):
    
    if len(s) != len(t):
        raise ValueError("Строки должны быть одинаковой длины")
    
    distance = 0 
    for char_s, char_t in zip(s, t):  
        if char_s != char_t:  
            distance += 1  
    
    return distance  

# Ввод данных
s = "GAGCCTACTAACGGGAT"  # Первая строка
t = "CATCGTAATGACGGCCT"  # Вторая строка
try:
    distance = hamming_distance(s, t)
    print("Расстояние Хэмминга:", distance)  
except ValueError as e:
    print("Ошибка:", e)  