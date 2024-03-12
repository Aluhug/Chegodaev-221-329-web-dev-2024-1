import subprocess
import pytest

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

    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],

    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['-3', '7'], ['Error!'])
    ],

    'division': [
        (['3', '5'], ['0', '0.6']),
        (['8', '0'], ['Error!']),
        (['7', '3'], ['2', '2.3333333333333335'])
    ],

    'loops': [
        (['5'], ['0', '1', '4', '9', '16']),
        (['1'], ['0']),
        (['20'], ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81', '100', '121', '144', '169', '196', '225', '256', '289', '324', '361']),
        (['30'], ['Error!'])
    ],

    'print_function': [
        (['10'], '12345678910'),
        (['1'], '123'),
        (['20'], '1234567891011121314151617181920'),
        (['30'], 'Error!')
    ],

    'second_score': [
        (['5', '2 3 6 6 5'], '5'),
        (['6', '10 5 8 7 9 6'], '9'),
        (['4', '1 1 3 1'], '1')
    ],

    'nested_list': [
        (['5', 'Harry', '37.21', 'Berry', '37.21', 'Tina', '37.2', 'Akriti', '41', 'Harsh', '39'], 'Berry\nHarry'),
        (['3', 'Alice', '50', 'Bob', '45', 'Charlie', '55'], 'Alice'),
        (['2', 'Alex', '80', 'Brian', '75'], 'Alex')
    ],

    'lists': [
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], ['[1, 3, 2]']),
        (['10', 'append 4', 'insert 0 5', 'insert 2 6', 'print', 'remove 5', 'insert 0 99', 'sort', 'print', 'reverse', 'print'], ['[5, 4, 6]', '[4, 6, 99]', '[99, 6, 4]']),
        (['5', 'insert 0 3', 'insert 0 2', 'print', 'pop', 'print'], ['[2, 3]', '[2]'])
    ],

    'swap_case': [
    (['qwerty ZXCVBN123456 wprgoh'], ['QWERTY zxcvbn123456 WPRGOH']),
    (['АБВГДЕ ЯЮЭ 43е tgh ААБГ'], ['абвгде яюэ 43Е TGH аабг']),
    (['234 3333 0505 0= - 3= 1='], ['234 3333 0505 0= - 3= 1='])
    ],

    'split_and_join': [
    (['123 4 5 6 78 9 0=== === !!'], ['123-4-5-6-78-9-0===-===-!!']),
    (['this is a string а это строка'], ['this-is-a-string-а-это-строка']),
    (['тутпростотекст, я не знаю что писать. Пусть будет. ifrgiojgwroijgjogogj ff ldl gg ggg er r rrrr 5'],
     ['тутпростотекст,-я-не-знаю-что-писать.-Пусть-будет.-ifrgiojgwroijgjogogj-ff-ldl-gg-ggg-er-r-rrrr-5'])
    ],

    'max_word': [
    (['example.txt'], ['сосредоточенности']),
    (['empty_file.txt'], ['']),
    (['short_words.txt'], ['Hello'])
    ], 

    'price_sum': [
        (['products.csv'], ['6842.84 5891.06 6810.90']),
        (['products2.csv'], ['4128.50 3497.94 4185.61']),
        (['products3.csv'], ['1005905.85 5812.15 10113.05'])
    ],

    'anagram': [
    (['listen', 'silent'], 'YES'),
    (['hello', 'world'], 'NO'),
    (['7453', '3475'], 'YES'),
    (['qwertyuiopasdfghjklzxcvbnm', 'mnbvcxzlkjhgfdsapoiuytrewq'], 'YES'),
    (['abcde', 'e d c b a'], 'NO')
    ],

    'metro': [
    (['4', '10 20', '15 25', '30 40', '35 45', '18'], '2'),
    (['3', '5 10', '12 15', '20 25', '8'], '1'),
    (['5', '0 5', '10 15', '20 25', '30 35', '40 45', '23'], '1'),
    (['3', '10 20', '15 25', '30 40', '25'], '1'),
    (['2', '5 10', '15 20', '10'], '1')
    ],

    'minion_game': [
    (['BANANA'], 'Stuart 12'),
    (['EAEAEA'], 'Kevin 21'),
    (['BCDFGHJ'], 'Stuart 28'),
    (['BAA'], 'Ничья!')
    ],

    'is_leap': [
    (['2000'], 'True'),
    (['2100'], 'False'),
    (['2096'], 'True'),
    (['1'], 'Error!'),
    (['2000000'], 'Error!')
    ],

    'happiness': [
    (['3 2', '1 5 3', '3 1', '5 7'], '1'),
    (['4 3', '10 20 30 40', '15 20 25', '30 40 50'], '-1'),
    (['5 2', '1 2 3 4 5', '1 3', '2 4'], '0'),
    (['3 2', '2 4 6', '1 3', '5 7'], '0'),
    (['0 0', '2 4 6', '1 3', '5 7'], 'Error!')
    ],

    'pirate_ship': [
    (['20 4', 'gold 5 100', 'silver 7 80', 'diamond 2 120', 'copper 10 50'], ['diamond 2.00 120', 'gold 5.00 100', 'silver 7.00 80', 'copper 6.00 30.0']),
    (['15 3', 'rum 8 30', 'food 6 40', 'water 10 20'], ['food 6.00 40', 'rum 8.00 30', 'water 1.00 2.0']),
    (['25 5', 'gunpowder 12 90', 'clothes 8 50', 'spices 5 30', 'wood 15 10', 'tea 3 60'], ['tea 3.00 60', 'gunpowder 12.00 90', 'clothes 8.00 50', 'spices 2.00 12.0'])
    ],

    'matrix_mult': [
    (['2', '1 2', '3 4', '5 6', '7 8'], ['19 22', '43 50']),
    (['3', '2 0 1', '1 3 2', '4 1 3', '2 1 0', '3 2 1', '1 0 2'], ['5 2 2', '13 7 7', '14 6 7']),
    (['2', '2 0', '1 3', '4 1', '2 1'], ['8 2', '10 4']),
]

}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected.split('\n')

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['price_sum'])
def test_price_sum(input_data, expected):
    assert run_script('price_sum.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data) == '\n'.join(expected)
    
@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data) == '\n'.join(expected)