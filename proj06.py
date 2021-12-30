#################################################################################################################################
# 
# CSE 231
# Project 6
#
# Algorithm
#
#   function open_file():
#       prompt for a file_name
#       while loop to repeatedly prompt for a file_name:
#           use try-except method to prevent the program from running errors
#           try :
#               break from the loop if a file is successfully opened
#           except:
#               print Invalid filename  and prompt for a file name
#               go back to the while loop to start from the beginning
#       return file_pointer
# 
#   function read_file(fp):
#       assign file_pointer to a variable such as reader
#       skip the header row using readline()
#       create a master_list = []
#       for loop through the file_pointer:
#           append the elements from the file_pointer to master_list
#       return sorted master_list (list of list)
#
#
#   function process_file(master_list of list)
#       for loop through the master_list:
#           asign c = ' '
#           if there is white space between first name and last name, find the index to slice
#               assign last name using the index value (slice method)
#               assign first name using the  index value (slice method)
#           assign n = " "
#           if there is a white space after last name , find the index
#               assign last name to element before the white space using index (slice method)
# 
#       for loop through the master_list:
#           for loop through the range(from 4, to length of master_list)
# 
#               if the element is empty:
#                   assign the element = 0.0
# 
#               else:
#                   assign all elements from index 4 as float
# 
#       return sorted(master_list) (list of list)
#       
#   function get_team_list(master_list)
# 
#       create a teams_list
#       for loop through the master_list:
#           append elements of index[2] from master_list to teams_list
#           create a team_list
#       remove team's name that appears twice, team's name should only appear once
#       for loop through teams_list:
#           if element of teams_list is not in team_list:
#           append the element to team_list
#       return sorted team_list
#
#   function get_players_on_team (master_list,team)
# 
#       assign team to string
#       create a team_list []   
#       for loop through the masters_list:        
#         if index[2] == team (the input from the user )           
#             append first name and last name to team_list          
#     return sorted(team_list)
# 
#   function get_top_ten(master_list,stat) 
# 
#       create a stat_list    
#       for loop through master_list:
#           create if-else statements to add stat,lastname,firstname to stat_list based on user input
#           For example: 
#           if state = "GP":
#               append index of stat, last name, first name to the stat_list
#           repeat the if-elif statements for other stats
# 
#     sort the stat_list and reverse it, so the list is in descending order 
#     create a real_list []
#     create variable count = 0
#     for loop through the stat_list:
#         remove all the elements except keep the 10 largest elements 
#         append item to real_list form stat_list 
#         update count by adding 1
#         when count is more than 10 break the loop
# 
#     return real_list
# 
#   function get_bottom_ten(master_list,stat)
# 
#       create a stat_list    
#       for loop through master_list:
#           create if-else statements to add stat,lastname,firstname to stat_list based on user input
#           For example: 
#           if state = "GP":
#               append index of stat, last name, first name to the stat_list
#           repeat the if-elif statements for other stats
# 
#     sort the stat_list and reverse it, so the list is in descending order 
#     create a stat1_list []
#     create variable count = 0
#     for loop through the stat_list:  
#       if the element is 0.0
#           continue (skip it)
#       remove all the elements except keep the 10 lowest elements 
#       append item to real_list form stat_list 
#       update count by adding 1
#       when count is more than 10 break the loop
# 
#     return stat1_list
# 
#   function get_players_in_position(master_list,position)
#       create a position_list []   
#       for loop through master_list:       
#           if position == index of position from master_list:           
#            append the element to position_list by combining lastname and first name as one element           
#       create real_list []   
#       for loop through position_list:       
#         append the elements from position_list to real_list (so we can get just one list, not list of list )      
#  
#       return sorted(real_list) (list)
# 
#   function main():
#       call the function open_file() to get the text file
#       then call the function display_options() to print all the prompts 
#       prompt the user for an option
#       create a  while loop with condition that if the user enters enters q then the program ends
#           assign answer as int
#           Create If statements based on the user input for answer
#           assign check = False
#           If answer == 1:
#               prompt the user to enter a stat
#               create a while loop if the user entered an invalid statistic
#                   assign check = False
#                   print(Invalid error directed by the project)
#                   then break the while loop
#               If check = True (However, if check = False, it wont run this if statement, it will go back and run the display function)
#                   call the get_top_ten function
#                   for loop through the elements of the list returned by calling get_top_ten function
#                       print the solution based on the format firected from the project using the index of the list returned by get_top_ten function
#           
#           elif answer == 2:
#               prompt the user to enter a stat
#               create a while loop if the user entered an invalid statistic
#                   assign check = False
#                   print(Invalid error directed by the project)
#                   then break the while loop
#               If check = True (However, if check = False, it wont run this if statement, it will go back and run the display function)
#                   call the get_bottom_ten function
#                   for loop through the elements of the list returned by calling the get_bottom_ten function
#                       rint the solution based on the format directed from the project using the index of the list returned by get_bottom_ten function
#       
#           elif answer == 3:
#               prompt the user to enter a position
#               create a while loop if the user entered an invalid position
#                   assign check = False
#                   print(Invalid error directed by the project)
#                   then break the while loop
#               If check = True (However, if check = False, it wont run this if statement, it will go back and run the display function)
#                   call the get_players_in_position function
#                   for loop through the elements of the list returned by calling the get_players_in_position function
#                    print the solution based on the format firected from the project
#       
#           elif answer == 4:
#               prompt the user to enter a team
#               create a while loop if the user entered an invalid team
#                   assign check = False
#                   print(Invalid error directed by the project)
#                   then break the while loop
#               If check = True (However, if check = False, it wont run this if statement, it will go back and run the display function)
#                   call the get_players_in_position function
#                   print the format firected from the project
#                   for loop through the elements of the list returned by calling the get_players_on_team function
#                       print every element of the list
# 
#           elif the answer == 5:
#               print the format directed by the project
#               call the function get_team_list
#               for loop through the elements of the list returned by calling the get_team_list function
#                   print every element
# 
#           else:
#               print(Error message directed by the project)
#               prompt the user to pick an option:
#               continue
# 
#       call the display options
#       prompt the user to pick an option
#       continue
# 
# 
###########################################################################################################################################



import csv
from operator import itemgetter

PLAYER ="Last_name, First_name,TEAM,POS,GP,MPG,Usage Rate,Turnover Rate,FTA,FT%,2PA,2P%,3PA,3P%,FG%,PointsPerGame,ReboundsPerGame,AssistsPerGame,StealsPerGame,BlocksPerGame,TurnoversPerGame,Offensive Rating"

def open_file():
    ''' 
    prompt for a file_name
    while loop to repeatedly prompt for a file_name:
        use try-except method to prevent the program from running errors
        try :
            break from the loop if a file is successfully opened
        except:
            print Invalid filename  and prompt for a file name
            go back to the while loop to start from the beginning
            
    return file_pointer

    '''
    
    file_name = input("Input a file: ")
    check = True
    if file_name == "":
        filepointer = ""
        return filepointer
    while check == True:
        try:
            filepointer = open(file_name)
            break
        except FileNotFoundError:
            print("Invalid filename. Please try again.")
            file_name = input("Input a file: ")
            continue
    
    return filepointer

def read_file(fp):
    ''' 
    assign file_pointer to a variable such as reader
    skip the header row using readline()
    create a master_list = []
    for loop through the file_pointer:
        append the elements from the file_pointer to master_list
    
    return sorted master_list (list of list)
        
    '''
    
    reader = csv.reader(fp)   
    fp.readline()
    master_list = []
    
    for line in reader:
        
        master_list.append(line)
        
    
    return sorted(master_list)
    
    
    

def process_file(master_list):
    ''' 
    
     for loop through the master_list:
         
         asign c = ' '
         if there is white space between first name and last name, find the index to slice
             assign last name using the index value (slice method)
             assign first name using the  index value (slice method)
         assign n = " "
         if there is a white space after last name , find the index
             assign last name to element before the white space using index (slice method)
        
        for loop through the master_list:
            for loop through the range(from 4, to length of master_list)
            
            if the element is empty:
                assign the element = 0.0
            
            else:
                assign all elements from index 4 as float
                
        return sorted(master_list) (list of list)
    
    '''
    
    
    
    
    for i in master_list:
        
        c = " "
        if c in i[0]:
            inde = int(i[0].index(c))
            last_name = i[0][inde+1:]
            first_name = str(i[0][0:inde])
            
            i[0] = last_name
            i.insert(1, first_name)
        
        n = " "
        if n in i[0]:
            
            ind = int(i[0].index(n))
            las = i[0] [0:ind]
            i [0] = las

    for i in master_list: 
        
          for j in range(4,len(i)):
            
            if i[j] == "":
                i[j] = 0.0
            else:
                i[j] = float(i[j])
                
       
            
            
 
    return sorted(master_list)

def get_team_list(master_list):
    ''' 
    create a teams_list
    
    for loop through the master_list:
        
        append elements of index[2] from master_list to teams_list
        
    
    create a team_list
    
    remove team's name that appears twice, team's name should only appear once
    for loop through teams_list:
        
        if element of teams_list is not in team_list:
            append the element to team_list
        
    return sorted team_list
    
    '''
    
    
    teams_list = []
    for i in master_list:
        
        
        
        teams_list.append(i[2])
        
        
    team_list =  []
    
    for i in teams_list:
       
        if i not in team_list:
            team_list.append(i)
        
        
    return sorted(team_list)
        
    
    
              
            
def get_players_on_team (master_list,team):
    ''' 
    assign team to string
    create a team_list
    
    for loop through the masters_list:
        
        if index[2] == team (the input from the user )
            
            append first name and last name to team_list
            
    return sorted(team_list)
    
    '''
    
    team = str(team)
    team_list = []
    
    for i in master_list:
        
        
            
        if i[2] == team:
            
            
            team_list.append(i[0] + ", "  + i[1] )
    
    return sorted(team_list)
            


def get_top_ten (master_list,stat):
    ''' 
    create a stat_list
    
    for loop through master_list:
        create if-else statements to add stat,lastname,firstname to stat_list based on user input
        For example: 
        if state = "GP":
            append index of stat, last name, first name to the stat_list
        repeat the if-elif statements for other stats
        
    sort the stat_list and reverse it, so the list is in descending order
    
    
    create a real_list []
    create variable count = 0
    for loop through the stat_list:
        remove all the elements except keep the 10 largest elements 
        append item to real_list form stat_list 
        update count by adding 1
        when count is more than 10 break the loop
    
    return real_list
    
    '''
    
    
    stat_list = []
    
    
    for i in master_list:
        
        if stat == "GP":
            stat_list.append([i[4],i[0],i[1]])
            
        elif stat == "MPG":
            stat_list.append([i[5],i[0],i[1]])
            
        elif stat == "Usage Rate":
            stat_list.append([i[6],i[0],i[1]])
            
        elif stat == "Turnover Rate":
            stat_list.append([i[7],i[0],i[1]])
            
        elif stat == "FTA":
            stat_list.append([i[8],i[0],i[1]])
        
        elif stat == "FT%":
            stat_list.append([i[9],i[0],i[1]])
            
        elif stat == "2PA":
            stat_list.append([i[10],i[0],i[1]])
        
        elif stat == "2P%":
            stat_list.append([i[11],i[0],i[1]])
        
        elif stat == "3PA":
            stat_list.append([i[12],i[0],i[1]])
            
        elif stat == "3P%":
            stat_list.append([i[13],i[0],i[1]])
            
        elif stat == "FG%":
            stat_list.append([i[14],i[0],i[1]])
            
        elif stat == "PointsPerGame":
            stat_list.append([i[15],i[0],i[1]])
            
        elif stat == "ReboundsPerGame":
            stat_list.append([i[16],i[0],i[1]])
            
        elif stat == "AssistsPerGame":
            stat_list.append([i[17],i[0],i[1]])
            
        elif stat == "StealsPerGame":
            stat_list.append([i[18],i[0],i[1]])
            
        elif stat == "BlocksPerGame":
            stat_list.append([i[19],i[0],i[1]])
            
        elif stat == "TurnoversPerGame":
            stat_list.append([i[20],i[0],i[1]])
            
        elif stat == "Offensive Rating":
            stat_list.append([i[21],i[0],i[1]])
        
    stat_list.sort(reverse = True)
    
    real_list = []
    count = 0
    for i in  stat_list:
        
        
        if count < 10:
            real_list.append(i)
            count += 1
            
        else:
            break
    
      
    return real_list

def get_bottom_ten (master_list,stat):
    ''' 
    
    create a stat_list
    
    for loop through master_list:
        create if-else statements to add stat,lastname,firstname to stat_list based on user input
        For example: 
        if state = "GP":
            append index of stat, last name, first name to the stat_list
        repeat the if-elif statements for other stats
        
    sort the stat_list 
    
    
    create a stat1_list []
    create variable count = 0
    for loop through the stat_list:
        if the element is 0.0, 
            continue (skip it)
        
        remove all the elements except keep the 10 smallest elements 
        append item to real_list form stat_list 
        update count by adding 1
        when count is more than 10 break the loop
    
    return stat1_list
    
    '''
    
    
    stat_list = []
    
    
    for i in master_list:
        
        if stat == "GP":
            stat_list.append([i[4],i[0],i[1]])
            
        elif stat == "MPG":
            stat_list.append([i[5],i[0],i[1]])
            
        elif stat == "Usage Rate":
            stat_list.append([i[6],i[0],i[1]])
            
        elif stat == "Turnover Rate":
            stat_list.append([i[7],i[0],i[1]])
            
        elif stat == "FTA":
            stat_list.append([i[8],i[0],i[1]])
        
        elif stat == "FT%":
            stat_list.append([i[9],i[0],i[1]])
            
        elif stat == "2PA":
            stat_list.append([i[10],i[0],i[1]])
        
        elif stat == "2P%":
            stat_list.append([i[11],i[0],i[1]])
        
        elif stat == "3PA":
            stat_list.append([i[12],i[0],i[1]])
            
        elif stat == "3P%":
            stat_list.append([i[13],i[0],i[1]])
            
        elif stat == "FG%":
            stat_list.append([i[14],i[0],i[1]])
            
        elif stat == "PointsPerGame":
            stat_list.append([i[15],i[0],i[1]])
            
        elif stat == "ReboundsPerGame":
            stat_list.append([i[16],i[0],i[1]])
            
        elif stat == "AssistsPerGame":
            stat_list.append([i[17],i[0],i[1]])
            
        elif stat == "StealsPerGame":
            stat_list.append([i[18],i[0],i[1]])
            
        elif stat == "BlocksPerGame":
            stat_list.append([i[19],i[0],i[1]])
            
        elif stat == "TurnoversPerGame":
            stat_list.append([i[20],i[0],i[1]])
            
        elif stat == "Offensive Rating":
            stat_list.append([i[21],i[0],i[1]])
        
    
    
    real_list = []
    real_list = sorted(stat_list)
    
    stat1_list = []
    count = 0
    for i in  real_list:
        
        if i[0] == 0.0 :
            
            continue
            
            
        
        elif count < 10:
            stat1_list.append(i)
            count += 1
            
        else:
            break
    
      
    return stat1_list
    
    
    
def get_players_in_position (master_list,position):
    ''' 
    create a position_list []
    
    for loop through master_list:
        
        if position == index of position from master_list:
            
            append the element to position_list by combining lastname and first name as one element
            
    create real_list []
    
    for loop through position_list:
        
        append the elements from position_list to real_list (so we can get just one list, not list of list )
        
    return sorted(real_list) (list)
        
    '''
    
    position_list = []
    
    
    for i in master_list:
        
        if position in i[3]:

            position_list.append([i[0]+ ", " + i[1]])
            # position_list.append(i[1])
            
    
    real_list =  []
    for i in position_list:
        
         real_list.append(i[0])
        
    
    return sorted(real_list)
  
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Top 10 players for a statistic 
    2: Bottom 10 players for a statistic
    3: Get players for a position 
    4: Get players on a team
    5: Get list of teams\n"""
    print(OPTIONS)
   

def main():
    
    fp = open_file()
    mas_list = read_file(fp)
    
    master_list = process_file(mas_list)
    
    display_options()
    
    answer = input("Choose an option, q to quit: ")
    answer.lower()
    
    while answer != "q" and answer != "Q":
        if answer.isdigit():
            answer = int(answer)
            
            if answer == 1:
                
                    
                stat = input("Enter the statistic: ")
                
                Check = True
                while stat != "GP" and stat != "MPG" and stat != "Usage Rate" and stat != "Turnover Rate" and stat != "FTA" and stat != "FT%" and stat != "2PA" and stat != "2P%" and stat != "3PA" and stat != "3P%" and stat != "FG%" and stat != "PointsPerGame" and stat != "ReboundsPerGame" and stat != "AssistsPerGame" and stat!= "StealsPerGame" and stat != "BlocksPerGame" and stat != "TurnoversPerGame" and stat != "Offensive Rating":
                    print("Valid statistic not entered.")
                    Check = False
                    break
                    
                
                if Check == True: 
                
                    print()
                    print("{:<25} {:<10}".format("Player", stat))
                    top_ten = get_top_ten(master_list,stat)
                    for i in top_ten:
                        
                        print("{:<25} {:<10,.2f}".format(i[1] + ", "+ i[2],i[0]))
                            
                        
                
            elif answer == 2:
                
                stat1 = input("Enter the statistic: ")
                
                check1 = True
                while stat1 != "GP" and stat1 != "MPG" and stat1 != "Usage Rate" and stat1 != "Turnover Rate" and stat1 != "FTA" and stat1 != "FT%" and stat1 != "2PA" and stat1 != "2P%" and stat1 != "3PA" and stat1 != "3P%" and stat1 != "FG%" and stat1 != "PointsPerGame" and stat1 != "ReboundsPerGame" and stat1 != "AssistsPerGame" and stat1 != "StealsPerGame" and stat1 != "BlocksPerGame" and stat1 != "TurnoversPerGame" and stat1 != "Offensive Rating":
                    print("Valid statistic not entered.")
                    check1 = False
                    
                    break
                    
                if check1 == True:   
                    print()
                    print("{:<25} {:<10}".format("Player", stat1))
                    bottom_ten = get_bottom_ten(master_list,stat1)
                    for i in bottom_ten:
                        
                        print("{:<25} {:<10,.2f}".format(i[1] + ", "+ i[2],i[0]))
                        
                        
                    
                
            elif answer == 3:
                pos = input("Enter the position: ")
                check2 = True 
                
                while pos != "G" and pos != "C" and pos!= "F":
                    print("Valid position not entered.")
                    check2 = False
                
                    break
                    
                if check2 == True:   
                    
                    print("{:<10} {:<10}".format("Position: ", pos))
                    position = get_players_in_position(master_list,pos)
                    for i in position:
                        
                        print(i)
                    
                    
            elif answer == 4:
                    
                t = input("Enter the team: ")
                check3 = True
                while t != "Bos" and t != "Bro" and t != "Dal" and t != "Den" and t != "Hou" and t != "Ind" and t != "Lac" and t != "Lal" and t != "Mia" and t != "Mil" and t != "Okc" and t != "Orl" and t != "Phi" and t != "Por" and t != "Tor" and t != "Uta":
                    print("Valid team not entered.")
                    check3 = False
                    break
                
                if check3 == True:   
                    
                    print("{:<10} {:<10}".format("Team: ", t))
                    players = get_players_on_team(master_list, t)
                    
                    for i in players:
                        
                        print(i)
                        
                      
            elif answer == 5:
                print("\nTeams\n")
                team = get_team_list(master_list)
                
                for i in team:
                    
                    print(i)
            
            else:
                print("Error: incorrect option, please try again.")
                answer = input("Choose an option, q to quit: ")
                continue
                
                
        display_options()
        answer = input("Choose an option, q to quit: ")
        answer.lower()
        continue
            
                    
        
                 
        
                 

if __name__ == '__main__':
    main()