def longest_common_prefix(lists):
    prefix = lists[0]

    for i in range(1,len(lists)):
        while(not lists[i].startswith(prefix)):
            prefix = prefix[0:len(prefix) - 1]

    return prefix

print(longest_common_prefix(['flower', 'flow', 'flight']))