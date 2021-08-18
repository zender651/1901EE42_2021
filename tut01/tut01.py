def meraki_helper(n):  # Defining the meraki_helper function
    given_no = n       
    last_digit = given_no % 10
    given_no = int(given_no/10)
    curr_diff=0
    curr_no=0
    while given_no != 0:    # loop for traversing digits of the number
        curr_no = given_no % 10
        curr_diff = abs(curr_no - last_digit)
        last_digit = curr_no
        given_no = int(given_no/10)
        if curr_diff != 1:
            print("No, {} is not a Meraki number".format(n))
            return False
 
    print("Yes - {} is a Meraki number".format(n))       
    return True


input = [12, 14, 56, 78, 98, 54, 678, 134,                #given input list
         789, 0, 7, 5, 123, 45, 76345, 987654321]

meraki_count = 0  # counting the no of meraki numbers
for n in input:
    if meraki_helper(n):
        meraki_count += 1

print('the input list contains {} meraki and {} non meraki numbers.'.format(
    meraki_count, len(input)- meraki_count))
