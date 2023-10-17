text = input().split()
palindrome_search = input()
palindromes = []

for i in text:
    if i == ''.join(reversed(i)):
        palindromes.append(i)

print(f'{palindromes}')
print(f"Found palindrome {palindromes.count(palindrome_search)} times")