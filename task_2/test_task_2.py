from task_2 import count_versions


def test_count_versions():
    # Тест на базовом примере из задачи
    list_version_1 = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]
    expected_result_1 = [['665587', 2, 1], ['669532', 1, 2], ['669537', 2, 1], ['665587', 1, 1]]
    assert count_versions(list_version_1) == expected_result_1

    # Тест на список из одного элемента
    list_version_2 = [['123456', 1]]
    expected_result_2 = [['123456', 1, 1]]
    assert count_versions(list_version_2) == expected_result_2

    # Тест на список с повторяющимися парами
    list_version_3 = [['111', 1], ['222', 2], ['111', 1], ['333', 3], ['222', 2], ['111', 1]]
    expected_result_3 = [['111', 1, 3], ['222', 2, 2], ['333', 3, 1]]
    assert count_versions(list_version_3) == expected_result_3

    # Тест на список с одинаковыми id, но разными version
    list_version_4 = [['111', 1], ['111', 2], ['111', 1], ['111', 1]]
    expected_result_4 = [['111', 1, 3], ['111', 2, 1]]
    assert count_versions(list_version_4) == expected_result_4

    # Тест на список с пустыми данными
    list_version_5 = []
    expected_result_5 = []
    assert count_versions(list_version_5) == expected_result_5

    print("Все тесты успешно пройдены!")


test_count_versions()
