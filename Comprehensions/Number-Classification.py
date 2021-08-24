list_of_numbers = [int(num) for num in input().split(", ")]
positives = []
negatives = []
odds = []
evens = []
[positives.append(el) if el >= 0 else negatives.append(el) for el in list_of_numbers]
[evens.append(el) if el % 2 == 0 else odds.append(el) for el in list_of_numbers]
positives = [str(item) for item in positives]
negatives = [str(item) for item in negatives]
evens = [str(item) for item in evens]
odds = [str(item) for item in odds]
print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")