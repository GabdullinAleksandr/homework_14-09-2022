import utlis

def check_fitness(student,profession):
    '''
    Проводит проверку пригодности студента, сравнивая скилы из словарей
    :param student: номер студента из файла students.json
    :param profession: профессия из файла professions.json
    :return: итоговый словарь с данными для вывода
    '''
    dict_student = utlis.get_student_by_pk(student)
    dict_profession = utlis.get_profession_by_title(profession)
    student_skills = set(list(dict_student['skills']))
    profession_skills = set(list(dict_profession['skills']))
    final_dict = {}
    final_dict['has'] = list(student_skills.intersection(profession_skills))
    final_dict['lacks'] = list(profession_skills.difference(student_skills))
    final_dict['fit_percent'] = int((len(list(student_skills.intersection(profession_skills))) * 100 / (
        len(list(dict_profession['skills'])))))
    return final_dict


def main():
    '''
    Основная функция
    '''
    try:
        user_input = int(input(f'Программа: Введите номер студента\nПользователь: '))
        dict_student = utlis.get_student_by_pk(user_input)
        if dict_student == False:
            print('Программа: У Вас нет такого студента')
            quit()
        else:
            student_name = dict_student['full_name']
            student_skills = ', '.join(dict_student['skills'])
            print(f'Программа: Студент {student_name}\nПрограмма: Знает: {student_skills}')
        user_input2 = input(f'Программа: Выберите специальность для оценки студента {student_name} - ')
        dict_profession = utlis.get_profession_by_title(user_input2)
        if user_input2 == False:
            print('Программа: У Вас нет такой специальности')
            quit()
        else:
            final_dict = check_fitness(user_input, user_input2)
            has = ', '.join(final_dict['has'])
            lacks = ', '.join(final_dict['lacks'])
            print(f'Программа: Пригодность {final_dict["fit_percent"]}%')
            print(f'Программа: {student_name} знает {has}' if len(has) != 0
                  else f'Программа: {student_name} не знает нужных языков')
            print(f'Программа: {student_name} не знает {lacks}' if len(lacks) != 0
                  else f'Программа: {student_name} знает все требуемые языки')
    except:
        print('incorrect input')


main()
