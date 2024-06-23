import psycopg2
import random
import numpy as np
from datetime import datetime, timedelta

from numpy import number
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

AMOUNT_AIRPLANES=200
AMOUNT_PASSENGERES=500
AMOUNT_AIRPORTS=50
AMOUNT_FLIGHTS=0 # заполняется в InsertFlight
AMOUNT_TICKETS=0 # заполняется в InsertFlight
amount_of_baggage=[0,10,20,30]


def equal_distribution(general, scale):
    # Используем нормальное распределение для генерации случайных чисел
    amount = np.random.choice(range(1,general))
    return int(amount)


def normal_distribution_for_airplane():
    # Используем нормальное распределение для генерации случайных чисел
    amount = np.random.normal(loc=15, scale=10)
    amount = max(5, min(25, int(round(amount))))
    return amount
def generate_aircraft_registration():
    # Префиксы для различных стран
    country_prefixes = ['RA', 'TC', 'UR', 'N', 'G', 'F', 'C', 'B', 'A']
    # Буквы и цифры, которые могут использоваться в номере
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Выбор случайного префикса для страны
    prefix = random.choice(country_prefixes)

    # Генерация случайного номера самолета (5-7 символов)
    aircraft_number = ''.join(random.choices(characters, k=random.randint(5, 7)))

    # Сборка итогового номера
    registration_number = prefix + aircraft_number

    return registration_number



#last_names =["Калугин","Гусева","Савенко","Кондраев","Тимофеев","Рябинин","Орлов","Филонов","Олейник",
#             "Важенина","Гуй","Нгуен","Доан","Черданцев","Брезгина","Турбина","Попов",
#             "Галкин","Пугачева","Моргернштерн","Дудь","Мартиросян","Ургант","Лебедев"]

last_names = ["Иванов", "Garcia", "Смирнов", "Lee", "Попов", "Thompson", "Кузнецов", "Hall", "Соколов", "Brown", "Петров", "Мартинес", "Волков", "Lewis", "Новиков", "Тарасов", "Миллер", "Семёнов", "Комаров", "Гарсия", "Виноградов", "Родригес", "Богданов", "Макаров", "Климов", "Taylor", "Орлов", "Шмидт", "Беляев", "Джонс"]

# Самые популярные имена
first_names = [
    'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Анна', 'Елена', 'Ольга', 'Наталья',
    'Михаил', 'Иван', 'Евгений', 'Татьяна', 'Мария', 'Ирина', 'Владимир', 'Олег',
    'Павел', 'Максим', 'Екатерина', 'Алексей', 'Николай', 'Виктор', 'Юлия', 'Галина',
    'Валентин', 'Валерий', 'Александра', 'Евгения', 'Григорий', 'Лариса','Августина'
]

# Самые популярные отчества
middle_names = [
    'Александрович', 'Сергеевич', 'Андреевич', 'Дмитриевич', 'Алексеевич', 'Михайлович',
    'Иванович', 'Евгеньевич', 'Павлович', 'Максимович', 'Николаевич', 'Владимирович',
    'Георгиевич', 'Денисович', 'Анатольевич', 'Олегович', 'Станиславович', 'Романович',
    'Валерьевич', 'Викторович', 'Григорьевич', 'Семенович', 'Николаевна', 'Владимировна',
    'Александровна', 'Андреевна', 'Михайловна', 'Сергеевна', 'Евгеньевна', 'Олеговна'
]
passport_series = ['{:04d}'.format(random.randint(0, 9999)) for _ in range(30)]

passport_numbers = ['{:07d}'.format(random.randint(0, 9999999)) for _ in range(30)]

airplane_models = ['Boeing 747' ,'Airbus A380','Airbus A350','Airbus A220','Embraer E175','Airbus A320neo']

general_wieght_baggage = ['500','1000','2000','5000','10000','20000']


date_of_birth = ['{:02d}-{:02d}-{:04d}'.format(
    random.randint(1, 28),  # День
    random.randint(1, 12),  # Месяц
    random.randint(1900, 2023)  # Год
) for _ in range(30)]


airport_country_pairs = [
    ("Шереметьево", "Россия"), ("Домодедово", "Россия"), ("Внуково", "Россия"), ("Пулково", "Россия"),
    ("Толмачёво", "Россия"), ("Кольцово", "Россия"), ("Жуковский", "Россия"), ("Курумоч", "Россия"),
    ("Борисполь", "Украина"), ("Жуляны", "Украина"), ("Торонто", "Канада"), ("Куала-Лумпур", "Малайзия"),
    ("Дубай", "ОАЭ"), ("Хитроу", "Великобритания"), ("Франкфурт", "Германия"), ("Нарита", "Япония"),
    ("Бен-Гурион", "Израиль"), ("Шанхай Пудонг", "Китай"), ("Инчхон", "Южная Корея"),
    ("Сингапур Чанги", "Сингапур"), ("Лос-Анджелес", "США"), ("Ататюрк", "Турция"), ("Делли", "Индия"),
    ("Сидней", "Австралия"), ("Орландо", "США"), ("Гонконг", "Гонконг"), ("Фукуока", "Япония"),
    ("Даллас/Форт-Уэрт", "США"), ("Амстердам Схипхол", "Нидерланды"), ("Бангкок Суварнабхуми", "Таиланд"),
    ("Мюнхен", "Германия"), ("Грибочки", "Россия"),("Ягодки", "Папуа Новая Гвинея"),("Сеул Инчхон", "Южная Корея"), ("Макао", "Макао"), ("Париж Шарль-де-Голль", "Франция"),
    ("Феникс Скай-Харбор", "США"), ("Джон Ф. Кеннеди", "США"), ("Хонолулу", "США"), ("Минск 2", "Беларусь"),
    ("Лиссабон Портела", "Португалия"), ("Хьюстон Джорджа Буша", "США"), ("Барселона Эль Прат", "Испания"),
    ("Стамбул", "Турция"), ("Каир", "Египет"), ("Анталья", "Турция"), ("Берлин Шёнеберг", "Германия"),
    ("Женева", "Швейцария"), ("Венеция Марко Поло", "Италия"), ("Амстердам Схипхол", "Нидерланды")
]

class_of_service = ['Эконом','Премиум-эконом','Комфорт','Бизнес','Первый']


def generate_datetime_pair():
    # Генерируем случайную дату и время для первого момента
    start_date = datetime(1904, 1, 1)
    end_date = datetime(2123, 12, 31)
    delta = end_date - start_date
    random_date1 = start_date + timedelta(days=random.randint(0, delta.days),
                                          hours=random.randint(0, 23),
                                          minutes=random.randint(0, 59),
                                          seconds=random.randint(0, 59))

    # Генерируем случайное время от 5 минут до 24 часов
    delta_time = timedelta(minutes=random.randint(5, 24 * 60), seconds=random.randint(0, 59))

    # Вычисляем второй момент времени
    random_date2 = random_date1 + delta_time

    # Преобразуем дату и время в строки с нужным форматом
    date_time_format = "%Y-%m-%d %H:%M:%S"
    date_time_str1 = random_date1.strftime(date_time_format)
    date_time_str2 = random_date2.strftime(date_time_format)

    return (date_time_str1, date_time_str2)





def Connect():
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="7052018",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="airtransport") #  подключились к бд
    cursor = connection.cursor() # возвращает объект подключения
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

    cursor.execute("TRUNCATE TABLE passenger CASCADE; "
                   "TRUNCATE TABLE ticket CASCADE; "
                   "TRUNCATE TABLE route_segment CASCADE;"
                   "TRUNCATE TABLE class_of_service CASCADE;"
                   "TRUNCATE TABLE flight_final_set CASCADE;"
                   "TRUNCATE TABLE seat CASCADE;"
                   "TRUNCATE TABLE class_of_service_airplane CASCADE;"
                   "TRUNCATE TABLE airplane  CASCADE;"
                   "TRUNCATE TABLE airplane_flight  CASCADE;"
                   "TRUNCATE TABLE flight CASCADE ;"
                   "TRUNCATE TABLE airport CASCADE;"
                   "TRUNCATE TABLE passenger RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE ticket RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE route_segment RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE class_of_service RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE flight_final_set RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE seat RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE class_of_service_airplane RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE airplane RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE airplane_flight RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE flight RESTART IDENTITY CASCADE;"
                   "TRUNCATE TABLE airport RESTART IDENTITY CASCADE;"

                   )
    connection.commit()

    for i in range(AMOUNT_PASSENGERES): # заполняем пассажиров
        cursor.execute("INSERT INTO passenger "
                       "(last_name, first_name, middle_name, passport_series, passport_number, date_of_birth) "
                       "VALUES (%s, %s, %s, %s, %s, %s)",
                       (
                           last_names[random.randint(0, len(last_names) - 1)],  # Фамилия
                           first_names[random.randint(0, len(first_names) - 1)],  # Имя
                           middle_names[random.randint(0, len(middle_names) - 1)],  # Отчество
                           passport_series[random.randint(0, len(passport_series) - 1)],  # Серия паспорта
                           passport_numbers[random.randint(0, len(passport_numbers) - 1)],  # Номер паспорта
                           date_of_birth[random.randint(0, len(date_of_birth) - 1)]  # Дата рождения
                       )
                       )

    for i in range(AMOUNT_AIRPLANES):# самолеты
        cursor.execute("INSERT INTO airplane "
                       "(model, registration_number, number_of_baggage) "
                       "VALUES (%s, %s, %s)",
                       (
                           airplane_models[random.randint(0, len(airplane_models) - 1)],  # модель
                           generate_aircraft_registration(),  # номер
                           general_wieght_baggage[random.randint(0, len(general_wieght_baggage) - 1)],  # багаж

                       )
                       )
        connection.commit()

    for airport, country in airport_country_pairs:   # аэропорты
        cursor.execute("INSERT INTO airport (name_airport, country) VALUES (%s, %s)", (airport, country))

    for class_ in class_of_service: #классы обслуживания
        cursor.execute("INSERT INTO class_of_service (name_class) VALUES (%s)", (class_,))


    #2



    #билеты
    for i in range(AMOUNT_PASSENGERES):
        for _ in range(equal_distribution(50,10)):
            global AMOUNT_TICKETS
            AMOUNT_TICKETS+=1
            cursor.execute(
                "INSERT INTO ticket (passenger_id) "
                "VALUES (%s)",
                (i+1,)
            )

       #места и классы
    def insertIntoSeat(n,i,j):

        cursor.execute(
            "INSERT INTO seat (class_of_service_id,airplane_id,number_of_seat) "
            "VALUES (%s,%s,%s)",
            (random_indices_classe_sorted[n]+1, i+1, seat_names[j])
        )

    def insertIntoClasses_Airplanes(air, cls):
        cursor.execute(
            "INSERT INTO class_of_service_airplane (airplane_id,class_of_service_id) "
            "VALUES (%s,%s)",
            (air+1,cls+1)
        )
    amount_seats_list=[20,AMOUNT_AIRPORTS,150,400]
    amount_classes_list=[1,2,3]
    seat_names=[str(i)+j for i in range(1, 100) for j in ('a','b','c','d','e','f')]
    for i  in range(AMOUNT_AIRPLANES):
        amount_classes=amount_classes_list[random.randint(0,len(amount_classes_list)-1)]
        amount_seats = amount_seats_list[random.randint(0, len(amount_seats_list) - 1)]
        random_indices_classe_sorted = random.sample(range(len(class_of_service)), amount_classes)
        random_indices_classe_sorted.sort()
        names_classes_in_airplane = [class_of_service[i] for i in random_indices_classe_sorted]
        if amount_classes==1:
            for j in range(0,amount_seats):
                insertIntoSeat(0, i, j)
            insertIntoClasses_Airplanes(i,random_indices_classe_sorted[0])
        if amount_classes == 2:
            for j in range(0,int(0.8*amount_seats)):
                insertIntoSeat(0, i, j)
            for j in range(int(0.8*amount_seats),amount_seats):
                insertIntoSeat(1, i, j)
            insertIntoClasses_Airplanes(i, random_indices_classe_sorted[0])
            insertIntoClasses_Airplanes(i, random_indices_classe_sorted[1])
        if amount_classes == 3:
            for j in range(0, int(0.75 * amount_seats)):
                insertIntoSeat(0, i, j)
            for j in range(int(0.75 * amount_seats), int(0.9 * amount_seats)):
                insertIntoSeat(1, i, j)
            for j in range(int(0.9 * amount_seats) , amount_seats):
                insertIntoSeat(2, i, j)
            insertIntoClasses_Airplanes(i, random_indices_classe_sorted[0])
            insertIntoClasses_Airplanes(i, random_indices_classe_sorted[1])
            insertIntoClasses_Airplanes(i, random_indices_classe_sorted[2])




    #3
    # Самолет_рейс              и рейс

    # Рейсы
    def insertFlight():
        global AMOUNT_FLIGHTS
        AMOUNT_FLIGHTS += 1
        i1 = random.randint(1, AMOUNT_AIRPORTS)
        i_ = random.randint(1, AMOUNT_AIRPORTS)
        i2 = i1 + 1 if i1 == i_ else i_
        if i2 == 51:
            i2 = i1 - 1;
        date1, date2 = generate_datetime_pair()
        cursor.execute(
            "INSERT INTO flight (airport_flight_id, airport_of_landing_id, date_and_time_flight, date_and_time_landing) "
            "VALUES (%s, %s, %s, %s)",
            (i1, i2, date1, date2)
        )

    current_flight=0
    for i in range(AMOUNT_AIRPLANES):
        amount_flight=normal_distribution_for_airplane()

        for _ in range(amount_flight):
            insertFlight()
            current_flight+=1
            cursor.execute(
                "INSERT INTO airplane_flight (airplane_id,flight_id) "
                "VALUES (%s,%s)",
                (i + 1, current_flight)
            )




    counter_flight_final_set=0
    # рейс фианлбный набор и сегмент маршрута:
    for i in range(AMOUNT_TICKETS):
        amount_segment_for_ticket= random.randint(1,6)
        for _ in range(amount_segment_for_ticket):
            random_flight=0
            while 1==1:
                random_flight = random.randint(1, AMOUNT_FLIGHTS)
                cursor.execute("""
                                     SELECT s.seat_id, s.class_of_service_id
                                     FROM seat s
                                     JOIN airplane a ON a.airplane_id = s.airplane_id
                                     JOIN airplane_flight af ON af.airplane_id = a.airplane_id
                                     JOIN flight f ON f.flight_id = af.flight_id
                                     WHERE f.flight_id = {}

                                 """.format(random_flight))                                                      # получили места  и классы обслуживания рейса № random_flight
                list_of_pair_seat_class = cursor.fetchall()
                random_pair_seat_class = random.choice(list_of_pair_seat_class)                       # получили случайное место на рейсе

                cursor.execute("""SELECT * FROM flight_final_set WHERE seat_id={} AND flight_id={}
                                                 """.format(random_pair_seat_class[0],random_flight))
                
                if not cursor.fetchall():
                    break

            cursor.execute("""
                             SELECT airport_flight_id,airport_of_landing_id FROM flight
                             WHERE flight.flight_id={}
                         """.format(random_flight))
            random_pair_flight_landing = cursor.fetchall()

            random_amount_of_baggage=random.choice(amount_of_baggage)
            cursor.execute("INSERT INTO flight_final_set (flight_id,seat_id,number_of_baggage) "
            "VALUES (%s,%s,%s)",
            (random_flight,random_pair_seat_class[0], random_amount_of_baggage))
            counter_flight_final_set+=1
            cursor.execute("INSERT INTO route_segment(ticket_id,airport_flight_id,airport_of_landing_id,"
                           "class_of_service_id,flight_final_set_id ,number_of_baggage) "
                           "VALUES (%s,%s,%s,%s,%s,%s)",
                           (i+1, random_pair_flight_landing[0][0], random_pair_flight_landing[0][1],
                            random_pair_seat_class[1],counter_flight_final_set,random_amount_of_baggage))

            print("index of ticket: ", i, "max index ", AMOUNT_TICKETS, "index of flight: ",counter_flight_final_set)
            # Вывод результатов
            # for row in list_of_pair_seat_class:
            #     print("Seat ID:", row[0], "Class of Service ID:", row[1])

    connection.commit()
def main():
    """  free_flights = [i for i in range(10)]
    for _ in range(10):
        k = random.randint(0, len(free_flights)-1)
        free_flights.pop(k)
        print(free_flights)
    """

    Connect()
    list =[i for i in range(0,3)]
    print (list)
    list = [i for i in range(4, 6)]
    print(list)








main()
