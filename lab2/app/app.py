from flask import Flask, render_template, request, make_response
from operator import add, sub, mul, truediv

app = Flask(__name__)
application = app
operations = {'+': add, '-': sub, '*': mul, '/': truediv}

@app.route('/args')
def args():
    return render_template('args.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/')
def index():
    url = request.url
    return render_template('index.html', url=url)

@app.route('/cookies')
def cookies():
    response = make_response()
    if "Supersecretcookie" in request.cookies:
        response.delete_cookie("Supersecretcookie")
    else:
        response.set_cookie("Supersecretcookie", "1")
    response.set_data(render_template('cookies.html'))
    return response

@app.route('/form', methods=['GET', 'POST'])

def form():
    return render_template('form.html')

@app.route('/calc', methods=['GET', 'POST'])

def calc():
    error = ""
    result = ""
    if request.method == "POST":
        try:
            num1 = request.form.get("num1", '0')
            num2 = request.form.get("num2", '0')
            operation = request.form.get("operation", '')
            num1, num2 = list(map(int, (num1, num2)))
            result = operations[operation](num1, num2)
        except ZeroDivisionError:
            error = "Нельзя делить на ноль!"
        except ValueError:
            error = "Введены неверные числа!"
        except KeyError:
            error = "Данная операция не поддерживается!"
        except Exception as e:
            error = f"Неизвестная ошибка: {e}!"
    return render_template('calc.html', error=error, result=result, operations=operations.keys())

@app.route('/phone', methods=['GET', 'POST'])


def phone():
    if request.method == 'GET':
        return render_template('phone.html')
    result = ""
    error = ""
    try:
        num = request.form.get("num", '0')
        cleaned_num = ''.join(filter(str.isdigit, num))
        if not all(char.isdigit() or char in '+()-. ' for char in num):
            raise ValueError("Введены недопустимые символы!")
            
        if len(cleaned_num) not in (10, 11):
            raise ValueError("Введено неверное количество цифр!")

        formatted_phone_num = '8-{}-{}-{}-{}'.format(cleaned_num[-10:-7], cleaned_num[-7:-4], cleaned_num[-4:-2], cleaned_num[-2:])
        result = formatted_phone_num

    except ValueError as e:
        error = str(e)
    except Exception as e:
        error = f"Неизвестная ошибка: {e}!"

    return render_template('phone.html', error=error, result=result)



