import fresh_tomatoes
import media

gentle = media.Movie("Gentle",
                     "This is the first song I played and uploaded to YouTube.",
                     "https://i.loli.net/2017/07/25/59764863960f6.png",
                     "https://www.youtube.com/watch?v=lhEMwFGDpok")
the_heart_never_lies = media.Movie("The Heart Never Lies",
                                   "Singing on The brooklyn bridge!",
                                   "https://i.loli.net/2017/07/25/59764b255e0d7.png",
                                   "")
imagine = media.Movie("Imagine",
               "The world famous song: Imagine - John Lennon, covered by Haiquan.",
               "https://i.loli.net/2017/07/25/59764b2622d33.png",
               "https://www.youtube.com/watch?v=Kfl99Sfk-T8")
alive = media.Movie("Alive",
               "Run for your life :)",
               "https://i.loli.net/2017/07/25/59764b23e600b.png",
               "https://www.youtube.com/watch?v=O5aaYJtjABc")
young_for_you = media.Movie("Young For You",
               "There're always some reasons why and how you're young.",
               "https://i.loli.net/2017/07/25/59764b25cef02.png",
               "https://www.youtube.com/watch?v=Q7sPiSMhsiY")
cant_help = media.Movie("Can't Help",
               "This is a famous Chinese song telling the singer can't help loving a girl.",
               "https://i.loli.net/2017/07/25/59764b2552215.png",
               "https://www.youtube.com/watch?v=UWJXmFdRLtE")

movies = [gentle, the_heart_never_lies, imagine, alive, young_for_you, cant_help]
fresh_tomatoes.open_movies_page(movies)
