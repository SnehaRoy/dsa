class GroupAnagram():
    def __init__(self):
        self.dict_result = {}
    
    def findanagram(self, input):
        for i in input:
            word = ''.join(sorted(i))

            if word in self.dict_result.keys():
                self.dict_result[word].append([i])
            else:
                self.dict_result.setdefault(word, [i])
        return list(self.dict_result.values())

def main():

    obj = GroupAnagram()

    input_list = ["eat","tea","tan","ate","nat","bat"]

    result  = obj.findanagram(input_list)

    print(result)

if __name__ == "__main__":
    main()