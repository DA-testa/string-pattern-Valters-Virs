# python3

B = 128
Q = 79

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return

    input_type = input()

    if input_type.upper()[0] == "I":
        # Input I

        return (input().rstrip(), input().rstrip())

    if input_type.upper()[0] == "F":
        # Input F

        file = open("tests/06", "r")

        pattern = file.readline()
        text = file.readline()

        file.close()

        return (pattern.rstrip(), text.rstrip())
    
    return ('', '')

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    occurrences = []

    pattern_len = len(pattern)
    text_len = len(text)

    pattern_hash = get_hash(pattern)
    substring_hash = get_hash(text[:pattern_len])

    multiplier = 1
    for _ in range(pattern_len - 1):
        multiplier = (multiplier * B) % Q

    # for each character in text minus last few, where the pattern cannot be
    for i in range(text_len - pattern_len + 1):
        if i != 0:
            # calculate next substring hash
            substring_hash = ((substring_hash - ord(text[i - 1]) * multiplier) * B + ord(text[i + pattern_len - 1])) % Q

        if pattern_hash == substring_hash:
            if pattern == text[i:(i + pattern_len)]:
                occurrences.append(i)
        
    # and return an iterable variable
    return occurrences

def get_hash(text):
    hash = 0

    for i in range(len(text)):
        hash = (B * hash + ord(text[i])) % Q

    return hash

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

