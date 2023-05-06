from random import randint

def generate_numbers(quantity):
    finalNumber = ''
    for _ in range(quantity):
        finalNumber += str(randint(0, 9))
    return finalNumber

def phone_number():
    return f"'+49 {generate_numbers(3)} {generate_numbers(3)} {generate_numbers(4)}'"

def write_to_file(content, *args: str):
    for element in args:
        content += f'\n{element}'
    with open('output.txt', 'wt') as file:
        file.write(content)

if __name__ == '__main__':
    write_to_file(*(phone_number() for _ in range(50)))