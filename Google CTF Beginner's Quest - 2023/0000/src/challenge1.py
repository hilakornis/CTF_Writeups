



if __name__ == "__main__":
    with open("challenge1.txt", "r") as file:
        file_content = file.read()

    print("hello")
    print(f"file content : {file_content}")
    str = ""

    shift = 13
    # file_content = "SYNT{ebgngr_gung_nycunorg}"
    for i in range(26):
        str = ""
        for c in file_content:
            if ord(c) in range(ord('a'), ord('z') + 1) :
                cd =(( (ord(c) - ord('a') + (i )) % 26)) + ord('a')

                str = str + chr(cd)
            elif ord(c) in range(ord('A'), ord('Z') + 1):
                cd =(( ord(c) - ord('A')+ (i )) % 26) + ord('A')
                str = str + chr(cd)
            else :
                str = str + c

        # print(f"i: {i}")
        if( str.__contains__("FLAG")):
            print(f"i: {i}, This is the str: " + str)
        print(f"i: {i}, This is the str: " + str)


