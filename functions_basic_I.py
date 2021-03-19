# #1
# def a():
#     return 5
# print(a())      #I predict that it will print 5  CORRECT


# #2
# def a():
#     return 5
# print(a()+a())  # i predict that it will give us back 10 CORRECT

#3
# def a():
#     return 5
#     return 10
# print(a())  #It's gonna be 5 because first come first served CORRECT


# #4
# def a():
#     return 5
#     print(10)
# print(a())  #gonna be 5 because of the return statement, not the print CORRECT


#5
# def a():
#     print(5)
# x = a()
# print(x)   # it's gonna be 5 because it prints 5, therefore a is 5, therefore x is 5 HALF RIGHT.  I'm not sure why x does not also equal 5


# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))  #i predict 8.  INCORRECT.  It gave b and c, but not the sum...


# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))                   # i predict that it's gonna be nan or something because those are int not str. INCORRECT
#                                 # oh i get it.  it CONCAT rather than added them


# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# ok lets see: gonna print b (100), print 10, then 100 again, maybe the 7 in the middle? HALF RIGHT
#ok so, it printed b, then it returned 10.  skipped 7 because FCFS, then a was never really defined was it?


# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# # 7, 14, 14. HALF RIGHT....where did the 21 come from??? oh i get it....


# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
 #   8 because FCFS CORRECT


# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
#             # 500, 500, 500, 500.  I never understand why the 3rd one is 300....oh bc like 86 and 89 as in a is now...i keep confusing it with b

# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# # 500, 500, 300 500  CORRECT

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# # 500 500 500, 300  HALF RIGHT, #3 was 300 because 109 and 112 i think??


# #14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# # 1,2,3?? WRONG.  ah trick question bc nothing really called


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# ok so 10, 5, 10, 10? WRONG.  ok so it prints 1, sets a, prints 3, sets b, i have no idea how the 5 comes into play 



















