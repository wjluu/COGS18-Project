import os
import string
import random
import nltk

def test_new_selector():
    
    assert isinstance(new_selector(["list"],PYTHON_TERM_INPUTS, PYTHON_TERM_OUT), str) 

    assert(new_selector(["list"],PYTHON_TERM_INPUTS, PYTHON_TERM_OUT)) == "what is a list?, A list is a collection of mutable items bounded by square brackets."

    assert(new_selector(["tuple"], PYTHON_TERM_INPUTS, PYTHON_TERM_OUT)) == "what is a tuple?, A tuple is a collection of immutable items bounded by brackets."
    
    
def test_quizzer():
    
    """tests for the quizzer function"""
    
    #test if the answer is an integer
    assert isinstance(quizzer("python"), int)
    
    #test if the answer is 1
    assert(quizzer("python")) == 1
    
    #test if the answer is 0
    assert(quizzer("java")) == 0
    
    