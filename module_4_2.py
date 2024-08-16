def  test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        #inntr_function() # ни чего не возвращает


#inntr_function() # выдаёт ошибку :NameError: name 'inntr_function' is not defined. Did you mean: 'test_function'?
# (Ошибка NameError: имя "внутренняя функция" не определено. Вы имели в виду "тестовая функция"?)
test_function() # так работает
