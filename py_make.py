#!/usr/bin/python3
import sys

def make_java():
    string = f'''
    #
    # define compiler and compiler flag variables
    #

    JFLAGS = -d .
    JC = javac


    #
    # Clear any default targets for building .class files from .java files; we 
    # will provide our own target entry to do this in this makefile.
    # make has a set of default targets for different suffixes (like .c.o) 
    # Currently, clearing the default for .java.class is not necessary since 
    # make does not have a definition for this target, but later versions of 
    # make may, so it doesn't hurt to make sure that we clear any default 
    # definitions for these
    #

    .SUFFIXES: .java .class


    #
    # Here is our target entry for creating .class files from .java files 
    # This is a target entry that uses the suffix rule syntax:
    #	DSTS:
    #		rule
    #  'TS' is the suffix of the target file, 'DS' is the suffix of the dependency 
    #  file, and 'rule'  is the rule for building a target	
    # '$*' is a built-in macro that gets the basename of the current target 
    # Remember that there must be a < tab > before the command line ('rule') 
    #

    .java.class:
        $(JC) $(JFLAGS) $*.java


    #
    # CLASSES is a macro consisting of 4 words (one for each java source file)
    #

    #Register calsses here
    CLASSES = Main.java 
            


    #
    # the default make target entry
    #

    default: classes
            #add entry point command here


    #
    # This target entry uses Suffix Replacement within a macro: 
    # $(name:string1=string2)
    # 	In the words in the macro named 'name' replace 'string1' with 'string2'
    # Below we are replacing the suffix .java of all words in the macro CLASSES 
    # with the .class suffix
    #

    classes: $(CLASSES:.java=.class)


    #
    # RM is a predefined macro in make (RM = rm -f)
    #

    clean:
        $(RM) *.class
    '''
    with open('Makefile', 'w') as file:
        file.write(string)
    file.close()

def help():
    string = f'''
    py_make: \n

    -j or --java                creates a make file scaffold for a Java project \n
    -c or --c                   creates a make file scaffold for a C project \n
    -c++ or --c++               creates a make file scaffold for a C++ project \n
    '''
    print(string)

def main():
        if(len(sys.argv) < 2):
            print("[Usage: py_make <flags>] -h for help")
            return
        if(len(sys.argv)>2):
            print("[Usage: py_make <flags>] -h for help")
            return
        if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            help()
            return
        if(sys.argv[1] == "-j" or sys.argv[1] == "--java"):
            make_java()
            return
        if(sys.argv[1] == '-c' or sys.argv[1] == '--c'):
            make_c()
            return
        if(sys.argv[1] == '-c++' or sys.argv[1] == '--c++'):
            make_cpp()
            return
if __name__ == "__main__":
    main()




