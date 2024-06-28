def validate_text(test_text, list_keys):
    def check_brackets(text):
        stack = []
        for char in text:
            if char == '{':
                stack.append(char)
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
        return len(stack) == 0

    if not check_brackets(test_text):
        return "Ошибка: несбалансированные фигурные скобки"

    # Максимальная длина ключа из list_keys
    max_key_length = max(len(key) for key in list_keys)

    i = 0
    while i < len(test_text):
        if test_text[i] == '{':
            # Устанавливаем границу поиска закрывающей скобки
            search_limit = min(i + max_key_length + 2, len(test_text))
            end_brace = -1
            for j in range(i + 1, search_limit):
                if test_text[j] == '}':
                    end_brace = j
                    break
            if end_brace == -1:
                return "Ошибка: отсутствует закрывающая фигурная скобка"

            key = test_text[i + 1:end_brace].strip()
            if key not in list_keys:
                return f"Ошибка: некорректный ключ '{key}'"

            i = end_brace
        i += 1

    return "Тест пройден"
