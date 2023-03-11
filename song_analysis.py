#a series of lyrical analysis tools written in python to estimate song complexity
song_path = "/Users/henry_chadban/Documents/Data/Song Lyrics/Midnight Oil/Place_Without_A_Postcode/Brave_Faces.txt"

#import the lyrics from a text file
def read_lyrics(path):
    #generic code for reading a text file from https://www.pythontutorial.net/python-basics/python-read-text-file/
    with open(path) as f:
        lines = f.readlines()
    
    return lines

def remove_new_line_characters(lyrics):
    #remove new line characters from lines
    #all lines except last will have \n
    num_lines = len(lyrics) #number of lines in the song
    for i,line in enumerate(lyrics): #i is line index, go through all lines
        if i==num_lines-1: #for last line
            continue #no new line character, so continue
        else:
            line = line[:-1] #remove the last newline character
            lyrics[i] = line #update the lyrics object with the new line
    #now remove empty lines
    i = 0 #this time we need to keep track of line index manually, as we are deleting lines
    while i<num_lines:
        line = lyrics[i] #extract the line
        line_length = len(line)
        if line_length==0: #if line empty
            del lyrics[i] #delete the empty line
            num_lines = num_lines - 1 #there is one less line to iterate over
        else:
            i = i + 1 #move onto the next line
    return lyrics #return the updated lyrics

#converts all lines to lowercase at once, this is useful so words with different upper/lowercase are not counted as seperate words
def all_lower(lyrics):
    for i,line in enumerate(lyrics):
        lower_line = line.lower() #convert the string for each line to be lowercase
        lyrics[i] = lower_line #and store this lowercase line in the container for the lines
    return lyrics

#breaks a line into words
def break_line_into_words(line):
    words = []
    word = ''
    for i,character in enumerate(line): #go through all the characters in the line
        if character==' ':
            if len(word)==0: #catch the edge case that there are leading/trailing blanks
                continue #and do nothing, we don't need to store empty words
            else:
                words.append(word)
                word = '' #reset the word
        else:
            word = word+character #add the next character to the word
    #add the final word
    if len(word)==0:
        pass
    else:
        words.append(word)
    return words

#produces a dictionary representing word prevalence, key is the word, data is the prevalence
def word_prevalence(list_words):
    word_prevalence = {}
    for word in list_words:
        if word in word_prevalence: #if word already in the dictionary
            word_prevalence[word] = word_prevalence[word] + 1 #we have an extra instance of an already used word
        else:
            word_prevalence[word] = 1 #we have one instance of the new word
    return word_prevalence

#put all words into one list
def all_words_one_list(lyrics):
    all_words = [] #list to store all words
    for line in lyrics: #go through each line in the lyrics
        words = break_line_into_words(line) #break each line into words
        all_words = all_words + words #add these to the list of all words
    return all_words

#words per unique word, this is known in academia as T.T.R = Type-Token Ratio
#also returns num words and num unique words 
def words_per_unique_word(lyrics):
    lines = remove_new_line_characters(lyrics)
    lines = all_lower(lines)
    all_words = all_words_one_list(lines)
    word_frequency = word_prevalence(all_words)
    num_words = len(all_words)
    num_unique_words = len(word_frequency)
    words_per_unique_word = num_words/num_unique_words
    return words_per_unique_word,num_words,num_unique_words


def main():
    
    lyrics = read_lyrics(song_path)
    """
    lines = remove_new_line_characters(lines)
    lines = all_lower(lines)
    all_words = all_words_one_list(lines)
    word_frequency = word_prevalence(all_words)
    print(word_frequency)
    """
    uniqueness,num_words,num_unique_words = words_per_unique_word(lyrics)
    print(("{:.3f}".format(uniqueness)) ,' words per unique word')
    print(num_words,' total words')
    print(num_unique_words,' unique words')


if __name__ == "__main__":
    main()
