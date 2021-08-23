input_nums = [3, 4, 1, 6, 3, 3, 9, 0, 0, 0]  # This is the input array list


arr_inval = []   # This will store the invalid inputs
int_excl = 0       # for checking invalid inputs 
for i in input_nums:
    if type(i)!= int:
        int_excl = 1
        arr_inval.append(i)


if(int_excl == 1):
    print("Please enter a valid input list. Invalid inputs detected : ", arr_inval)

else:
    arr_score = []
    def get_memory_score(input_nums) :   # score counting function
        score_count = 0
        for int_excl in input_nums:
            if int_excl in arr_score:
                score_count +=1
            elif len(arr_score) < 5:
                arr_score.append(int_excl)
            else:
                arr_score.append(int_excl)
                arr_score.pop(0)
        return score_count         
    print("Score: ",get_memory_score(input_nums))