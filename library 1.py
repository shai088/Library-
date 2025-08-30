print('WELCOME TO YOUR LIBRARY\n')
books = [ ]
book = input('Enter the name of a book you own: ').lower()
books.append(book)
book = input("Enter another name of a book you own(or press 'Enter' to skip: ").lower()
if book :
	books.append(book)
	print(f'your library: {books}')
else :
	print(f'your library: {books}')

wishlist = [ ]
wish = input('\nEnter the name of a book you wish to have in future: ').lower()
wishlist.append(wish)
wish = input("Enter another name of book you wish to have (or press 'Enter' to skip): ").lower()
if wish:
	wishlist.append(wish)
	print(f'your wishlist: {wishlist}')
else:
	print(f'your wishlist: {wishlist}')
	
got = input("\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ").lower()
if got :
	
	books.append(got)
	wishlist.remove(got)
	print(f'Updated library : {books}')
	print(f'Updated wishlist : {wishlist}')
else:
	print(f'Updated library : {books}')
	print(f'Updated wishlist : {wishlist}')

don = input("\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip): ").lower()
if don:
	books.remove(don)
	print(f'final library after donation: {books}')
else :
	print(f'final library after donation: {books}')
