s = "This is (a test) of the (emergency) broadcast system" # вводим строку со скобками
while "(" in s: # пока есть открывающая скобка в строке
  i = s.find("(") # находим индекс открывающей скобки
  j = s.find(")") # находим индекс закрывающей скобки
  s = s[:i] + s[j+1:] # удаляем скобки и все, что между ними
print(s) # выводим результат
