from csv import reader
import xml.dom.minidom as minidom
#ID;Название;Тип;Автор;Автор (ФИО);Возрастное ограничение на книгу;Дата поступления;Цена поступления;Кол-во выдач;Дата списания книги;Инвентарный номер;Выдана до;Жанр книги
def open_table(filename='books.csv'):
    try:
        with open(filename, 'r', encoding='cp1251') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            return table[1:]
    except FileNotFoundError:
        print('ФАЙЛ НЕ НАЙДЕН!!!!!!!')
        return 0


def task1():
    table=open_table()
    nums=0
    for row in table:
        name=row[1]
        if len(name)>30:
            nums+=1
    print(nums)


def task2():
    table=open_table()
    while True:
        line = input('Введите имя автора (0 для выхода): ')
        if line == '0':
            break
        f=True
        visited = []
        for row in table:
            auth = row[4].lower()
            if auth.find(line.lower()) != -1:
                if row[1] not in visited:
                    print(f'{row[1]} - {row[4]}')
                    visited.append(row[1])
                f=False
        if f:
            print('Ничего не найдено!')
        print()


def task3():
    table = open_table()[:20]
    file=open('journal.txt', 'w')
    for row in enumerate(table, start=1):
        line = f'{row[1][3]}. {row[1][1]} - {row[1][6][6:10]}'
        print(line)
        file.write(f'{row[0]}. {line}\n')
    file.close()



def task4():
    char_cods=[]
    values=[]
    xml_file = open('currency.xml', encoding='cp1251')
    xml_data = xml_file.read()
    dom = minidom.parseString(xml_data)
    dom.normalize()
    nodes = dom.getElementsByTagName('CharCode')
    for node in nodes:
        char_cods.append(node.firstChild.data)
    nodes=dom.getElementsByTagName('Value')
    for node in nodes:
        values.append(node.firstChild.data)

    print(char_cods)
    print(values)


def task5():
    table = open_table('books-en.csv')
    tags=set()
    for row in table:
        tags.add(row[4])
    for i in tags:
        print(i)

def task6():
    table=open_table()
    books=[]
    for row in table:
        if [row[1], int(row[8])] not in books:
            books.append([row[1], int(row[8])])
    books.sort(key=lambda x: -x[1])
    for n,i in enumerate(books[:20], start=1):
        print(f'{n}. {i[0]} - {i[1]} выдач')
task6()
