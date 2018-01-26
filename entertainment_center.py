import media
import fresh_tomatoes

# Create the Movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/zTYxDx",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://goo.gl/XRGxGu",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")
school_of_rock = media.Movie("School of Rock",
                             "Struggling rock singer disguises as a teacher",
                             "https://goo.gl/N6Vroj",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
gladiator = media.Movie("Gladiator",
                        "A man robbed of his name and his dignity strives" +
                        " to win them back",
                        "https://goo.gl/JbM2jf",
                        "https://www.youtube.com/watch?v=owK1qxDselE")
the_big_sick = media.Movie("The Big Sick",
                           "Pakistan-born comedian meets an American" +
                           " graduate student",
                           "https://goo.gl/y2bMK8",
                           "https://www.youtube.com/watch?v=PJmpSMRQhhs")
baby_driver = media.Movie("Baby Driver",
                          "Talented getaway driver wants to ditch his" +
                          " shady lifestyle for a girl",
                          "https://goo.gl/omd1h8",
                          "https://www.youtube.com/watch?v=z2z857RSfhk")

# Add the movies to a list
movies = [toy_story, avatar, school_of_rock, gladiator, the_big_sick,
          baby_driver]

# Call the the function to create the page and pass it the list
fresh_tomatoes.open_movies_page(movies)
