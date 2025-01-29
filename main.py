# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     char_dict = get_num_chars(text)
#     chars_sorted_list = convert_dict_to_list(char_dict)

#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     print()


#     for item in chars_sorted_list:
#         if not item['char'].isalpha():
#             continue
#         print(f"The {item['char']} character has {item['num']} times")

#     print("----End report-----")

# def get_book_text(path):
#     with open(path) as f:
#         return f.read()   
         
# def get_num_words(text):
#     words = text.split()
#     return len(words)
    
  
# def get_num_chars(words):
#     dic = {}
#     for word in words.lower():
#         if word not in dic:
#             dic[word] = 1
#         else:
#             dic[word] += 1
#     return dic     


# def convert_dict_to_list(num_char_dict):
#     sorted_list = []
#     for ch in num_char_dict:
#         sorted_list.append({'char':ch, 'num':num_char_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list


# def sort_on(dic):
#     return dic["num"]




# if __name__ =="__main__":
#     main()


dragons = [
        ("Green Dragon", 0, 0, 1),
        ("Red Dragon", 2, 2, 2),
        ("Blue Dragon", 4, 3, 3),
        ("Black Dragon", 5, -1, 4),
    ]

# def describe(dragon):
#     print(f"{dragon[0]} is at {dragon[1]}/{dragon[2]}")


# for dragon in dragons:
#     describe(dragon)


# for i in range(0, len(dragons)):
#     dragon = dragons[i]
#     other_dragons = dragons.copy()
#     del other_dragons[i]
#     print(f"dragon:{dragon} will breathe fire and the other dragons:{other_dragons} will get hit ")


# for i in range(len(dragons)):
#     dragon = dragons[i]
#     other_dragons = dragons.copy()
#     del other_dragons[i]
#     print(f"dragon:{dragon} will breathe fire and the other dragons:{other_dragons} will get hit ")



# for index, value in enumerate(dragons):
#     dragon = dragons[index]
#     other_dragons = dragons.copy()
#     del other_dragons[index]
#     print(f"dragon:{dragon} will breathe fire and the other dragons:{other_dragons} will get hit ")


# for i in range(0,len(dragons)):
#     print(dragons[i])


# dic = {}
# hairstyles = ["bouffant", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop","pixie"]
# new_prices = [25,35, 15, 15, 30, 45, 30,20]
# lst = []
# for hair, price in zip(hairstyles, new_prices):
#     dic[hair]= price
# for style in dic:
#     if dic[style] <= 25:
#         lst.append(style)
# print(lst)


# cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
# print(cuts_under_30)



# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self,point):
#         x = self.x + point.x
#         y = self.y + point.y 
#         return Point(x,y)

#     def __repr__(self):
#         return f"Point({self.x},{self.y})"
        


# p1 = Point(4, 5)
# p2 = Point(2, 3)
# p3 = p1 + p2
# print(p3)


# class Human:
#     def __init__(self, pos_x, pos_y, speed):
#         self.__pos_x = pos_x
#         self.__pos_y = pos_y
#         self.__speed = speed

#     def move_right(self):
#         out = self.__pos_x + self.__speed
#         return out 

#     def move_left(self):
#         self.__pos_x -= self.__speed

#     def move_up(self):
#         self.__pos_y += self.__speed

#     def move_down(self):
#         self.__pos_y -= self.__speed

#     def get_position(self):
#         return (self.__pos_x, self.__pos_y)

#     def __repr__(self):
#         return f"Human({self.__pos_x}, {self.__pos_y}, {self.__speed})"


# man = Human(1,2,10)
# print(man.move_right())
# print(man.get_position())



# class Wall:
#     armor = 5
#     height = 10 


#     def fortify(self):
#         return self.armor + self.armor 


# my_wall = Wall().fortify() * 5

# print(my_wall)

    
    
