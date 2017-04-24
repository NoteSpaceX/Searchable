from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import tkinter.simpledialog as tksd

import EditDistanceForSentences
import levenshtein_distance
import status_bar
import synonym_search
import part_speech_search
import entity_analysis

# TODO: if user types in nothing in the editor
# TODO: highlight repeated words (make sure)
# TODO: error for invalid searches

# set up the frame
master = Tk()
master.title("Searchable")
master.config(background="black")
master.wm_state("zoomed")

text = Text(master)
text.pack(fill=Y, expand=1)

text.config(
    borderwidth=0,
    font="{Helvetica} 20",
    foreground="white",
    width="300",
    background="black",
    insertbackground="white",  # cursor
    selectforeground="white",  # selection
    selectbackground="#008000",
    wrap=WORD,  # use word wrapping
    undo=True,  # Tk 8.4
)

ment = StringVar()
labelText = StringVar()

status = status_bar.StatusBar(master)
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

    ment = tksd.askstring("Search Synonyms", "Enter your search:", parent=master)
    print(ment)

    # ment = pop_up.MyDialog.ok()
    search_word = str(ment)

    # get the text from the text editor
    the_text = text.get("1.0", END)

    result_dict = synonym_search.word_to_concepts(the_text, the_text)
    print(result_dict)

    if search_word not in result_dict:
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

    ment = tksd.askstring("Part of Speech Search", "Enter your grammar search:", parent=master)
    print("ment: ", ment)
    part_word = str(ment)

    print('part_word', part_word)

    # get the text from the text editor
    the_text = text.get("1.0", END)

    pos_acr_list = part_speech_search.part_of_speech_to_tag(part_word)
    print("pos_acr_list: ", pos_acr_list)
    r_dict = part_speech_search.make_dict(the_text, the_text)

    if pos_acr_list is None:
        print("message box??")
        messagebox.showinfo("Part of Speech", ment + "not found")
        return

    for pos_acr in pos_acr_list:
        if pos_acr in r_dict.keys():
            word_speech = r_dict[pos_acr]
            print('word_speech:', word_speech)

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

    ment = tksd.askstring("Entity Search", "Enter your type search:", parent=master)
    print(ment)
    s_word = str(ment)

    the_text = text.get("1.0", END)

    s_dict = entity_analysis.create_dict(s_word, the_text, the_text)
    print(s_dict)

    if s_word not in s_dict:
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


def levenshtein():
    text.tag_remove("tag", "1.0", END)

    ment = tksd.askstring("Levenshtein Calculation", "Enter your levenshtein distance search:", parent=master)
    print(ment)
    word = str(ment)
    other_word = tksd.askstring("Levenshtein Calculation", "Enter your levenshtein distance search:", parent=master)

    the_text = text.get("1.0", END)

    l_dict = levenshtein_distance.find_word(word, other_word, the_text, the_text)

    lev_distance = levenshtein_distance.minimumEditDistance(word, other_word, the_text)[2]

    if word not in the_text and other_word not in the_text:
        messagebox.showinfo("Levenshtein", "Word not in text.")
        return
    else:
        messagebox.showinfo("Levenshtein distance", lev_distance)

    word_list = l_dict[word]

    for item in word_list:
        print("word: " + str(item[0]) + " line: " + str(item[1]) + " , " + " column: " + str(item[2]))

        if item[2] is None:
            continue

        else:
            text.tag_add("tag", str(item[1]) + "." + str(item[2]), str(item[1]) + "." + str(len(item[0]) + item[2]))
            text.tag_config("tag", background="green", foreground="black")

    status.set("Levenshtein distance for : " + word + " " + other_word)


def editDistanceForSentence():
    text.tag_remove("tag", "1.0", END)

    sentence_one = tksd.askstring("Edit Distance for Sentence", "Enter your levenshtein distance search:",
                                  parent=master)
    # print(ment)
    # sentence_one = str(ment)
    sentence_two = tksd.askstring("Edit Distance for Sentence", "Enter your levenshtein distance search:",
                                  parent=master)

    distance_value = EditDistanceForSentences.LDforSentences(sentence_one, sentence_two)

    the_text = text.get("1.0", END)

    if sentence_one in the_text and sentence_two in the_text:
        messagebox.showinfo("Edit Distance for Sentence", distance_value)
    else:
        messagebox.showinfo("Edit Distance for Sentence", "Sentence not in text.")

    status.set("Edit Distance for Sentence: " + sentence_one + " " + sentence_two)


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
extra_menu.add_cascade(label="Edit Distance for Sentences", command=editDistanceForSentence)

text.focus_set()

master.mainloop()
