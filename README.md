# Python-Project-Submission---Moxuan
Capstone project for adv Python training

IMDB is the world's most authoritative source for movie. To get movie information, I used advanced search in IMDB and got a list of top 1000 popular movies.
https://github.com/moritzcao/Python-Project-Submission---Moxuan/blob/main/snapshot/imdb.PNG

I used Selenium to scrape movies’ ranking, title, year, genre and description from IMDB. 
![aaa](https://github.com/moritzcao/Python-Project-Submission---Moxuan/blob/b1c75b8acf7a147a97e78bde060d4082f8dad7d0/snapshot/scrape.PNG)

The results were stored in a txt file. Columns were separated by \t to make Pandas easier to read as CSV.


I created a function to use Pandas to read result file as DataFrame. The function is also able to output a movie info dictionary based on a user-input genre. 


I also created an app using Tkinter package. User could select a genre he interested in and click OK button.


Then, the app displays a random movie that matches the desired input genre. 


