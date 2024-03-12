import datetime

def function_logger(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(log_file, 'a+') as file:

                file.write(f"{func.__name__}\n") #имя функции

                start_time = datetime.datetime.now() 
                file.write(f"{start_time}\n")#когда вызвана функция

                file.write(f"{args, kwargs}\n") #входящие аргументы

                result = func(*args, **kwargs) #вызов функции

                file.write(f"{result if result is not None else '-'}\n") #выходное значение

                end_time = datetime.datetime.now() #когда закончилась функция
                file.write(f"{end_time}\n")

                elapsed_time = end_time - start_time
                file.write(f"{elapsed_time}\n\n") #сколько работала функция
            return result
        return wrapper
    return decorator


@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'

greeting_format('John')
