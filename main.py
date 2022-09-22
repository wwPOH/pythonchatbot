while True:
 chat=input()
 if 'Привіт' in chat or 'Хай' in chat or 'Доброго дня' in chat:
  print(" Доброго вечора, я бот з України! ")
 elif 'Як справи?' in chat or 'Що робиш?' in chat or 'Чим займаєшся?' in chat:
  print(" Вчусь програмувати на Python!")
 elif 'Фільм' in chat or 'Кінотеатр' in chat or 'Серіал' in chat:
  print(" Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Залізна людина, він просто бомба!")
 elif 'Бувай' in chat or'Гудбай' in chat or 'Надобраніч'  in chat or 'До зустрічі'  in chat:
  print(" Побачимось у мережі, I'll be back.")
  exit(0)
 else :
  print ('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :( ')
