class Navigate:
    # way to get the line number of something we want
    # @staticmethod
    # def get_line(word, text):
    #     text = (text.split("\n"))
    #     line_num = 1
    #     line_list = []
    #     print('text: ', text)
    #     for sentence in text:
    #         words_in_sentence = sentence.split(" ")
    #         print('sent:', words_in_sentence)
    #         # if word in sentence:
    #         #     line_list.append(line_num)
    #         # line_num += 1
    #         for text_word in words_in_sentence:
    #             print('text_word: ', text_word)
    #             if text_word == word:
    #                 print('hi')
    #                 line_list.append(line_num)
    #
    #         line_num += 1
    #     return line_list

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
        # for line_list in text:
        #     line_list = text.split("\n")
        line_list = text.split("\n")
        print('line_list', line_list)
        print('line_list length: ', len(line_list))

        for i in range(0, len(line_list)):
            item = line_list[i].split(" ")
            print(item)
            j = 0

            for k in range(0, len(item)):
                if " " not in word:
                    if item[k] == word:
                        return j
                    j += len(item[k]) + 1
                # for search phrase with more than one word
                else:
                    word_list = word.split(" ")
                    for num in range(0, len(word_list)):
                        if k + num < len(item) - 1:
                            if word_list[num] == item[k + num]:
                                return j
                    j += len(item[k]) + 1

    @staticmethod
    def get_tuple(word, text):
        # for line_list in text:
        #     line_list = text.split("\n")
        line_list = text.split("\n")

        column_list = []

        for i in range(0, len(line_list)):
            item = line_list[i].split(" ")
            j = 0

            for k in range(0, len(item)):
                if " " not in word:
                    if item[k] == word:
                        column_list.append((i+1, j))
                    j += len(item[k]) + 1
                # for search phrase with more than one word
                else:
                    word_list = word.split(" ")
                    for num in range(0, len(word_list)):
                        if k + num < len(item) - 1:
                            if word_list[num] == item[k + num]:
                                column_list.append((i+1, j))
                    j += len(item[k]) + 1
        return column_list
                    # for m in range(0, len(word)):
                    #     if k+m < len(item)-1:
                    #         if item[k+m] != word[k+m]:
                    #             j += len(item[k]) + 1