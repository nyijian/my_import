import pandas as pd
tweets_df = pd.read_csv('tweets.csv')
#initialize an empty distionary:lang_count
# lang_count = {}
# #extract.column from DataFrame:co
# col = tweets_df['lang']
# #iterate over lang columns in DataFrame
# for entry in col:
#     if entry in lang_count.keys():
#         lang_count[entry] += 1
#     else:
#         lang_count[entry] =1
# print(lang_count)

#Define count_entries()
# def count_entries(df,col_name):
#     lang_count ={}
#     col = df[col_name]
#     for entry in col:
#         if entry in lang_count.keys():
#             lang_count[entry] += 1
#         else:
#             lang_count[entry] = 1
#     return lang_count
#
# result = count_entries(tweets_df,'lang')
# print(result)
#
# # Create a string: team
# team = "teen titans"
#
#
# # Define change_team()
# def change_team():
#     """Change the value of the global variable team."""
#     # Use team in global scope
#     global team
#     # Change the value of team in global: team
#     team = "justice league"
# # Print team
# print(team)
# # Call change_team()
# change_team()
# # Print team
# print(team)

####Python's built-in scope
# import builtins
# x =dir(builtins)
# print('array' in x)

"""
Scopes searched 
Local scope
Enclosing functions
Globals
Built-in
-->LEGB
global or nonlocal
"""

####Nested Functions I
## Define three_shouts
# def three_shouts(word1, word2, word3):
#     """Returns a tuple of strings
#     concatenated with '!!!'."""
#     # Define inner
#     def inner(word):
#         """Returns a string concatenated with '!!!'."""
#         return word + '!!!'
#     # Return a tuple of strings
#     return (inner(word1), inner(word2), inner(word3))
# # Call three_shouts() and print
# print(three_shouts('a', 'b', 'c'))
# ##Nested Functions II
# #Define echo
# def echo(n):
#     def inner_echo(word1):
#         echo_word = word1*n
#         return echo_word
#     return inner_echo
# twice = echo(2)
# thrice = echo(3)
# print(twice("hello"),thrice("hello"))
# ##The keyword nonlocal and nested functions
# # Define echo_shout()
# def echo_shout(word):
#     """Change the value of a nonlocal variable"""
#     # Concatenate word with itself: echo_word
#     echo_word = word * 2
#     # Print echo_word
#     print(echo_word)
#     # Define inner function shout()
#     def shout():
#         """Alter a variable in the enclosing scope"""
#         # Use echo_word in nonlocal scope
#         nonlocal echo_word
#         # Change echo_word to echo_word concatenated with '!!!'
#         echo_word = echo_word + '!!!'
#     # Call function shout()
#     shout()
#     # Print echo_word
#     print(echo_word)
# # Call function echo_shout() with argument 'hello'
# echo_shout('hello')
#
# ####Functions with one default argument
# # Define shout_echo
# def shout_echo(word1, echo=1):
#     echo_word = word1*echo
#     shout_word = echo_word + '!!!'
#     return shout_word
# no_echo = shout_echo('Hey')
# with_echo = shout_echo('Hey',5)
# print(no_echo)
# print(with_echo)
#
# # Define shout_echo
# def shout_echo(word1, echo=1, intense=False):
#     echo_word = word1 * echo
#     if intense is True:
#         echo_word_new = echo_word.upper() + '!!!'
#     else:
#         echo_word_new = echo_word + '!!!'
#     return echo_word_new
# with_big_echo = shout_echo('Hey',echo=5,intense=True)
# big_no_echo = shout_echo('Hey',intense=True)
# print(with_big_echo)
# print(big_no_echo)
# ##Functions with variable-length arguments (*args)
# # Define gibberish
# def gibberish(*args):
#     hodgepodge=str()
#     for word in args:
#         hodgepodge += word
#     return hodgepodge
# one_word = gibberish('luke')
# many_words = gibberish("luke", "leia", "han", "obi", "darth")
# print(one_word)
# print(many_words)
# ##Functions with variable-length keyword arguments (**kwargs)
# def report_status(**kwargs):
#     print('\nBegin: Report\n')
#     for key,value in kwargs.items():
#         print(key+":"+value)
#     print('\nEnd report')
# report_status(name="luke", affiliation="jedi", status="missing")
# report_status(name="anakin", affiliation="sith lord", status="deceased")

# # Define count_entries()
# def count_entries(df, *args):
#     cols_count = {}
#     for col_name in args:
#         col = df[col_name]
#         for entry in col:
#             if entry in cols_count.keys():
#                 cols_count[entry] += 1
#             else:
#                 cols_count[entry] = 1
#     return cols_count
# result1 = count_entries(tweets_df, 'lang')
# result2 = count_entries(tweets_df, 'lang', 'source')
# print(result1)
# print(result2)
#
# #a lambda function
# echo_word = (lambda word1,echo: word1*echo)
# result = echo_word('hey',5)
# print(result)
# #Map() and lambda functions
# # Create a list of strings: spells
# spells = ["protego", "accio", "expecto patronum", "legilimens"]
# shout_spells = map(lambda item:item+'!!!', spells)
# shout_spells_list =list(shout_spells)
# print(shout_spells_list)
# ##Filter() and lambda functions
# # Create a list of strings: fellowship
# fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# result = filter(lambda member: len(member) > 6, fellowship)
# result_list = list(result)
# print(result_list)
# #Reduce() and lambda functions
# # Import reduce from functools
# from functools import reduce
# stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# result = reduce(lambda item1, item2: item1 + item2, stark)
# print(result)

##Error handling by raising an error
# Define shout_echo
def shout_echo(word1, echo=1):
    if echo < 0:
        raise ValueError('echo must be greater than 0')
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    return shout_word
shout_echo("particle", echo=5)


