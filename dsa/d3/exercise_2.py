def main():
    s = "race a car"
    print(palindrome(s))

def palindrome(string):
    #clean_s = ""
    clean_list = []
    for i in string:
       if i.isalpha() or i.isdigit():
           #clean_s += i.lower()
            clean_list.append(i)
    clean_string = "".join(clean_list)
    left = 0
    right = len(clean_string)-1
    print(clean_string)
    while left < right:

        if clean_string[left] != clean_string[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == "__main__":
    main()