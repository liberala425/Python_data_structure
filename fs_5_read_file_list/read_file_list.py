def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    file1 = open(filename, "r")
    output_lst = file1.readlines() 
    #remove all empty lines isspace() cover the \n
    output_lst = [val for val in output_lst if (not val.isspace())] 
    for val in output_lst:
        if '\n' in val:
            print(f"- {val[:-1]}")
        else:
            print(f"- {val}")


