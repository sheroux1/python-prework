import prework

my_list = [100001,100002,100003]
print(prework.is_consecutive(my_list))

#   last_number = a_list[0] # We will use this one as the trailing comparison (otherwise lots of index errors)
#     for current_num in a_list:
#         if current_num == last_number: # Need to iterate through the first time so current_num increments and last_num doesn't
#             continue
#         elif current_num-1 == last_number: # Bulk of the work, checks to see if they incremented or not. 
#             cons_bool = True
#             last_number += 1
#             continue
#         else:
#             cons_bool = False
#             break






# next_number = a_list[1]
#     print(a_list[next_number])
#     for nums in a_list:
#         if nums+1 == a_list[int(next_number)]:
#             next_number += 1
#             print(nums + " time through")


  # next_place = 1
    # while place < len(a_list):
    #     if a_list[place+1] == a_list[next_place]:
    #         place += 1
    #         next_place += 1
    #         continue
    #     else:
    #         return False
    # return True

    # for num in a_list:
    #     if (num+1) == a_list[int(place)+1]:
    #         place += 1
    #         continue
    #     else:
    #         return False
    #         break
    # return True


    # total_numbers = len(a_list)
    # print(total_numbers)
    # place = 0
    # print(a_list[place+1])
    # print(a_list[place] + 1)
    # while place < total_numbers:
    #     if (a_list[place] + 1 == a_list[place+1]):
    #         place += 1
    #         continue
    #     else:
    #         return False
    # return True