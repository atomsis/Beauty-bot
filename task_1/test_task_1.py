from task_1 import validate_text


def test_validate_text():
    # Тест на корректный текст
    test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services', 'record_link']
    print('test1')
    assert validate_text(test_text, list_keys) == "Тест пройден"

    # Тест на некорректный ключ
    test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {invalid_key}
Услуги:
{services}
управление записью {record_link}'''
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services', 'record_link']
    print('test2')
    assert validate_text(test_text, list_keys) == "Ошибка: некорректный ключ 'invalid_key'"

    # Тест на несбалансированные скобки
    test_text = '''{name, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services', 'record_link']
    print('test3')
    assert validate_text(test_text, list_keys) == "Ошибка: несбалансированные фигурные скобки"

    # Тест на отсутствие закрывающей скобки
    test_text = '''{name, ваша запись изменена:
⌚️ {day_month в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services', 'record_link']
    print('test4')
    assert validate_text(test_text, list_keys) == "Ошибка: несбалансированные фигурные скобки"

    print("Все тесты успешно пройдены!")


test_validate_text()
