import sys


def checkMe(test):
    left = 0
    right = 0

    for i, c in enumerate(test):
        # Adding left is always okay
        if c == '(':
            left += 1

        # Cant add right if its equal, it will make the right side higher
        elif c == ')':
            if left != right:
                right += 1
            else:
                sys.exit('Invalid at I:{} C:{}'.format(i, c))
        # All other characters
        else:
            pass

    # After all counting, its has to be equal
    if left == right:
        sys.exit('Valid')
    else:
        sys.exit('Invalid')

checkMe(sys.argv[1])
