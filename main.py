import random
import math



#בחרנו לתכנת משחק המדמה דייג המחפש דג במיקום מסוים
#לאחר כל בחירה הוא מקבל מרחק שלו ממיקום הדג כך הוא יכול להתקרב אליו יותר
# במקרה שהדייג ממש מתקשה, הוא יכול לבקש מהלווין מידע לאיזה כיוון להשליך את החכה
# בסוף הדייג יגיע ליעד


#מקרי קצה שטופלו:
#משום שרמז בנוי עפ בחירתו הקודמת של המשתמש 1.
# אתחלנו את העמודה ואת השורה בשביל שהרמז יעבוד גם בבחירה של המשתמש בפעם הראשונה
#כאשר מפרשים את המידע מהקובץ מחלקים למילון עפ הסימן ':' לכן ווידאנו שהמשתמש הכניס רק אותיות לשמו 2.
# בדקנו שכאשר ממירים את הקובץ למילון שלא ינסה להמיר שורה ריקה .3
#כמו כן, השחקן יכול להכניס טור ושורה רק בתוך גודל המטריצה


# prints a matrix nicely
def print_mat(mat):
    for i in mat:
        formatted_row = " ".join(f"{num:>{size}}" for num in i)
        print(formatted_row)##


#this finds the distanceof the fish's radius from the players guess
def find_radius(row, column):
    row = int(row)
    column = int(column)
    if (fish == matrix[row ][column ]):
        return 0
    else:
        matrix[row][column ] = "👣"  # good
        c = (fish - 1) % size
        r = int((fish - 1) / size)
        distance = max(math.fabs(column  - c), math.fabs(row - r))
        return int(distance)



#if the player asks for a hint this give him a hint
#saying to go up , down , right or left according to the last guess
def give_a_hint():

    cfish = int((fish - 1) % size)
    rfish = int((fish - 1) / size)
    if column == cfish:
        if rfish > row:
            print(" ↓ ")
        else:
            print(" ↑ ")
    else:
        if cfish < column:
            print(" ← ")
        else:
            print(" → ")


#gets the players guess and makes sure it is a valid
def get_column():#
    col = input("Please enter column, enter '?' for a hint ")
    while (col == "?" or col.isnumeric() == False or int(col) < 1 or int(col) > size):
        if col == "?":
            give_a_hint()
            col = input("Please enter column, enter '?' for a hint ")
        else:
            col = input("Please re-enter the selected column must be smaller than " + str(size) + " enter '?' for a hint ")
    return int(col)-1

def get_row():
    r = input("Please enter row ")
    while (r.isnumeric() == False or int(r) < 1 or int(r) > size):
        r = input("Please re-enter the selected row must be smaller than " + str(size))
    return int(r)-1



#main

name = input("Welcome, please enter your name for identification ")
while(not name.isalpha()):
    name=input("Your name must only contain alphabetical letters")

size = input("Please enter the fishing area (length and depth) ")
while (size.isnumeric() == False):
    size = input("Please re-enter the area")
size = int(size)

matrix = [["💦" for j in range(1, size + 1)] for i in range(1, size + 1)]  # building the area of the game

fish = int(random.randint(1, size * size))
print_mat(matrix)
scores = {}#this will hold all the players that ever played with all the high scores
count = 0#this counts all the tries the player had
column = 0#initialized with 0
row = 0
# the actual game
while (True):
    count += 1
    column = get_column()
    row = get_row()
    distance = find_radius(row, column)
    if distance == 0:
        break
    print("The radius distance is: " + str(distance))
    print_mat(matrix)

# once the game is finished
matrix[int((fish - 1) / size)][(fish - 1) % size] = "🐠"
print_mat(matrix)
print("Good Job! You stepped " + str(count) + " steps, your score is: "+str((10-count)*10)+" !!")

try:
   with open("data.txt", 'r') as file:
      content = file.read()
except Exception as e:
    print("The file does not exist")
    exit()

fullplayer = content.split('\n')
for p in fullplayer:
   if p == "":
       pass
   else:
     name1,score = p.split(':')
     scores[name1.strip()] = str(score.strip())


if scores.get(name)== None:
    scores[name]=(10-count)*10
else:
    if int(scores[name]) < (10-count)*10:
        scores[name] = (10-count)*10
        print("Your broke your high score! The new high score is: "+str((10-count)*10)+"!!")

updated=""
for k,v in scores.items():
    updated=updated+k+": "+str(v)+"\n"

try:
  with open("data.txt",'w') as file:
     file.write(updated)
except:
    print("We are fixing the program, but in the meantime -you are great!!")
    exit()



