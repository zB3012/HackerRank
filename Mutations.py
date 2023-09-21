def mutate_string(string, position, character):
    sone = list(string)
    sone[position] = character
    s_new = ''.join(sone)
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    
    print(s_new)