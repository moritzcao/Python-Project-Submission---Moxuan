from tkinter import *
from tkinter import ttk
from data_processing import *


# Initiate our data processing function
DP = data_processing()
unique_genre_list = DP.unique_genre_list

# Initiate a Tkinter app
root = Tk()
root.title('Movie Picker - Designed by moxuan@')
root.geometry(f'750x400')
root.config(background="#F8981D")


def tk_row(row, key, value):
    # Define a function to display the movie info on the app
    Label(text=key, height='2', width="20", font=("Arial", 14, 'bold'), bg='#F8981D', anchor="w").grid(row=row, column=0)
    Label(text=value, height='2', width="40", font=("Arial", 12), bg='#F8981D', anchor="w").grid(row=row, column=1)


def recommend():
    # Get the selected genre
    global selected_genre
    selected_genre = var.get()
    if selected_genre == '':
        return None

    # Invoke our data processing function to recommend a movie and display it on the app
    movie_info = DP.recommend_a_movie(selected_genre)
    tk_row(30, '', '')
    tk_row(31, 'Movie name', movie_info['title'])
    tk_row(32, 'Year', movie_info['year'])
    tk_row(33, 'Genre', movie_info['genre'])


# Construct the banner and user selection area
banner = Label(text=f'Select a genre you are interest in.\nI will recommend a movie for you!', font=("Arial", 18, 'bold'), width=50, height=2, bg='#283442', fg='white',)
banner.grid(row=0, column=0, columnspan=2)
var = StringVar()
Label(text="Select a genre:", height="2", width="20", font=("Arial", 14, 'bold'), bg='#F8981D', anchor="w").grid(row=5, column=0)
ttk.Combobox(textvariable=var, values=unique_genre_list, height=10, width=40, state='readonly').grid(row=5, column=1)
button = Button(text="OK", bg="#D3D3D3", font="Arial", width="6", height="1", command=recommend)
button.grid(row=7, column=1)

# Start the movie picker app
root.mainloop()