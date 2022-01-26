# STUDENT NAME: SHRUTI PAGHADAL
# STUDENT ID: 20CE065
# AIM: Find runner-up from given list

print("\n------------------------------------PRACTICAL 4------------------------------------------------------------\n")
if __name__ == '__main__':
    # The first line contains n. n denotes the total number of scores.
    n = int(input("\nEnter the number of scores:"))
    # The second line contains an array A[]  of n integers each separated by a space.
    print("\nThe list of scores is:")
    array = map(int, input().split())
    array=sorted(array,reverse=True)
    for i in range(len(array)):
        if array[i]==array[0]:
            continue
        else:
            print("\nThe Runner up score is:",array[i])  
            break
print("\n------------------------------------------END OF PRACTICAL 4--------------------------------------------------------\n")