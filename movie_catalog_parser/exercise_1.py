from collections import defaultdict

class InvalidMovieError(Exception): pass

class Movie:

    def __init__(self,title, genre, rating, votes):
        self.title =title
        self.genre=genre
        self.rating=rating
        self.votes=votes

    def __repr__(self):
        return f"{self.title} ({self.rating})"


    @classmethod
    def from_line(cls, line):
        try:
            title, genre, rating, votes=line.split(",")
            rating = float(rating)
            votes=int(votes)
        except ValueError:
            raise InvalidMovieError("Invalid movie")

        if not 0<=rating<=10:
            raise InvalidMovieError("Invalid rating")

        return cls(title.strip(), genre.strip(), rating, votes)



class Catalog:
    def __init__(self):
        self.movies=[]

    def add_movie(self, movie):
        self.movies.append(movie)

    def average_rating_by_genre(self):
        genre_ratings=defaultdict(list)
        for movie in self.movies:
            genre_ratings[movie.genre].append(movie.rating)
        result = {}
        for genre, rating in genre_ratings.items():
            result[genre] = round(sum(rating)/len(rating), 2)
        return result

    def top_rated(self, n):
        return sorted(
            self.movies,
            key=lambda movie: (-movie.rating, movie.title)
        )[:n]

    def most_voted(self):
        return max(self.movies, key=lambda m:m.votes)

    def genres(self):
        genres=[]
        added=[]
        for m in self.movies:
            if m.genre not in added:
                added.append(m.genre)
                genres.append(m.genre)
        return sorted(genres)
        #return sorted(set(m.genre for m in self.movies))

def read_from_file(file_name):
    lines=[]
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return []
    else:
        return lines

def main():
    catalog = Catalog()
    lines = read_from_file("sample.txt")
    skipped=0

    for line in lines:
        if not line.strip():
            continue
        try:
            catalog.add_movie(Movie.from_line(line.strip()))
        except InvalidMovieError:
            skipped+=1
    print(f"Skipped {skipped} malformed lines")
    print(f"Average rating by genre: {catalog.average_rating_by_genre()}")
    print(f"Top rated: {catalog.top_rated(3)}")
    print(f"Most voted: {catalog.most_voted()}")
    print(f"Genres: {catalog.genres()}")

if __name__ == "__main__":
    main()
