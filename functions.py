import os
import string
import random
import nltk

PYTHON_TERM_OUT = ["what is a list?, A list is a collection of mutable items bounded by square brackets." ,
                   "what is a tuple?, A tuple is a collection of immutable items bounded by brackets." , 
                   "what is a dictionary?, A dictionary is a collection of items indexed by their keys bounded by weird brackets." ,
                   "what is indexing?, Indexing is taking an element from a list."]
PYTHON_TERM_INPUTS = ["list" , "tuple" , "dictionary" , "indexing",]
                 
RANDOM_LIST = [" is an awesome coder", " is a real python expert"]
NAMES = ["William", "Cyrus"]

def new_selector(input_string, check_list, return_list):
    
    """
    When the user asks for a term or piece of vocabulary in python, the function returns the exact definition of it.
    
    Returns
    -------
    Output: string
        string containing the definition of a python term
    """
    #initalize the output to None
    output = None
    
    #the conditional tests what is in the input string and returns the correct definition from the PYTHON_TERMS_DEFINITION list
    for x in input_string:
        if x in check_list:
            if x == check_list[0]:
                output = return_list[0]
            elif x == check_list[1]:
                output = return_list[1]
            elif x == check_list[2]:
                output = return_list[2]
            elif x == check_list[3]:
                output = return_list[3]
            break
        else:
            continue
    return output

def identity(input_string, names, random_list):
    """
    When the user inputs a name, it will return that name and a random sentence at the end about them as a student.
    
    Returns
    -------
    Output : string
        string containing the name concatenated with the random sentence finisher
    """
    
    #initalize output to None
    output = None
    
    #loop through the names inputted by user
    for x in input_string:
        
        #ensure the input is in the list of names
        if x in names:
            
            #if the name is a certain name in the list, it will return that name along with a random sentence finisher.
            if x ==names[0]:
                output = names[0] + random.choice(random_list)
            elif x == names[1]:
                output = names[0] + random.choice(random_list)
            break
        else:
            continue
    #the break and continue ensure the code is continous and does not stop randomly if a name is not in the list    
    
    #returns the name as well as the random sentence concatenated with it.
    return output 

def quiz_trigger(input_string):
    output = None
    if input_string == "quiz me":
        output = "what language do we learn in COGS18"
    return output

def quizzer(input_string):
    
    """
    When user answers a question, function returns a score depending on if the answer is the same as what it programmed
    
    Returns
    -------
    Output: int
        int represents how many questions were right
    """
    
    #initalize couter to 0 to represent the score before the quiz is graded
    counter = 0
    
    #tests if the input by user matches the answer
    if input_string == "python":
        
        #adds 1 to the score if correct
        counter += 1
        
    elif input_string == "java":
        
        #gain no score if the input by user is not the answer
        counter += 0
    
    #returns the score of the user
    return counter

def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False 

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []
            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))
            outs.append(selector(msg, NAMES, RANDOM_LIST))
            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))
        
            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE
            outs.append(new_selector(msg, PYTHON_TERM_INPUTS, PYTHON_TERM_OUT))
            outs.append(identity(msg, NAMES, RANDOM_LIST))
            outs.append(quiz_trigger(msg))
            outs.append(quizzer(msg))
            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)