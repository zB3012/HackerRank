def split_and_join(line):
    lineone=line.split(" ") # Split the string 
    linetwo = "-".join(lineone) # Join the string
    return linetwo
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)