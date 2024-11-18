

def find_pairs(n):
    result = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            sum_ab = a + b
            if sum_ab != 0 and n % sum_ab == 0:
                result.append((a, b))
    result_string = ''.join(f'{a}{b}' for a, b in result)
    return result_string
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = find_pairs(n)
    print("Пароль:", result)

