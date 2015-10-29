#!/usr/bin/python3
import curses
#from pygithub3 import Github


def main(stdscr):
    stdscr.clear()
    login()
    pass

def initscr():
    pass

def login():
    #display login prompt
    beginx = 20
    beginy = 7
    height = 4
    width = 30
    form = curses.newwin(height, width, beginy, beginx)
    form.addstr(0,1,"press q to quit, i to login")
    form.addstr(1,1,"username")
    form.addstr(2,1,"password")
    c = form.getch()
    if c == ord('q'):
        curses.endwin()
    elif c == ord('i'):
        curses.echo()
        username =  form.getstr(1, 1+len('username'), 15)
        password =  form.getstr(2, 1+len('password'), 15)
        curses.noecho()
    pass

# takes in a query string, sends the query to github returns the query results
def search(query):
    pass

# returns the feed of the user
def feed():
    pass

# given a repo it will display the name, commits, and other stuff
def view_repo():
    pass

if __name__ == "__main__":
    curses.wrapper(main)
