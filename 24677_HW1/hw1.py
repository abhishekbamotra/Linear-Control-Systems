#!/usr/bin/env python
# coding: utf-8

# ## Homework 1

# #### Knowledge: Using python matrix operations

# Write a NumPy program to construct a random 3x3 matrix and perform these operations:
# 1. Find the inverse of the matrix.
# 2. Find the determinant of the same matrix. 
# 2. Normalize the same matrix w.r.t the maximum and minimum of the matrix.
# 
# The definition of matrix normalization is: For the matrix $A$, every element $a_{ij_{n e w}}=\frac{a_{ij} -A_{m i n}}{A_{m a x}-A_{m i n}}$ where, $A_{min}$ and $ A_{max}$ are the maimum and minimum of all elements in the matrix and $i,j = 0,1,3$.
# 
# 
# 
# 
# ---
# 
# 
# Save your randomized matrix and output matrix in "hw1_output.npy".
# 
# The npy files contains a dictionary with these key and value pairs. 
# 
# 
# 
# 
# *   "0": the_randomized_matrix_used, 
# *   "1": your_output_of_qs_1
# *   "2": your_output_of_qs_2
# *   "3": your_output_of_qs_3
# 
# 
# 
# 
# 
# 
# 
# 
# Attach the code with your homework solution. Make a zip file named "hw1.zip".
# 
# The code space is provided in next cell, take a look at submission details below for more details.
# 
# 
# Consider this jupyter notebook as your python playgroud. You can make cells and see line wise outputs. For information on what all things you can do, refer to: https://www.codecademy.com/articles/how-to-use-jupyter-notebooks 
# 
# 

# In[12]:


import numpy as np
import scipy as spy

randMat = np.random.rand(3,3)

inverseMat = np.linalg.inv(randMat)

detMat = np.linalg.det(randMat)

maxMat = np.amax(randMat)
minMat = np.amin(randMat)
normMat = (randMat-minMat)/(maxMat-minMat)

matDict = {"0": randMat, "1": inverseMat, "2": detMat, "3": normMat}

np.save("hw1_output", matDict)


# <!-- $
# \begin{array}{l}{\text { If you need help with this assignment, go to the following links: }} \\ {\bullet \text { Python Programming Language (wikipedia.org) }}  \\ \bullet \text {The Python Tutorial (python.org) }\end{array}
# $
#  -->
#  
#  If you need help with this assignment, go to the following links:
#  
#  
# 
# *   Python Programming Language (wikipedia.org)
# *   The Python Tutorial (python.org)
# *   Another good resource for python exercises and the video lectures provided by Udacity: 
# https://www.udacity.com/course/introduction-to-python--ud1110
# *    Consider this jupyter notebook as your python playgroud. You can make cells and see line wise outputs. For information on what all things you can do, refer to: https://www.codecademy.com/articles/how-to-use-jupyter-notebooks. 
# *    *Tip: You can use various hokeys for quick code testing like ctrl + / for commenting a line and ctrl + \[ to reduce tab for lines of code, find out and use various shortcut keys to increase your productivity. Debugging is an underrated and very important aspect of coding, figure out quick ways of debugging your code for yourself.*
# 
# 
# 

# 
# 
# 
# 
# ***Note:*** We will be using google style of python scripting according to this reference: https://github.com/google/styleguide/blob/gh-pages/pyguide.md
# 
# The way of code/variable Name writing highlited is provided in the same, i.e: 
# 
# 
# ---
# 
# 
# 
# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.

# 
# 
# ---
# 
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 
# If you are new to python , or not much confident to code in python from scratch, we provide you a reference to understand the concepts in a organized manner.
# 
# We **best one** we came across is *Introduction to python* in Udactiy, lectured by software engineer at Databricks, Juno Lee. 
# 
# 
# 
# > This crash course will teach you the best way to code in python.
# 
# 
# 
# ---
# 
# 
# 
# You are free to use any matrial on internet in only understanding the concepts.
# **Please refrain from copying codes from internet**. Typing it yourself makes you understand why the code is written in that manner. We provide you ways to learn and refesh new concepts. Use the assignment to practice coding and implementation by only yourself.
# 
# We recommend you to watch the series of videos in **1.5x**, in some important topics make sure you understand it correctly and hence you can reduce the speed. Try out these codes that is provided after the video in an online compiler like [Repl](https://repl.it/languages/python3) or [TutorialsPoint](https://www.tutorialspoint.com/execute_python_online.php)
# 
# 
# 
# ---
# 
# 
# 
# *   **Lesson 1** : Programming In Python.  
#   *Time: 1min with 1.5x (Video 2)*
# 
# *   **Lesson 2** : Arithematic Operators, Variables and Assignment Operators,   Integers and Floats, Boolean and Comparision operators, Strings, Type and Type conversion[1.25x], String Methods[1.25x], Read: "There's a Bug in my Code".
#  (Videos: section 2, 5, 8, 10, 13, 16, 19, 24, 25)
# 
#   *Time: Spend maximum about 20mins in 1st 5 sections and another 30min in the remaining*
#   
# *   **Lesson 3** : List and Membership Operators, Slice and Dice with Lists[1.25x], Mutability and Order[1.25x], Read: "Why Do We Need Lists?", List Methods[1.25x], 
#  (Videos: section 2, 5) (You dont need to understand all the keywords)
# 
# All of these might become too much to digest if you are just starting with python, hence we suggest you to complete all the lessons in a 3 day period starting from the release of this assignment. Practice a little daily, play with the codes, understand how it works and gain experience, soon you will get a hang of this language.
# 
# 
# 
# 
# ---
# 
# 

# __Submission:__
# 
# 
# 
# *   Upload your files "hw1.py" and "hw1_output.npy" to gradescope programming assignment 1 section. 
# *   The Autograder will give you the score to corresponding submission.
# *    You can resubmit multiple times. But only the latest of top two submissions will be evaluated for your score. Hence you have only 2 times for submission of scripts on gradescope.
# 
# 
# 
