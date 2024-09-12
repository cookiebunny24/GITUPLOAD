def isHappyNumber(n):
    sum = 0
    while (n):
        digit = n % 10
        sum = sum + digit * digit
        n = n / 10
    # code goes here
    return n


def MathChallenge(n):
    st = set()
    while (1):
        n = isHappyNumber(n)
        if (n == 1):
            return True
        if n not in st:
            return False
        st.insert(n)

    # keep this function call here


print(MathChallenge(1))