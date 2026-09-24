def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        d1 = ord(num1[i]) - ord('0')
        for j in range(n - 1, -1, -1):
            d2 = ord(num2[j]) - ord('0')
            mul = d1 * d2
            sumPos = i + j + 1
            carryPos = i + j
            total = mul + result[sumPos]
            result[sumPos] = total % 10
            result[carryPos] += total // 10
    start = 0
    while start < len(result) - 1 and result[start] == 0:
        start += 1
    return ''.join(map(str, result[start:]))
print(multiply("123", "456"))  # 56088