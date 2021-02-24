import random

def main():
    circle=1
    workers = create_list()
    while circle:
        menu()
        answer=input()
        if answer == "1":
             # for name in workers:
             #     print(name,workers)
             print(workers)
        elif answer == "2":
            add_elem(workers)
        elif answer == "3":
            delete_elem(workers)
        elif answer == "4":
            sort_elem(workers)
        elif answer == "5":
            max_d(workers)
        elif answer == "6":
            min_d(workers)
        elif answer == "7":
            print("Спасибо за работу!")
            circle=0


def menu():
    print("------Выберите действие которое хотите сделать------")
    print("1. Вивести список на экран.")
    print("2. Добавить элемент.")
    print("3. Удалить элемент.")
    print("4. Отсортировать по ключу.")
    print("5. Фамилия человека с найбольшей зарплатой.")
    print("6. Мужчина и женщина с найменшей зарплатой.")
    print("7. Выход.")

def create_list():
    list_ = ["F", "M"]
    workers = {
        "Shevchenko": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Khoudoley": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Koushch": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Bondar": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Taran": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Limarenko": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Falchenko": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Mertoko": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Kipelef": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        },
        "Zerpok": {
            "sex": random.choice(list_),
            "salary": random.randrange(6000, 20000, 100)
        }
    }
    return workers

def add_elem(workers):
    print("----Введите новый элемент----")
    print ("Введите фамилию: ")
    surname=input()
    print("Введите стать: ")
    sex = input()
    print("Введите зарплату: ")
    salary = int(input())
    workers[surname]={"sex":sex,"salary":salary}
    print(workers)
    # for name in workers:
    #     print(name,workers)

def delete_elem(workers):
    print("----Удаление элемента----")
    print("Введите фамилию человека которого хотите удалить:")
    sur=input()
    del workers[sur]
    print(workers)
    # for name, workers in workers.items():
    #     print(name, workers)  

def sort_elem(workers):
    for name, workers in sorted(workers.items(), key=lambda x: x[0]):
        print(name, workers)

def max_d(workers):
    max_solary=list()
    workers_keys = list(workers.keys())
    for item in workers_keys:
       max_solary.append(workers[item]["salary"])
    max_s=max(max_solary)
    for item_new in workers:
        if workers[item_new]["salary"] == max_s:
            print("Человек с найбольшей зарплатой: ",item_new)

def min_d(workers):
    min_salary_F = workers.copy()
    min_salary_M = workers.copy()
    min_M = list()
    min_F = list()
    for item_1 in workers:
        if min_salary_M[item_1]["sex"] == "F":
            name=str(item_1)
            del min_salary_M[name]

    for item_2 in workers:
        if min_salary_F[item_2]["sex"] == "M":
            name = str(item_2)
            del min_salary_F[name]

    Keys_list_F=list(min_salary_F.keys())
    Keys_list_M=list(min_salary_M.keys())

    for item_3 in Keys_list_M:
       min_M.append(workers[item_3]["salary"])
    min_sal_M=min(min_M)

    for item_4 in Keys_list_F:
       min_F.append(workers[item_4]["salary"])
    min_sal_F=min(min_F)

    for iteem_new in workers:
        if workers[iteem_new]["salary"] == min_sal_M:
            print("Мужчина с найменшей зарплатой: ",iteem_new)
        elif workers[iteem_new]["salary"] == min_sal_F:
            print("Женщина с найменшей зарплатой: ", iteem_new)


if __name__ == "__main__":
    main()