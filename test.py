import curses
import csv



"""print variables in desired display"""

# Start Curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


# End Curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()


""" Load variable's from csv """

