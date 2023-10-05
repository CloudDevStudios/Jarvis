from plugin import plugin


@plugin("kaprekar")
def kaprekar(jarvis, s):
    n1 = int(input("Enter a number: "))
    if n1 > 0:
        sq = n1**2
        m = 1 * 10
        a = sq // m
        b = sq % m
        while a + b != n1 and a != 0:
            m = m * 10
            a = sq // m
            b = sq % m

        if a + b == n1 and sq % 10 != 0:
            answer = "Yes, kaprekar number"
        else:
            answer = "Not kaprekar number"
        jarvis.say(answer)


