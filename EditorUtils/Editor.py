import tkinter.simpledialog as tksd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from EditorUtils import Status_Bar
from SearchFeatures import Edit_Distance_For_Sentences, Entity_Analysis, Synonym_Search, Part_Speech_Search, \
    Levenshtein_Distance_3

# TODO: highlight repeated words (make sure)
# TODO: Ignroe punctuation


# set up the frame
master = Tk()
master.title("Searchable")
master.geometry("400x380")

text = Text(master, width=400, height=380, font=("Andale Mono", 12), highlightthickness=0, bd=2)

labelText = StringVar()

status = Status_Bar.StatusBar(master)
status.pack(side=BOTTOM, fill=X)
text.pack()


# Methods
def new():
    ans = messagebox.askquestion(title="Save File", message="Would you like to save this file?")
    if ans is True:
        save()
    delete_all()


def open_file():
    new()
    file = filedialog.askopenfile()
    # take whatever is in file and put it in box
    text.insert(INSERT, file.read())


def save():
    path = filedialog.asksaveasfilename()
    write = open(path, mode='w')
    write.write(text.get("1.0", END))


def close():
    save()
    master.quit()


def cut():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def copy():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())


def paste():
    text.insert(INSERT, master.clipboard_get())


def delete():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def select_all():
    text.tag_add(SEL, "1.0", END)


def delete_all():
    text.delete(1.0, END)


def search_synonyms():
    text.tag_remove("tag", "1.0", END)

    # get the text from the text editor
    the_text = text.get("1.0", END)

    ment = tksd.askstring("Search Synonyms", "Enter your search:", parent=master)


    if len(str(ment))== 0:
        messagebox.showinfo("Synonym", "No text in the search.")
        print("hi")
        return
    elif text.compare("end-1c", "==", "1.0"):
        messagebox.showinfo("Synonym", "No text in the editor.")

    else:
        # ment = tksd.askstring("Search Synonyms", "Enter your search:", parent=master)

        search_word = str(ment).lower()

        result_dict = Synonym_Search.word_to_concepts(the_text)
        print(result_dict)

        if len(result_dict.values()) == 0:
            return
        elif search_word not in result_dict:
            messagebox.showinfo("Synonym", "Search word not found.")
            return
        else:
            word_syns = result_dict[search_word]

        for item in word_syns:
            print("word: " + str(item[0]) + " line: " + str(item[1]) + " , " + " column: " + str(item[2]))

            if item[2] is None:
                continue
            else:
                text.tag_add("tag", str(item[1]) + "." + str(item[2]), str(item[1]) + "." + str(len(item[0]) + item[2]))
                text.tag_config("tag", background="yellow", foreground="black")
        status.set("Synonym search complete for: " + search_word)


def part_speech():
    text.tag_remove("tag", "1.0", END)

    # get the text from the text editor
    the_text = text.get("1.0", END)

    ment = tksd.askstring("Part of Speech Search", "Enter your grammar search:", parent=master)

    if len(str(ment)) == 0:
        messagebox.showinfo("Synonym", "No text in the search.")
        print("hi")
        return
    elif text.compare("end-1c", "==", "1.0"):
        messagebox.showinfo("Synonym", "No text in the editor.")
        return
    else:

        part_word = str(ment).lower()

        pos_acr_list = Part_Speech_Search.part_of_speech_to_tag(part_word)
        r_dict = Part_Speech_Search.make_dict(the_text, the_text)

        print(r_dict)

        if len(part_word) == 0:
            print("Hi")
            return
        elif pos_acr_list is None:
            messagebox.showinfo("Part of Speech", str(ment) + " not part of speech.")
            return

        for pos_acr in pos_acr_list:
            if pos_acr in r_dict.keys():
                word_speech = r_dict[pos_acr]

                for item in word_speech:
                    print("word: " + str(item[0]) + " line: " + str(item[1]) + " , " + " column: " + str(item[2]))
                    if item[2] is None:
                        continue
                    else:
                        text.tag_add("tag", str(item[1]) + "." + str(item[2]),
                                     str(item[1]) + "." + str(len(item[0]) + item[2]))
                        text.tag_config("tag", background="orange", foreground="black")
        status.set("Part of speech search complete for:  " + part_word)


def entity():
    text.tag_remove("tag", "1.0", END)

    the_text = text.get("1.0", END)
    s_dict = {}
    s_dict.clear()

    ment = tksd.askstring("Entity Search", "Enter your type search:", parent=master)
    s_word = str(ment).lower()

    if text.compare("end-1c", "==", "1.0"):
        messagebox.showinfo("Synonym", "No text in the search.")
        print("hi")
        return
    elif text.compare("end-1c", "==", "1.0"):
        messagebox.showinfo("Synonym", "No text in the editor.")
        return
    else:
        s_word = str(ment).lower()

        # s_dict = Entity_Analysis.create_dict(s_word, the_text, the_text)
        s_dict = Entity_Analysis.create_dict(s_word, the_text)
        print(s_dict)

        if len(s_dict.values()) == 0:
            return

        elif s_word not in s_dict:
            messagebox.showinfo("Entity Analysis", "Type not found.")
            return
        else:
            word_speech = s_dict[s_word]

        for item in word_speech:
            print("word: " + str(item[0]) + " line: " + str(item[1]) + " , " + " column: " + str(item[2]))

            if item[2] is None:
                continue

            else:
                text.tag_add("tag", str(item[1]) + "." + str(item[2]), str(item[1]) + "." + str(len(item[0]) + item[2]))
                text.tag_config("tag", background="green", foreground="black")
        status.set("Entity search complete for: " + s_word)
        s_dict.clear()


def levenshtein():
    text.tag_remove("tag", "1.0", END)

    the_text = text.get("1.0", END)

    ment = tksd.askstring("Levenshtein Calculation", "Enter your levenshtein distance search:", parent=master)
    max_distance = tksd.askstring("Levenshtein Calculation", "Enter the upper bound for the levenshtein distance search:", parent=master)

    if len(str(ment)) == 0:
        messagebox.showinfo("Synonym", "No text in the search.")
        print("hi")
        return
    if text.compare("end-1c", "==", "1.0"):
        messagebox.showinfo("Synonym", "No text in the editor.")
        return
    else:

        word = str(ment).lower()
        max_distance = int(max_distance)

        l_dict = Levenshtein_Distance_3.find_word(word,max_distance,the_text)

        print(l_dict)

        if len(l_dict.values()) == 0:
            print("hi")
            return
        elif word not in the_text:
            messagebox.showinfo("Levenshtein", "Word not in text.")
            return
        else:
            word_list = l_dict[word]

            for item in word_list:
                print("word: " + str(item[0]) + " line: " + str(item[1]) + " , " + " column: " + str(item[2]))
                if item[2] is None:
                    continue

                else:
                    text.tag_add("tag", str(item[1]) + "." + str(item[2]), str(item[1]) + "." + str(len(item[0]) + item[2]))
                    text.tag_config("tag", background="green", foreground="black")

        status.set("Levenshtein distance for : " + word + " " + str(max_distance))


def edit_distance_for_sentence():
    text.tag_remove("tag", "1.0", END)
    the_text = text.get("1.0", END)

    if len(the_text) == 1:
        messagebox.showinfo("Synonym", "No text in the editor.")
        return
    else:
        sentence_one = tksd.askstring("Edit Distance for Sentence", "Enter your levenshtein distance search:",parent=master)

        sentence_two = tksd.askstring("Edit Distance for Sentence", "Enter your levenshtein distance search:",parent=master)

        distance_value = Edit_Distance_For_Sentences.LDforSentences(sentence_one, sentence_two)

        if sentence_one in the_text and sentence_two in the_text:
            messagebox.showinfo("Edit Distance for Sentence", distance_value)
        else:
            messagebox.showinfo("Edit Distance for Sentence", "Sentence not in text.")

        status.set("Edit Distance for Sentence: " + sentence_one + " " + sentence_two)


def get_sentiment():
    text.tag_remove("tag", "1.0", END)
    the_text = text.get("1.0", END)

    sentiment = Entity_Analysis.GetData.get_sentiment(the_text)
    messagebox.showinfo("Text Sentiment:", "sentiment: " + sentiment[3] + "\nscore: " + str(sentiment[1]))


def get_emotion():
    text.tag_remove("tag", "1.0", END)
    the_text = text.get("1.0", END)

    emotions = Entity_Analysis.GetData.get_emotion(the_text)
    result = ""
    for emotion in emotions.keys():
        result += emotion + ": " + str(emotions[emotion]) + "\n"
    messagebox.showinfo("Text Emotion:", result)


# File Menu
menu = Menu(master)
# set menu and makes main menu
master.config(menu=menu)
file_menu = Menu(menu)

menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close)
file_menu.add_command(label="Save", command=save)

# Edit Menu
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

# Search Menu

search_menu = Menu(menu)
menu.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Synonyms", command=search_synonyms)
search_menu.add_command(label="Entity Analysis", command=entity)

# mEntry = Entry(search_menu, textvariable=ment).pack()
grammar_menu = Menu(menu)
menu.add_cascade(label="Grammar", menu=grammar_menu)
grammar_menu.add_cascade(label="Part of Speech", command=part_speech)

extra_menu = Menu(menu)
menu.add_cascade(label="Extra", menu=extra_menu)
extra_menu.add_cascade(label="Levenshtein", command=levenshtein)
extra_menu.add_cascade(label="Edit Distance for Sentences", command=edit_distance_for_sentence)

text_analysis_menu = Menu(menu)
menu.add_cascade(label="Analyze", menu=text_analysis_menu)
text_analysis_menu.add_command(label="Sentiment", command=get_sentiment)
text_analysis_menu.add_command(label="Emotion", command=get_emotion)

text.focus_set()

master.mainloop()
