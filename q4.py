def make_list_of_files(n):
    """
    Make a list of n file names with the format "file_0.txt"
    Assume n is greater than or equal to 1
    Hint: use a loop and append
    """
    file_list = []
    for i in range(n):
        file_list.append(f"file_{i}.txt")
    return file_list

print(make_list_of_files(5))  # ['file_0.txt', 'file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']
