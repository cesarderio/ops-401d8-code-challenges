#!/usr/bin/env python3

# Script Name:                  Cookie Capture Capades
# Author:                       Raphael Chookagian
# Date of latest revision:      08/28/2023
# Purpose:                      Create a python script:

# Import libraries
# import requests
import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
       `.    .              . ' .'       .    `.
        `.  '              .'  .'          `.   `
          /              `    `               \   \
        '                \   ,            .-''     |
       ;                 :   '          .'         |
      /                  |    \       .-'          ;
    ;       /                /         |          |
     '._      `-.__  |            '             .'
        ``"---...._ `-.___       .            ,'
               ....``"----'    .-;-._      _.-'
                           _.-'     ````-'
        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive a HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
with open("response.html", "w") as file:
    file.write(response_with_cookie.text)

# Open it with Firefox
webbrowser.get('firefox').open('response.html')
