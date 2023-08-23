def gen_five_letter_token_freq(file_name):

    # read file and ignore empty lines
    token_file = open(file_name, "r")
    line_file = filter(None, (line.rstrip() for line in token_file))

    token_freq = {}
    for local_line in line_file:
        local_line = local_line.split('\t')

        # parse token
        token = local_line[0]
        token = token.split('_')
        token = token[0].lower()

        # parse count
        recent_count = local_line[-1]
        recent_count = recent_count.split(',')
        recent_count = int(recent_count[1])

        if (token in token_freq):
            token_freq[token] += recent_count
        else:
            token_freq[token] = recent_count

    # sort dictionary
    token_freq = dict(sorted(token_freq.items()))
    return token_freq

def print_freq(token_freq):
    for i in token_freq:
        print (i, " ", token_freq[i])

if __name__=="__main__":
    
    file_name = "../dataset/n-gram/metadata/token.txt"
    token_freq = gen_five_letter_token_freq(file_name)
    print_freq(token_freq)
