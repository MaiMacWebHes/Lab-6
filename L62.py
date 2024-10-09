# L62 — Perfect Numbers
# Mac Weber-Hess & Serenity Schuler

def perfect_number(n):
    total = 0
    for x in range(1,n):
        if n % x == 0:
            total = total + x
    if total == n:
        return True
    else:
        return False

def give_response():
    n = int(input("Give us a number for n …\n"))

    ans = perfect_number(n)
    print(ans)

give_response()