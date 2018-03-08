from time import sleep
from os import system
import slice
time_between_steps = 5

def main():
    for timeslice in slice.csv_next_slice():
        system("clear")
        print(timeslice)
        sleep(time_between_steps)
        
main()
