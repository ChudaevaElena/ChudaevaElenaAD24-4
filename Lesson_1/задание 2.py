example_str = 'В строке, есть, ошибка, снова ошибка.'
modified_str = example_str.replace(',', '.')
two_str = modified_str.replace('ошибка', 'исправление')
print(two_str)