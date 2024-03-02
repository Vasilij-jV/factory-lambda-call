from termcolor import cprint

# lambda функция
multiplication = lambda a, b: a * b
print(multiplication(a=23, b=67))


def multiplication_func(a, b):
    return a * b


print(multiplication_func(a=10, b=7))


# Вызываемый объект

class Fruits:

    def __init__(self, values):
        self.values = values

    def __call__(self, keys):
        generator_dict = {key: value for key, value in zip(keys, self.values)}
        return generator_dict


key_dict = ['apple', 'orange', 'banana', 'pear']
value_dict = ['red', 'orange', 'yellow', 'green']

fruits = Fruits(values=value_dict)
fruits_dict = fruits(keys=key_dict)
cprint(fruits_dict, color='black', on_color='on_white', force_color=True)

