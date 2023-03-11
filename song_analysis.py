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

def main():
    lines = read_lyrics(song_path)
    lines = remove_new_line_characters(lines)
    print(lines)

if __name__ == "__main__":
    main()
