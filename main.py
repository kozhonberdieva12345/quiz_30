import csv

score = 0

with open('sfs.csv', newline='') as sfs:
  reader = csv.reader(sfs, delimiter=";")
  for row in reader:
    print(row[0])
    print(row[1], row[2], row[3])
    us = input("Выберите вариант ответа(a, b, c): ")

    if us == 'a':
      if row[1] == row[4]:
        score += 5
        print("Правильно!")
      else:
        print("Неправильно")
    elif us == 'b':
      if row[2] == row[4]:
        score += 5
        print("Правильно!")
      else:
        print("Неправильно")
    elif us == 'c':
      if row[3] == row[4]:
        score += 5
        print("Правильно!")
      else:
        print("Неправильно")
    else:
      print("Такого ответа нет")

print("Вы заработали " + str(score) + " баллов")

if score == 100:
  print("Ваша оценка A")
elif score >= 95:
  print("Ваша оценка A-")
elif score >= 90:
  print("Ваша оценка B+")
elif score >= 85:
  print("Ваша оценка B")
elif score >= 80:
  print("Ваша оценка B-")
elif score >= 75:
  print("Ваша оценка C+")
elif score >= 70:
  print("Ваша оценка C")
elif score >= 65:
  print("Ваша оценка C-")
elif score >= 60:
  print("Ваша оценка D")
else:
  print("Ваша оценка F")