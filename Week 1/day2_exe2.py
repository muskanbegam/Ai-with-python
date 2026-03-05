import re
def clean_text(text):
    text = re.sub(r"[^\w\s]", "",text)
    text = text.split()
    text = " ".join(text)
    text = text.lower()
    return text

text = "    hello world!! Welcome to python programming....     "
print(clean_text(text))









# sentence = "   I  li  ke t o e   a t     "
# print(sentence)
# clean_text = sentence.strip(" ")
# print(clean_text)




# from mathopr import add

# print(add(2,3))

# def factorial(num):
#     result = num
#     for i in range(1,num):
#         result = result *i
#     return result    

# def print_fact(num):
#      result = factorial(num)
#      return print(result)

# num = int(input("Enter the number: "))
# print_fact(num)

    

