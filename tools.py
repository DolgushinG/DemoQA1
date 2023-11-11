import allure


def compare_text(ext, actual):
    with allure.step("Сравнием текст {ext} с {actual}"):
        assert ext == actual, f"Текст {ext} отличается от того что ожидали {actual}"
