class Navigate:
    # way to get the line number of something we want
    @staticmethod
    def get_line(word, text):
        text = (text.split("\n"))
        line_num = 1
        for element in text:
            if word in element:
                return line_num
            line_num += 1

    @staticmethod
    def get_specific_column_number(word, text):
        for line_list in text:
            line_list = text.split("\n")
        print('line_list: ', line_list)

        for i in range(0, len(line_list)):
            item = line_list[i].split(" ")
            j = 0

            for k in range(0, len(item)):
                if item[k] == word:
                    print('j ', j)
                    return j
                j += len(item[k]) + 1