from plugin import plugin


@plugin("armstrong_numbers")
def element(jarvis, s):
    num = int(input("Enter a number: "))
    length = len(str(num))
    sum = 0
    tmp = num
    while tmp > 0:
        digit = tmp % 10
        sum += digit ** length
        tmp //= 10

    if num == sum:
        answer = f"The number {num} is armstrong."
    else:
        answer = f"The number {num} is not  armstrong."
    jarvis.say(answer)
