class Navigate:
    @staticmethod
    def get_line(word, text):
        text = text.split("\n")
        line_num = 1
        for element in text:
            if word in element:
                return line_num
            line_num += 1

    @staticmethod
    def get_specific_column_number(word, text):
        line_list = text.split("\n")
        print('line_list', line_list)

        for line in range(0, len(line_list)):
            line_word = line_list[line].split(" ")
            column_position = 0

            for char in range(0, len(line_word)):
                if " " not in word:
                    if line_word[char] == word:
                        return column_position
                    column_position += len(line_word[char]) + 1
                # for search phrase with more than one word
                else:
                    word_list = word.split(" ")
                    for num in range(0, len(word_list)):
                        if char + num < len(line_word) - 1:
                            if word_list[num] == line_word[char + num]:
                                return column_position
                    column_position += len(line_word[char]) + 1

    @staticmethod
    def get_tuple(word, text):
        line_list = text.split("\n")
        column_list = []

        for line in range(0, len(line_list)):
            item = line_list[line].split(" ")
            column_position = 0

            for k in range(0, len(item)):
                if " " not in word:
                    if item[k] == word:
                        column_list.append((line+1, column_position))
                    column_position += len(item[k]) + 1
                # for search phrase with more than one word
                else:
                    word_list = word.split(" ")
                    for num in range(0, len(word_list)):
                        if k + num < len(item) - 1:
                            if word_list[num] == item[k + num]:
                                column_list.append((line+1, column_position))
                    column_position += len(item[k]) + 1
        return column_list
