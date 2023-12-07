# main.py
# Name: James Speed and John Cannon
# email: speedjp@mail.uc.edu and cannonjp@mail.uc.edu
# Assignment Title: Fulcher Final
# Due Date: 12/7/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project loads 2 json files, decrypts them in two different methods, and displays an image based on the fruits of our labor
# Citations: CHATGPT and Stack Overflow
# Anything else that's relevant: We really do not like SAND!

from decryptPackage import movie, location, load_json
from photoPackage.photo import load_and_display_image

if __name__ == '__main__':
    movie_name = movie.find_movie_name()
    location = location.find_location()
    print(location)
    load_and_display_image("NO_SAND.jpeg")
