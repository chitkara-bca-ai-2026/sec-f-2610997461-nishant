
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {book[3] for book in books}

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("==================================================")
print("       LIBRARY BOOK & CATEGORY MANAGER            ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == '1':
        print("\n--- Current Library Catalog (Fixed Records) ---")
        for i, book in enumerate(books, 1):
            title, author, year, category = book 
            print(f'{i}. "{title}" by {author} ({year}) \n| Genre: {category}')
        print(f"Total Books: {len(books)}")

    elif choice == '2':
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()

        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            
            library_categories.add(category)
            
            print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("\n[ERROR] All fields are required. Record not added.")

    elif choice == '3':
        print("\n--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == '4':
        print("\n--- Add to Student Wishlist ---")
        genre = input("Enter requested category: ").strip()
        if genre:
            student_wishlist.add(genre)
            print(f'[SUCCESS] "{genre}" added to student wishlist.')

    elif choice == '5':
        print("\n==================== CATEGORY GAP ANALYSIS ====================")
        print(f"Library Holdings (Set): \n {sorted(list(library_categories))}")
        print(f"Student Wishlist (Set): \n {sorted(list(student_wishlist))}")
        print("----------------------------------------------------------------------")

        in_stock = sorted(list(library_categories & student_wishlist))
        print("1. Already in Stock (Intersection &):")
        print(f"   {in_stock}\n")

        purchase_needed = sorted(list(student_wishlist - library_categories))
        print("2. Purchase Order Needed (Difference -):")
        print(f"   {purchase_needed}\n")

        combined_coverage = sorted(list(library_categories | student_wishlist))
        print("3. Full Combined Genre Coverage (Union |):")
        print(f"   {combined_coverage}")
        print("======================================================================")

    elif choice == '6':
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice. Please enter a valid number between 1 and 6.")

