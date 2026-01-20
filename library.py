""" University Library management system using lists.
Add.
Insert.
Remove.
Update or replace.
Search.
Display.
Sort.
Reverse.
Count how many times book is borrowed.
Exit. """

# taking input
book_list = [b.strip() for b in input("Enter books (comma separated): ").split(",")]

# Add
book_list.append("Suspense")
print("After adding:", book_list)

# Insert
book_list.insert(2, "Biography")
print("After inserting:", book_list)

# Remove
if "Suspense" in book_list:
    book_list.remove("Suspense")
print("After removing:", book_list)

# Update
book_list[1] = "Awareness"
print("After updating:", book_list)

# Search
print("Is 'Awareness' present?", "Awareness" in book_list)

# Display
print("Last book:", book_list[-1])

# Sort
book_list.sort()
print("Sorted:", book_list)

# Reverse
book_list.reverse()
print("Reversed:", book_list)

# Count
print("BhagwadGeeta borrowed:", book_list.count("BhagwadGeeta"))

# Exit
print("Thank you for using our services")
