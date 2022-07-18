from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('ref_template')

content = {"Variables and data types" : {"Variables and data types":"ceder2018quick",
                                         "What Python doesn't do as well" :"ceder2018quick",
                                         "Numbers": "ceder2018quick",
                                         "Variables and assignments": "ceder2018quick",
                                         "Expressions": "ceder2018quick",
                                         "Strings": "ceder2018quick",
                                         "Casting variables": "ceder2018quick",
                                         "Getting input from user": "ceder2018quick",
                                         "Basic python style": "ceder2018quick"},
           "Collections" : {"Data Structures" : "gorelick2020high",
                            "Lists and tuples" : "gorelick2020high",
                            "Lists": "ceder2018quick",
                            "List indices": "ceder2018quick",
                            "List slicing": "ceder2018quick",
                            "Modifying lists": "ceder2018quick",
                            "Sorting lists": "ceder2018quick",
                            "Other common list operations": "ceder2018quick",
                            "List concatenation with the + operator": "ceder2018quick",
                            "List initialization with the * operator": "ceder2018quick",
                            "List minimum of maximum with min and max": "ceder2018quick",
                            "List matches with count": "ceder2018quick",
                            "Summary of list operations": "ceder2018quick",
                            "Tuples": "ceder2018quick",
                            "Packing and unpacking tuples": "ceder2018quick",
                            "Converting between lists and tuples": "ceder2018quick",
                            "Sets": "ceder2018quick",
                            "Set operations": "ceder2018quick",
                            "Dictionaries": "ceder2018quick",
                            "What is a dictionary?": "ceder2018quick",
                            "Other dictionary operations": "ceder2018quick",
                            "Word counting": "ceder2018quick",
                            "What can be used as key?": "ceder2018quick",
                            "Sparse matrices": "ceder2018quick"
                            },
            "Control flow": {"The while loop": "ceder2018quick",
                             "The if-elif-else": "ceder2018quick",
                             "Where's the case statement in Python?": "ceder2018quick",
                             "The for loop": "ceder2018quick",
                             "The range function": "ceder2018quick",
                             "Controlling range with starting and stepping values": "ceder2018quick",
                             "The for loop and tuple unpacking": "ceder2018quick",
                             "The enumerate function": "ceder2018quick",
                             "The zip function": "ceder2018quick"},
            "Functions" : {"Basic function definitions": "ceder2018quick",
                           "Positional parameters": "ceder2018quick",
                           "Default values": "ceder2018quick",
                           "Passing arguments by parameter name": "ceder2018quick",
                           "Variable number of arguments": "ceder2018quick",
                           "Dealing with an indefinite number of positional arguments": "ceder2018quick",
                           "Dealing with an indefinite number of arguments passed by keyword": "ceder2018quick",
                           "Mutable objects as arguments": "ceder2018quick",
                           "Local and global variables": "ceder2018quick",
                           "lambda expressions": "ceder2018quick",
                           "Generator functions": "ceder2018quick",
                           "More generator functions" : "danjou2018serious",
                           "Type Hints" : "sweigart2020beyond"},
            "List-dict-comp" : {
                          "List and dictionary comprehensions" :  "ceder2018quick",
                          "Multiple for statement" : "danjou2018serious",
                          "Generator expressions" :  "ceder2018quick",
                          "Functional Programming": "sweigart2020beyond",
                          "Side effect" : "sweigart2020beyond",
                          "Higher-Order Functions" : "sweigart2020beyond",
                          "Applying functions to items with map()" : "danjou2018serious",
                          "Filtering List with filter()": "danjou2018serious",
                          "Finding items that satisfy conditions with any() and all()": "danjou2018serious",
                          "Python Tricks" : "mayer2020oneliners",
                          "Using list comprehension to find top earners":  "mayer2020oneliners",
                          "Using Generator expressions to find companies that pay below minimum wage" : "mayer2020oneliners"},

            "Numpy" : {
                          "Numpy" : "mayer2020oneliners",
                          "Main memory and caches" : "herlihy20211",
                          "Processors" : "herlihy20211",
                          "Main memory and caches" : "herlihy20211",
                          "L1, L2 and L3 caches" : "robey2021parallel",
                          "Granularity" : "herlihy20211",
                          "Vectorized operations" : "robey2021parallel",
                          "let's get to hands on" : "mayer2020oneliners",
                          "Problem 1" : "mayer2020oneliners",
                          "Working with numpy arrays" : "mayer2020oneliners",
                          "Broadcasting" : "mayer2020oneliners",
                          "Problem 2" : "mayer2020oneliners",
                          "Array types" : "mayer2020oneliners",
                          "Conditional array search" : "mayer2020oneliners",
                          "Reshaping and Resizing" : "johansson10numerical",
                          "Matrix and Vector Operations" : "johansson10numerical"},

            "Pandas" : {
                          "Pandas" : "paskhaver2021pandas",
                          "Importing a data set" : "paskhaver2021pandas",
                          "Manipulating a DataFrame" : "paskhaver2021pandas",
                          "Counting values in a Series" : "paskhaver2021pandas",
                          "Filtering a column by one or more criteria" : "paskhaver2021pandas",
                          "Grouping data" : "paskhaver2021pandas"
            }

           }

output = template.render(content = content)
output = output.replace("{ ","{")
output = output.replace(" }","}")


text_file = open("latex/ref_dmdu_2022_python_course.tex", "w")
text_file.write(output)
text_file.close()
