import sqlite3


stephen_king_adaptations_list = []
with open('stephen_king_adaptations.txt', 'r') as file:
    for line in file:
        movie_id, movie_name, movie_year, imdb_rating = line.strip().split(',')
        stephen_king_adaptations_list.append((movie_id, movie_name, int(movie_year), float(imdb_rating)))


conn = sqlite3.connect('stephen_king_adaptations.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
                  (movieID TEXT, movieName TEXT, movieYear INTEGER, imdbRating REAL)''')


cursor.executemany('INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)', stephen_king_adaptations_list)

while True:
    print("\nOptions:")
    print("1. Search by Movie Name")
    print("2. Search by Movie Year")
    print("3. Search by Movie Rating")
    print("4. STOP")

    choice = input("Enter your choice: ")

    if choice == '1':
        movie_name = input("Enter the name of the movie: ")
        cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?', (movie_name,))
        result = cursor.fetchone()
        if result:
            print("Movie Found:")
            print(f"Movie Name: {result[1]}")
            print(f"Movie Year: {result[2]}")
            print(f"IMDB Rating: {result[3]}")
        else:
            print("No such movie exists in our database")

    elif choice == '2':
        movie_year = int(input("Enter the year: "))
        cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?', (movie_year,))
        results = cursor.fetchall()
        if results:
            print("Movies Found:")
            for result in results:
                print(f"Movie Name: {result[1]}")
                print(f"Movie Year: {result[2]}")
                print(f"IMDB Rating: {result[3]}")
        else:
            print("No movies were found for that year in our database.")

    elif choice == '3':
        rating_limit = float(input("Enter the minimum rating: "))
        cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?', (rating_limit,))
        results = cursor.fetchall()
        if results:
            print("Movies Found:")
            for result in results:
                print(f"Movie Name: {result[1]}")
                print(f"Movie Year: {result[2]}")
                print(f"IMDB Rating: {result[3]}")
        else:
            print("No movies at or above that rating were found in the database.")

    elif choice == '4':
        break

conn.close()
