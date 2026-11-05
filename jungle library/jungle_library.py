


members_info = [
    {'username': 'amir85', 'password': '1234', 'borrowed': '1984'},
    {'username': 'sara85', 'password': '5678', 'borrowed': 'a brief history of time'},
    {'username': 'ali_dev80', 'password': '2468', 'borrowed': 'the great gatsby'},
    {'username': 'john70', 'password': '1357', 'borrowed': 'sapiens'},
    {'username': 'mike75', 'password': '9876', 'borrowed': 'harry potter'},
    {'username': 'emma85', 'password': '4321', 'borrowed': 'the metamorphosis'},
    {'username': 'jhon85', 'password': '4321', 'borrowed': 'none'}

    ]


books = {
    'science': {
        'a brief history of time': {
            'author': 'Stephen Hawking',
            'publication_year': '1988',
            'status': 'borrowed'
        },
        'cosmos': {
            'author': 'Carl Sagan',
            'publication_year': '1980',
            'status': 'available'
        },
        'the selfish gene': {
            'author': 'Richard Dawkins',
            'publication_year': '1976',
            'status': 'available'
        },
        'the gene': {
            'author': 'Siddhartha Mukherjee',
            'publication_year': '2016',
            'status': 'available'
        }
    },

    'fictional': {
        '1984': {
            'author': 'George Orwell',
            'publication_year': '1949',
            'status': 'borrowed'
        },
        'the great gatsby': {
            'author': 'F. Scott Fitzgerald',
            'publication_year': '1925',
            'status': 'borrowed'
        },
        'to kill a mockingbird': {
            'author': 'Harper Lee',
            'publication_year': '1960',
            'status': 'available'
        },
        'the catcher in the rye': {
            'author': 'J. D. Salinger',
            'publication_year': '1951',
            'status': 'available'
        }
    },

    'history': {
        'sapiens': {
            'author': 'Yuval Noah Harari',
            'publication_year': '2011',
            'status': 'borrowed'
        },
        'guns germs and steel': {
            'author': 'Jared Diamond',
            'publication_year': '1997',
            'status': 'available'
        },
        'the silk roads': {
            'author': 'Peter Frankopan',
            'publication_year': '2015',
            'status': 'available'
        },
        'a peoples history of the united states': {
            'author': 'Howard Zinn',
            'publication_year': '1980',
            'status': 'available'
        }
    },

    'story': {
        'the little prince': {
            'author': 'Antoine de Saint-Exupery',
            'publication_year': '1943',
            'status': 'available'
        },
        'animal farm': {
            'author': 'George Orwell',
            'publication_year': '1945',
            'status': 'available'
        },
        'the old man and the sea': {
            'author': 'Ernest Hemingway',
            'publication_year': '1952',
            'status': 'available'
        },
        'the metamorphosis': {
            'author': 'Franz Kafka',
            'publication_year': '1915',
            'status': 'borrowed'
        }
    },

    'fantasy': {
        'the hobbit': {
            'author': 'J. R. R. Tolkien',
            'publication_year': '1937',
            'status': 'available'
        },
        'harry potter': {
            'author': 'J. K. Rowling',
            'publication_year': '1997',
            'status': 'borrowed'
        },
        'the lion the witch and the wardrobe': {
            'author': 'C. S. Lewis',
            'publication_year': '1950',
            'status': 'available'
        },
        'a game of thrones': {
            'author': 'George R. R. Martin',
            'publication_year': '1996',
            'status': 'available'
        }
    }
}



def show_books():
    for genre , book in books.items():
        print("\n======================")
        print(f"\n#Genre : {genre}")
        for THE_book , info_book in book.items():
            if info_book['status'] != 'borrowed':
                print(f'\nTitle : {THE_book}')
                print(f"Author : {info_book['author']}")
                print(f'Publication year : {info_book['publication_year']}')


            else:
                continue

def add_book(genre):
    while True:
        is_duplicate = False

        title = input("Please enter the Title (0 to exit): ")
        if title == '0':
            break

        author = input("Please enter the Author: ")
        publication_year = input("Please enter the Publication year: ")

        genre_titles = books[genre]
        genre_titles = list(genre_titles.keys())

        for t in genre_titles:
            if title == t:
                is_duplicate = True
                break

        if is_duplicate == False:
            books[genre][title] = {
                'author': author,
                'publication_year': publication_year,
                'status': 'available'
            }

            print(f"\n{title} successfully added to the library")
            return

        else:
            print("\nWe do not accept duplicates")

def search_book(genre , title):
    for book in list(books[genre]):
        if book == title:
            searched_book_info = books[genre][book]
            return [title , searched_book_info]
    return 'notfound'

def is_genre_valid(genre_name):
    is_valid = False
    genres = list(books.keys())
    for g in genres:
        if g == genre_name:
            is_valid = True
            break
    return is_valid

while True:


    print("Hello and welcome to jungle library")

    print("\nPleas select one of the options")
    print("\n1.Login\n2.Sign up")
    before_start = input("\nEnter your pick here:")
    if before_start == '1':
        is_member_valid = False
        username = input("\nEnter your username(0 to exit):")
        if username == '0':
            continue
        password = input("\nEnter your password:")
        for member in members_info:
            if member['username'] == username and member['password'] == password:
                is_member_valid = True
                break
        if is_member_valid:
            while True:

                print("\n1.Add a Book\n2.Show Available Books\n3.Search\n4.Return Book\n5.Exit")

                start = input("\nEnter your pick here:")

                if start == '1':
                    which_g = input("\nWhich genre is the book(0 to exit):")
                    if which_g == '0':
                        continue
                    if is_genre_valid(which_g) ==  False:
                        print("============================\nThe genre is not valid!!\n============================")
                    else:
                        add_book(which_g)
                elif start == '2':
                    show_books()
                elif start == '3':
                    search_book_genre = input("\nWhich genre is the book(0 to exit):")
                    if search_book_genre == '0':
                        continue
                    if is_genre_valid(search_book_genre):
                        search_book_title = input("\nWhat is the  title:")
                        searched_book_reult = search_book(search_book_genre,search_book_title)
                        if searched_book_reult == 'notfound':
                            print("============================\nBook not found!!\n============================")
                        else:
                            print("\nSearched book information:")
                            print("\nTitle : ", searched_book_reult[0])
                            print("Author :", searched_book_reult[1]['author'])
                            print("Publication year : ", searched_book_reult[1]['publication_year'])
                            print("Status : " , searched_book_reult[1]['status'])
                            if searched_book_reult[1]['status'] == 'available':
                                while True:
                                    print("\nPleas select one of the options")
                                    print("\n1.borrow the book\n2.exit")
                                    after_search = input("\nEnter your pick here:")
                                    if after_search == '2':
                                        break
                                    elif after_search == '1':
                                        for i in range(len(members_info)):
                                            if members_info[i]['username'] == username:
                                                if members_info[i]['borrowed'] == 'none':
                                                    books[search_book_genre][searched_book_reult[0]]['status'] = 'borrowed'
                                                    members_info[i]['borrowed'] = searched_book_reult[0]
                                                    print(f"\n{searched_book_reult[0]} successfully borrowed from the library")
                                                    break
                                                else:
                                                    print("You are already borrowed a Book")
                                                    break
                                        break
                                    else:
                                        print(
                                            "============================\nPlease enter a valid entry!!\n============================")
                    else:
                        print("============================\nThe genre is not valid!!\n============================")
                elif start == '4':
                    which_g = input("\nWhich genre is the book(0 to exit):")
                    if which_g == '0':
                        continue
                    if is_genre_valid(which_g) ==  False:
                        print("============================\nThe genre is not valid!!\n============================")
                    else:
                        search_book_title = input("\nWhat is the  title:")
                        searched_book_reult = search_book(which_g,search_book_title)
                        if searched_book_reult == 'notfound':
                            print("============================\nBook not found!!\n============================")
                        elif searched_book_reult[1]['status'] == 'available':
                                 print("The book is available")
                        else:

                            for i in range(len(members_info)):
                                if members_info[i]['username'] == username:
                                    if members_info[i]['borrowed'] != search_book_title:
                                        print("You did not borrow this book")
                                        break
                                    else:
                                        for i in range(len(members_info)):
                                            if members_info[i]['username'] == username:
                                                members_info[i]['borrowed'] = 'none'
                                        books[which_g][searched_book_reult[0]]['status'] = 'available'
                                        print(f"\n{searched_book_reult[0]} successfully returned to the library")

                elif start == '5':
                    break
                else:
                    print("============================\nPlease enter a valid entry!!\n============================")
        else:
            print("Wrong username or password!!")
    elif before_start == '2':
        is_member_valid = True
        username = input("\nEnter your username(0 to exit):")
        if username == '0':
            continue
        password = input("\nEnter your password:")
        for member in members_info:
            if member['username'] == username:
                is_member_valid = False
                break
        if is_member_valid:
            members_info.append({
                'username' : username,
                'password':password,
                'borrowed': 'none'

            })
            print("Congratulations, you are in!!")
        else:
            print("============================\nEnter another username!!\n============================")

    else:
        print("============================\nPlease enter a valid entry!!\n============================")
