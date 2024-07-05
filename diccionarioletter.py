import string

def char_sequence_iterator(max_length):
    chars = string.ascii_lowercase  
    
    for length in range(1, max_length + 1):
        for combination in chars:
            yield combination * length


char_sequences = char_sequence_iterator(9)

for sequence in char_sequences:
    print(sequence)