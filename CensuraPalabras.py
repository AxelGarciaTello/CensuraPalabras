##
# Redact a text file by removing all ocurrences of sensitive words.
# The redacted version of the text is writter to a new file.
#
# Note that this program does not perform any error checking, and it
# does not implements case insensitive redaction
#

try:
    #Get the name of the inpur file and open it
    inf_name=input("Enter the name of the text file to redact: ")
    inf=open(inf_name, "r")

    #Get the name of the sensitive words file and open it
    sen_name=input("Enter the name of the sensitive words file: ")
    sen=open(sen_name, "r")

    #Load all of the sensitive words into a list
    words=[]
    line=sen.readline()
    while line!="":
        line=line.rstrip()
        words.append(line)
        line=sen.readline()

    sen.close()

    #Get the name of the output file and open it
    outf_name=input("Enter the name for the new redacted file: ")
    outf=open(outf_name, "w")

    #Read each line from input file. Replace all of the sensitive words
    #with asterisks. Then write the line to the output file.
    line=inf.readline()
    while line!="":
        #Check for and replace each sensitive word. Use a number of
        #asterisks that matches the number of letters in the word
        for word in words:
            line=line.replace(word, "*"*len(word))
        #Write the modified line to the output file
        outf.write(line)
        #Read the next line from the input file
        line=inf.readline()

    #Close the input and output files
    inf.close()
    outf.close()

except IOError:
    #Display a message if something goes wrong while accesing the file
    print("An error ocurred while accessing the file.")
