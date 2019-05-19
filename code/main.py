sequenceString = "53,242,145,24,23,242,11,17,5,3"
targetNumber = 250

sequenceList = sequenceString.split(",")

lengthOfSequence = len(sequenceList)

unsortedListOfNumbers = [int(num) for num in sequenceList]

sorted_list_of_numbers = []

while unsortedListOfNumbers:
    minimum = unsortedListOfNumbers[0]  # arbitrary number in list
    for x in unsortedListOfNumbers:
        if x < minimum:
            minimum = x
    sorted_list_of_numbers.append(minimum)
    unsortedListOfNumbers.remove(minimum)

total = 0
counter = 0
for num in unsortedListOfNumbers:
    if total < targetNumber:
        total += int(num)
        counter += 1

print(total)
print(counter)
print(unsortedListOfNumbers)
