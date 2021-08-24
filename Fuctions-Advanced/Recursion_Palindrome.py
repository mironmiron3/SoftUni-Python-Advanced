def palindrome(word,index):
    left_index = index
    right_index = len(word) - 1 - index

    if left_index >= right_index:
        return f"{word} is a palindrome"

    left_letter = word[left_index]
    right_letter = word[right_index]

    if left_letter != right_letter:
        return f"{word} is not a palindrome"
    palindrome(word,index+1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome("abcba", 0))
