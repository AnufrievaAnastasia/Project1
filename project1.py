# Фитнес калькулятор для девушек
# Рассчет затрат калорий на выполнение стандартных физических упражнений
# Определение ИМТ
# Рассчет идеального веса в соответствии с параметрами
# Рассчет необходимого количества калорий в сутки
print("Укажите Ваш вес в килограммах:")
weight = float(input())
print("Укажите Ваш рост в см:")
cm = float(input())
growth = cm / 100
print("Укажите Ваш возраст:")
years = int(input())
print("Укажите время, потраченное на тренировку, в минутах:")
minutes = float(input())
hours = minutes / 60
rope = weight * 7.2 * hours
print("Прыжки на скакалке:", ('{:.2f}'.format(rope)))
bike1 = weight * 2 * hours
print("Велотренажёр со скоростью 3.5 км/ч:", ('{:.2f}'.format(bike1)))
bike2 = weight * 4.26 * hours
print("Велотренажере со скоростью 10 км/ч:", ('{:.2f}'.format(bike2)))
ellipse = 12 * weight * hours
print("Тренировка на эллиптическом тренажере:", ('{:.2f}'.format(ellipse)))
walking = 4.2 * weight * hours
print("Ходьба на беговой дорожке:", ('{:.2f}'.format(walking)))
run1 = 7 * weight * hours
print("Бег средний с остановками:", ('{:.2f}'.format(run1)))
run2 = 8.4 * weight * hours
print("Быстрый бег:", ('{:.2f}'.format(run2)))
dancing = 5.2 * weight * hours
print("Современные танцы:", ('{:.2f}'.format(dancing)))
pilate = 4 * weight * hours
print("Пилатес:", ('{:.2f}'.format(pilate)))
yoga = 3.2 * weight * hours
print("Йога:", ('{:.2f}'.format(yoga)))
BMI = (weight / growth ** 2)
print("Индекс массы Вашего тела равен:", ('{:.2f}'.format(BMI)))
ideal_weight = (cm - 110) * 1.15
print("Ваш идеальный вес (формула Лоренца):", ('{:.2f}'.format(ideal_weight)))
ideal_weight2 = 0.713 * cm - 49
print("Ваш идеальный вес (формула Купера):", ('{:.2f}'.format(ideal_weight2)))
kilo = 593 + (9.247 * weight) + (3.098 * cm) - (4.33 * years)
print("Необходимое количество калорий в сутки:", ('{:.2f}'.format(kilo)))
