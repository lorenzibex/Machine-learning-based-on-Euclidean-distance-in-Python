# Machine-learning-based-on-Euclidean-distance-in-Python
Ever wondered how Amazon or Youtube knows what books, movies or products you will probably like? In this short example you will see a simple way to measure the similarity of taste between two person. This can help to propose new movies, books or products, which one of the two, doesn’t know yet.


First we create a dictionary of different of ratings from different people for various movies.

In the end we print out all the ratings from Toby and next just his rating for the movie Terminator. This allows us to extract certain ratings and compare them with the ratings from other people. Now similar when calculating the distance between two points in space we can calculate the rating difference between two people. As an example we look at two points in a 2D space and calculate their difference.

This distance is also called the Euclidean distance. Next we translate the same thinking to a function calculating the distance between two persons within our created dictionary:

The function distance ask first for a dictionary, which is called ratings. Next, it asked for two names Toby and Julian, of whom the function will calculate the distance in a multidimensional space. First the function creates a dictionary of common movies of Julian and Toby. Then gives this smaller dictionary to calculate the difference between the tastes of Toby and Julian. The result is 1.67 which is smaller than for exmaple the difference in tastes between Toby and Alex, which is 0.25.
