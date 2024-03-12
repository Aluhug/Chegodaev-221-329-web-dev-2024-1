import subprocess
import pytest
from average_scores import average_scores
from complex_numbers import do_complex_operations
from email_validation import filter_mail
from fact import fact_it, fact_rec
from fibonacci import fibonacci
from file_search import file_search
from files_sort import files_sort
from my_sum import my_sum
from people_sort import name_format
from phone_number import sort_phone
from plane_angle import plane_angle, Point
from process_list import process_list, process_list_gen
from show_employee import *
from sum_and_sub import sum_and_sub

INTERPRETER = 'python3'


def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


test_data = {
    'fact': [
        (1, 1),
        (10, 3628800),
        (50, 30414093201713378043612608166064768844377641568960512000000000000)
    ],
    'show_employee': [
        (['Иванов Иван Иванович', '1234556789'], 'Иванов Иван Иванович: 1234556789 Рублей'),
        (['Alex', '100'], 'Alex: 100 Рублей'),
        (['Да'], 'Да: 10000 Рублей'),
        ([''], ': 10000 Рублей')
    ],
    'sum_and_sub': [
        ([0, 0], [0, 0]),
        ([1, 2], [3, -1]),
        ([10, 10], [20, 0]),
        ([-0.123, 5.3], [5.177, -5.423])
    ],
    'process_list': [
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
        ([0, -1, -2, -3, -4, -5], [0, -1, 4, -27, 16, -125]),
        ([0.5, 3.5, -2, 234, -237872874237], [0.125, 42.875, 4, 54756, -13459680801712577166876000228430053])
    ],
    'my_sum': [
        ([0], 0),
        ([1, 2, 3, 4, 5], 15),
        ([1.23, 4.56, 7.89, ], 13.68),
        ([-9.87, -6.54, 3.21], -13.2)
    ],
    'files_sort': [
        ('./files_sort_test/', ['f.js', 'x.py', 'z.py', 'a.txt', 'b.txt', 'c.txt'])
    ],
    'file_search': [
        ('a.txt', '\n'.join(['A', 'B', 'C', 'D', 'E'])),
        ('AAA.py', "Файл AAA.py не найден"),
        ('x.py', "print('Hello world')"),
        ('f.js', "")
    ],
    'email_validation': [
        (['brian-23@mospolytech.ru', 'britts_54@mospolytech.ru', 'lara@mospolytech.ru'],
         ['brian-23@mospolytech.ru', 'britts_54@mospolytech.ru', 'lara@mospolytech.ru']),
        (['lara@mospolytech.ru', '12344556788@@ya.ru'], ['lara@mospolytech.ru']),
        (['123@ya.net1'], []),
        (['123@.ya.net'], []),
        (['1_2_3@-ya.net'], [])
    ],
    'fibonacci': [
        (1, [0]),
        (5, [0, 1, 1, 8, 27]),
        (10, [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304])
    ],
    'average_scores': [
        ([[100.0]], (100.0,)),
        ([[100, 50.5, 11.1]], (100.0, 50.5, 11.1)),
        ([[50, 100], [25, 50], [75, 0]], (50, 50)),
        ([[89, 90, 78, 93, 80], [90, 91, 85, 88, 86], [91, 92, 83, 89, 90.5]], (90.0, 91.0, 82.0, 90.0, 85.5))
    ],
    'phone_number': [
        (['9195969878'], ['+7 (919) 596-98-78']),
        (['07895462130', '89875641230', '9195969878',],
         ['+7 (789) 546-21-30', '+7 (919) 596-98-78', '+7 (987) 564-12-30']),
        (['1234567890'], ['+7 (123) 456-78-90'])
    ],
    'people_sort': [
        ([['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']],
         ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']),
        ([['Mike', 'Thomson', '99', 'M'], ['Robert', 'Bustle', '40', 'M'], ['Andria', 'Bustle', '10', 'F']],
         ['Ms. Andria Bustle', 'Mr. Robert Bustle', 'Mr. Mike Thomson']),
        ([['Robert', 'Bustle', '32', 'F'], ['Andria', 'Bustle', '30', 'F'], ['Mike', 'Thomson', '20', 'F']],
         ['Ms. Mike Thomson', 'Ms. Andria Bustle', 'Ms. Robert Bustle']),
        ([['A', 'AA', '44', 'F'], ['B', 'BB', '55', 'M'], ['C', 'CC', '60', 'M']],
         ['Ms. A AA', 'Mr. B BB', 'Mr. C CC']),
         ([['alex', 'chegodaev', '19', 'M'], ['polina', 'chegodaev', '21', 'F'], ['arseniy', 'chegodaev', '21', 'M'], ['ЛЕХА', 'ЧЕГОДАЕВ', '100', 'M']],
         ['Mr. ЛЕХА ЧЕГОДАЕВ', 'Mr. alex chegodaev', 'Ms. polina chegodaev', 'Mr. arseniy chegodaev'])
    ],
    'plane_angle': [
        ([[1, 1, 0], [1, 3, 1], [0, 0, 1], [0, 0, 2]], 147.69),
        ([[1, 1, 0], [1, 1, 1], [0, 0, 1], [0, 0, 0]], 0.0),
        ([[1, 0, 1], [0, 1, 0], [0, 0, 0], [1, 0, 0]], 45.0),
        ([[0, 3.5, 1], [0, 1, -7], [1, 20, 0], [10, 1, 1]], 54.87),
        ([[2, 2, 1], [0, 1, 3], [1, 2, 0], [5, 2, 1]], 9.9)
    ],
    'complex_numbers': [
        (['2 1', '5 6'], ['7.00+7.00i', '-3.00-5.00i', '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i']),
        (['1 2', '3 4'], ['4.00+6.00i', '-2.00-2.00i', '-5.00+10.00i', '0.44+0.08i', '2.24+0.00i', '5.00+0.00i']),
        (['1 0', '0 -1'], ['1.00-1.00i', '1.00+1.00i', '0.00-1.00i', '0.00+1.00i', '1.00+0.00i', '1.00+0.00i']),
        (['1.5 2.5', '3 -5'], ['4.50-2.50i', '-1.50+7.50i', '17.00+0.00i', '-0.24+0.44i', '2.92+0.00i', '5.83+0.00i'])
    ]
}


@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list(input_data, expected):
    assert process_list(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_gen(input_data, expected):
    assert process_list_gen(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    assert files_sort(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    assert file_search(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    assert filter_mail(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert fibonacci(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['average_scores'])
def test_average_scores(input_data, expected):
    assert average_scores(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['phone_number'])
def test_phone_number(input_data, expected):
    assert sort_phone(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['people_sort'])
def test_people_sort(input_data, expected):
    assert name_format(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    data = [Point(*map(float, input)) for input in input_data]
    assert plane_angle(*data) == expected



@ pytest.mark.parametrize("input_data, expected", test_data['complex_numbers'])
def test_complex_numbers(input_data, expected):
    assert do_complex_operations(*input_data) == expected