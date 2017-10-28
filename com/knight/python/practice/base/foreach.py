# encoding: utf-8
import wester

movies = ['The Holy Grall',1975,'Terry Gilliam',91,"Terry Jones & Terry Goilliam",91,
          ['Graham Charpman',['Michael Palin','John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]];

print("----------origin data-----------")
for each_item in movies:

    if isinstance(each_item,list):
         for nested_item in each_item:
             print(nested_item)
    else:
        print (each_item)

print("----------finally data-----------")

wester.print_lol(movies)