def main():
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == 'done' : break
        try:
            int(num)
        except:
            print("Invalid Input")
            continue
        if largest == None or int(num) >= largest:
            largest = int(num)
        if smallest == None or int(num) <= smallest:
            smallest = int(num)
    
    print("Maximum is", largest)
    print("Minimum is", smallest)

if __name__ == "__main__":
    main()
