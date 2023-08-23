if __name__=="__main__":
    file_name = "../dataset/n-gram/metadata/recent_freq_dictionary.txt"
    base_value = 1

    recent_freq_dictionary = open(file_name, "r")
    line_file = filter(None, (line.rstrip() for line in recent_freq_dictionary))

    for local_line in line_file:
        local_line = local_line.split(" ")
        if (len(local_line) == 2):
            print (local_line[0], " ", local_line[1])
        else:
            print (local_line[0], " ", base_value)