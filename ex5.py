week = int(input("Введіть номер тижня (1 - за чисельником, 2 - за знаменником): "))
day = int(input("Введіть день тижня: "))
one_week_schedule = {
    1: "Понеділок: Операційні системи, Комп'ютерні мережі, Комп'ютерні мережі, Спеціалізоване прикладне програмування",
    2: "Вівторок: Розробка клієнт-серверних застосунків, Операційні системи, Web-розробка та web-дизайн",
    3: "Середа: Розробка клієнт-серверних застосунків, Web-розробка та web-дизайн, Web-розробка та web-дизайн",
    4: "Четвер: Спеціалізоване прикладне програмування, Технологія створення програного продукту, Розробка клієнт-серверних застосунків",
    5: "П'ятниця: Розробка клієнт-серверних застосунків, Технологія створення програного продукту",
}
two_week_schedule = {
     1: "Понеділок: Операційні системи, Комп'ютерні мережі, Комп'ютерні мережі, Спеціалізоване прикладне програмування",
    2: "Вівторок: Розробка клієнт-серверних застосунків, Web-розробка та web-дизайн, Web-розробка та web-дизайн",
    3: "Середа: Розробка клієнт-серверних застосунків, Web-розробка та web-дизайн, Web-розробка та web-дизайн",
    4: "Четвер: Спеціалізоване прикладне програмування, Технологія створення програного продукту, Розробка клієнт-серверних застосунків",
    5: "П'ятниця: Розробка клієнт-серверних застосунків, Технологія створення програного продукту",
}
if week == 1:  
    schedule = one_week_schedule.get(day, "Невірний день тижня")
elif week == 2:  
    schedule = two_week_schedule.get(day, "Невірний день тижня")
else:
    schedule = "Невірний номер тижня"
print(schedule)
