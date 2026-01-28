def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)

n1, n2 = map(int, input().split())

print(gcd(n1, n2))
print(lcm(n1, n2))