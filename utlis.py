import json

def load_students():
    '''
    Загружает и конвертирует в список данные из students.json
    :return: Возвращает список
    '''
    list_students = []
    with open('students.json') as file:
        list_students = json.loads(file.read())

    return list_students


def load_professions():
    '''
    Загружает и конвертирует в список данные из professions.json
    :return: Возвращает список
    '''
    list_professions = []
    with open('professions.json') as file:
        list_professions = json.loads(file.read())

    return list_professions


def get_student_by_pk(pk):
    '''
    Достает нужный словарь из list_students взависимости от ввода юзера
    :param pk: ввод юзера
    :return: словарь нужного студента
    '''
    list_studens = load_students()
    for item in list_studens:
        if item['pk'] == pk:
            return item
    else:
        return False


def get_profession_by_title(title):
    '''
    Достает нужный словарь из list_professions взависимости от ввода юзера
    :param title: ввод юзера
    :return: словарь нужной профессии
    '''
    list_professions = load_professions()
    for item in list_professions:
        if item['title'] == title:
            return item
    else:
        return False

