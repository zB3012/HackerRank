def count_substring(string, sub_string):
    count = 0
    i=0
    while True:
        x = string.find(sub_string, i)
        if x==-1:
            break
        count+=1
        i=x+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)