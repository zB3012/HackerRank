if __name__ == '__main__':
    phoneBook = {}
    n = int(input())
    for i in range(n):
        contact, phone = input().split()
        phoneBook[contact] = phone
    
    for asking in range(n):
        query = input()
        if query in phoneBook.keys():
            print(query + "=" + phoneBook[query])
        else:
            print("Not found")
        
    