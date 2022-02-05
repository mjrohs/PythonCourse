def main():
    # open file
    read_file = open('names.txt', 'r')
    # create counter for names
    name_count = 0

    # iterate through file and add to counter for each line
    for line in read_file:
        name_count += 1

    # close file
    read_file.close()

    # output final total of names
    print('There are', name_count, 'names in this file')


main()
