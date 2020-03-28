import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marline on a alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

monsters = media.Movie("Monsters Inc.",
                       "Monsters generate their city's power by scaring \
                        children, but they are terribly afraid themselves \
                        of being contaminated by children, so when one enters \
                        Monstropolis, top scarer Sulley finds his world \
                        disrupted.",
                       "http://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                       "https://www.youtube.com/watch?v=FLWO5uyFpNo")
                       

shrek = media.Movie("Shrek",
                    "After his swamp is filled with magical creatures, an \
                     ogre agrees to rescue a princess for a villainous lord \
                     in order to get his land back.",
                    "http://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                    "https://www.youtube.com/watch?v=jYejzdBwvY4")
                    

star_trek = media.Movie("Star Trek (2009)",
                        "The brash James T. Kirk tries to live up to his \
                         father's legacy with Mr. Spock keeping him in check \
                         as a vengeful, time-traveling Romulan creates black \
                         holes to destroy the Federation one planet at a \
                         time.",
                        "http://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                        "https://www.youtube.com/watch?v=SyJszxnJydA")
movies = [toy_story,avatar,monsters,shrek,star_trek]
fresh_tomatoes.open_movies_page(movies)
