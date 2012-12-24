#!/usr/bin/env python

'Final Project'
'Long Pham'
'CSC 171-1'
'Professor William Turner'

# read the mutliple-choice question file
# reorganize into a nested list, each element has this order
# (answer_code, question, answer1, answer2, answer3, answer4)

import os
import random

def QuizGame(n):

    # open the quiz file
    quiz = open("QUIZ.DAT", "r")
    lineList = quiz.readlines()
    quiz.close()

    # generate the nested list
    quiz_list = []
    for k, line in enumerate(lineList):

        line1 = line.strip()
        list_complete = False
        # build a list for each question
        if k % 6 == 0:
            answer_code = line1
        if k % 6 == 1:
            question = line1
        if k % 6 == 2:
            answer1 = line1
        if k % 6 == 3:
            answer2 = line1
        if k % 6 == 4:
            answer3 = line1
        if k % 6 == 5:
            answer4 = line1
            list_complete = True
        if list_complete == True:
            list1 = [answer_code, question, answer1, answer2, answer3, answer4]
            quiz_list.append(list1)

    # run the game
    for i in range(1,n+1):
        
        decision = ('A', 'B', 'C', 'D')
        me = ''
        computer = random.choice(decision)
        
        # starting a round
        random_question = random.choice(quiz_list)

        print "====================="
        print random_question[1]
        print 'A. %s' % random_question[2]
        print 'B. %s' % random_question[3]
        print 'C. %s' % random_question[4]
        print 'D. %s' % random_question[5]

        print '*** GO!!! ***'
        me = raw_input('What will you choose? A, B, C, or D: ')

        print "====================="
        print "You choose: %s" % me.upper()
        print "I choose: %s" % computer

        # return the result
        if cmp(me.upper(), random_question[0]) == 0 and cmp(computer, random_question[0]) == 0:
            print 'Draw!'
        elif cmp(computer, random_question[0]) == 0:
            print 'I win!'
        elif cmp(me.upper(), random_question[0]) == 0:
            print 'You win!'
        else:
            print 'Noone wins! The correct answer is %s!' % random_question[0]
        raw_input('Press ENTER to continue')
