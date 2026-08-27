def is_palindrome(x):
    s = str(x)
    if s == s[::-1]:
        return True
    else:
        return False
x = int(input("Enter a number: "))
print(is_palindrome(x))