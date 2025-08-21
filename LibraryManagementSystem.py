library={
    "Harry Potter":("J.K Rowling",True),
    "The Hobbit":("J.R.R. Tolkien",True),
    "1984":("George Orwell",False)
}

def view_books():
    print("\n Available Books")
    for title,(author,available)in library.items():
        if available==True:
            print("Available")
        else:
            print("Not Available")
        print(f"{title} by {author} is {available}.")

def borrow_book():
    try:
        book=input("Enter book you want to borrow:")
        if book not in library:
            raise KeyError("Book not available in library!")
        author,available=library[book]
        if available:
            library[book]=(author,False)
            print(f"You have borrowed '{book}'. ")
        else:
            print(f"Sorry!, '{book}' is not available for borrowing.")

    except KeyError as e:
        print(f"Error! {e}")

    
    

