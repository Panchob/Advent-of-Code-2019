START_VALUE = 402328
END_VALUE = 864247


def isValidPassword(password):
    isValid = False
    currentSequence = password[0]

    # Skip the first number, no need to check it.
    for number in password[1:]:
        # The password is always increasing
        if number < currentSequence:
            isValid = False
            break
        # It's not valid unless it have at least one repetition.
        elif number != currentSequence:
            currentSequence = number
        else:
            isValid = True
    return isValid


def isValidPasswordWithMatchingRule(password):
    isIncreasing = True
    currentSequence = password[0]
    sequenceSize = 1
    hasValidGroup = False

    # Skip the first number, no need to check it.
    for number in password[1:]:
        # The password is always increasing
        if number < currentSequence:
            isIncreasing = False
            break
        # It's not valid unless it have at least one repetition.
        elif number != currentSequence:
            currentSequence = number
            # Changed number after a valid sequence.
            if sequenceSize == 2:
                hasValidGroup = True
            sequenceSize = 1
        else:
            sequenceSize = sequenceSize + 1

    # Had to include sequence here for when the valid repetition
    # is at the end of the password ex: 111122
    return (isIncreasing and (hasValidGroup or sequenceSize == 2))


part1 = 0
part2 = 0

for n in range(START_VALUE, END_VALUE):
    # Change each number into an array
    password = [x for x in str(n)]

    # PART ONE
    if isValidPassword(password):
        part1 += 1

    # PART TWO
    if isValidPasswordWithMatchingRule(password):
        part2 += 1

print("PART ONE:", part1)
print("PART TWO:", part2)
