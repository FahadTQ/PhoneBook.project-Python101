book = {1111111111: "Amal", 2222222222: "Mohammed", 3333333333: "Khadijah", 4444444444: "Abdullah",
        5555555555: "Rawan", 6666666666: "Faisal", 7777777777: "Layla"}
query = None
while query == None:
    try:
        query = int(input("Enter the number of the person you're looking for: "))
        break
    except:
        print("This is invalid number")


def search(query):
    for number in book.keys():
        if number == query:
            return 0
    return 1


if search(query) == 0:
    print(book[query])
else:
    print("Sorry, the number is not found")
