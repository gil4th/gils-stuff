#Takes your age and when you have kids and you can tell it when roughly what year a
#generation is going to be born. Also you can enter a year and it will tell you (with some #assumptions) how many decedents you are going to have
choice_1 = ""
choice_2 = ""
def get_gen(gen_num , kid_names , kid_gen ,kid_age , 	age , had_kid_age , year_born):
   had_kid_age = int(had_kid_age)
   year_born = int(year_born)
   gen_num = int(gen_num)
   
   if had_kid_age == 0:
      print("since you haven't had any kids and you aren't planning to have any kids im just assuming that your first kid is when your 27 since thats the national average")
      had_kid_age = 27
   x = 0
   thing = 0
   y = had_kid_age + year_born
   while True:
      if kid_gen[ thing ] == gen_num:
            break
      #loops for every 5 generations since thats how many names we have and then adds 5 to each num in kid_gen so it just goes untill it hits gen_num
      for i in range(len(kid_gen)):
         print("year :", y)
         print("gen", kid_names[ i ] ,":", kid_gen[ i])
         y += had_kid_age
         if (kid_gen[ i ] == gen_num) or (kid_gen[i] > gen_num ):
            thing = i
            break
      #continues it for the next batch of generations
      if kid_gen[ thing ] == gen_num:
            break 
      for p in range(len(kid_gen)):
         kid_gen[ p ] = int(kid_gen[p]) + 5
   return(y)

def get_gen_year(gen_year,had_kid_age,num_decendents,year_born):
   i = int(year_born)
   i_2 = int(0) - had_kid_age
   if num_decendents == 0:
      print("since you dont have any kids or are not planning to have any im just assuming you have 2 since thats the national average")   
      num_decendents = 2
   while i != gen_year:
      i += 1
      i_2 += 1
      if i_2 == had_kid_age:
         num_decendents *= 2
         print("you have",num_decendents,"decendents at year",i)
         i_2 = 0
   print("So by the year ", gen_year," you will have",num_decendents,"decendents!")
def main():   
   choice_1 = ""
   while choice_1 != "quit":
      print("hey this program will take your age and when you plan to have kids (or when you did) and making some assumptions like the average age people have kids\nthen tell you at what year a generation of your choice will be born.\nOr you can also enter a year and it will compute how many decedents you are going to have by then")
      print("do you want to do that? If not type Quit, if not type literally anything other than that!")
      choice_1 = input()
      
      if choice_1 == "quit":
         break
      choice_1 = ""
      print(" tubular, now do you want to do")
      print("1) figure out at what year a generation is going to be")
      print("2) figure out how many decedents you are going to have by a certain year. Please give the integer of the choice you made")
      choice_2 = input()
      while ((choice_2 != "1" ) and (choice_2 != "2")):
         print("yo pick either choice one or two please!")
         print("1) figure out at what year a generation is going to be")
         print("2) figure out how many decedents you are going to have by a certain year. Please give the integer of the choice you made")
         choice_2 = input()
      print("if you don't mind could tell me when you were born, in an integer please")
      year_born = input()
      year_born = int(year_born)
      print("if you don't mind once more could you tell me at what year it was when you are planning to have kids,\nor if you already have kids what year did you have the first one?\nAs just a integer for the year. And if you dont have any kids or arent planning to have kids just input 0!!")
      year_kids_str = input()
      year_kids = int(year_kids_str)
      #this checks if you input the year you are planning/had kids and sees if its before you were born, because if so that messes up all the math
      while (year_kids <= year_born) and (year_kids != 0):
            print("yo how could you have a kid before you are even born? input a new year please!")
            year_kids_str = input()
            year_kids = int(year_kids_str)
      num_kids = 2      
      if year_kids != 0:
         print("how many kids are you planning to have/ had already? As an integer please")
         num_kids_str = input()
         num_kids = int(num_kids_str)
      #it doesnt matter if you pick 1 or 2 you will still need to ask for the year born the and the kids year born and the number of kids 
      
      if choice_2 == "1":
         age = 2025 - int(year_born)
         if year_kids == 0:
            had_kid_age = 27
            kid_age = 0
         else: 
            kid_age = 2025 - int(year_kids)
            had_kid_age = int(age) - int(kid_age)
         #this gets us all the numbers and ages and variables that we need at the moment 
         print("so you chose choice one ! Hey now tell me 5 names, the first 	name of your kid, the second of your kids kid and so on.")
         kid_names = [0,0,0,0,0]
         kid_gen = [0,0,0,0,0]
         #this is a parellel array for the kid names to have an array that hold the generation of the name
         for i in range(len(kid_names)):
            print("name ", i + 1 , " : ")
            kid_names[ i ] = input()
            kid_gen[ i ] = int(i + 1)
         #this will fill the array with the names of the generations   
         print("now the fun part. Now give me a generation number, and ill tell you the year ! ")
         gen_num = input()
         gen_num = int(gen_num)
         gen_year = get_gen(gen_num , kid_names , kid_gen ,kid_age , 	age , had_kid_age , year_born)
         print("the year for generation ",gen_num," was", gen_year)
         choice_2 = ""
         #this is the end of the first choice 
      if choice_2 == "2":
         age = 2025 - int(year_born)
         if year_kids == 0:
            had_kid_age = 27
            kid_age = 0
            print("since you haven't had any kids and you arent planning to have any kids im just assuming that your first kid is when your 27 since thats the national average") 
         else: 
            kid_age = 2025 - int(year_kids)
            had_kid_age = int(age) - int(kid_age)
         print("so you chose choice two ! Give me a year, and i will tell you how many decedents you will have in that year\nUsing some approximations of course, having a kid every", had_kid_age, "years and the average family in america has 2 kids\nso every one of your kids will have two kids and so on. So what year would you like to input?")
         
         gen_year_str = input()
         gen_year = int(gen_year_str)
         if year_kids >= gen_year:
            while year_kids >= gen_year:
               print("yo pick a new year that is after the year you had kids!")
               gen_year_str = input()
               gen_year = int(gen_year_str)
         num_decendents = num_kids
         get_gen_year(gen_year,had_kid_age,num_decendents,year_born)
         choice_2 = 0
         #ends the second choice

main()