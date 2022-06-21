#print("###################################")
nominee_1 = input("Enter Nominee 1 Name: ")
nominee_2 = input("Enter Nominee 2 Name: ")
nominee_3 = input("Enter Nominee 3 Name: ")
#print("###################################")

# Count vot number
nom_1_values = 0
nom_2_values = 0
nom_3_values = 0

# Voter id who are eligible
voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print("*******Voting Session Is Over!*******")
        if nom_1_values>nom_2_values and nom_1_values>nom_3_values:
            percentage1 = (nom_1_values/num_of_voter)*100
            print(nominee_1,"Has won!", percentage1, "% Votes")
            break
        elif nom_2_values>nom_1_values and nom_2_values>nom_3_values:
            percentage2 = (nom_2_values/num_of_voter)*100
            print(nominee_2,"Has won!", percentage2, "% Votes")
            break
        elif nom_3_values>nom_1_values and nom_3_values>nom_2_values:
            percentage3 = (nom_3_values / num_of_voter) * 100
            print(nominee_3, "Has won!", percentage3, "% Votes")
            break
        else:
            print("Both are equal")
            break

    else:
        voter = int(input("Enter Vote ID: "))
      #  print("###################################")

        if voter in voter_id:
            print("You are voter")
       #     print("###################################")

            voter_id.remove(voter)

            vote = int(input("Enter Your Value 1 or 2 or 3: "))
            if vote == 1:
                nom_1_values += 1
                print("Thank you for casting your vote")
        #        print("###################################")

            elif vote == 2:
                nom_2_values += 1
                print("Thank you for casting your vote")
         #       print("###################################")

            elif vote == 3:
                nom_3_values += 1
                print("Thank you for casting your vote")
          #      print("###################################")

        else:
            print("You are not a voter")

