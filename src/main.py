# import modules
import sys
from timeit import default_timer as timer
import numpy as np


'''technique does not work well with larger numbers, at least not on a Ryzen 1700x'''
'''it bogs down the larger the number gets, dropping to a prime roughly every 3 seconds around 50 million mark'''


# Initialize a list
class OptimusPrime:
    def __init__(self):
        # declare a separator bar
        self.sep_bar = """
------------------------------------------------------------------------------------------------------------------------
        """

        # declare range defaults
        self.default_start = 2
        self.default_finish = 29

        # declare empty self.primes list for use by class
        self.primes = []

    @staticmethod
    def print_progress(p, s=None, f=None, done=False):
        if done is False:
            # equation for a rough percentage
            percent = (p - s) / (f + 1 - s) * 100

            # stdout.write to write information on same line repeatedly
            sys.stdout.write("\r" + "Processing Primes: " + f"{str(p)} ({str(round(percent, 2))}%)")
            sys.stdout.flush()

        elif done is True:
            # insure that when the loop finishes, it says 100% since the above equation will never reach 100%
            sys.stdout.write("\r" + "Processing Complete: " + f"{str(p)} (100%)")
            sys.stdout.flush()

    def get_primes(self, start=None, finish=None, store=False, filename=None):
        # catch empty arguments and insert defaults
        if start is None or finish is None:
            start = self.default_start
            finish = self.default_finish
            print(f"unconfigured arguments, defaulting to ({start}, {finish})")

        print("\n")
        print(self.sep_bar)
        print(f"Beginning search for prime numbers within range ({start}, {finish})")
        print(self.sep_bar)

        # start timeit timer to determine performance of
        timer_start = timer()

        # start for loop to find primes
        for possible_prime in range(start, finish + 1):

            # Assume number is prime until shown it is not.
            is_prime = True
            for num in range(2, possible_prime):
                if possible_prime % num == 0:
                    is_prime = False
                    break

            # add prime numbers to list and print current value in place with completion percentage
            if is_prime:
                self.primes.append(possible_prime)
                self.print_progress(p=self.primes[-1], s=start, f=finish)

        # need to force stdout output change to "100%" upon loop completion due to dirty code.
        self.print_progress(p=self.primes[-1], done=True)

        # force next line after for loop to line down from stdout output
        print("\n")

        # assemble primes list into an np array and print output for wrap effect
        df = np.array(self.primes)
        print(df)

        # end timer and print statistics
        timer_end = timer()
        print(f"\nFound {len(self.primes)} prime numbers within range ({start} and {finish}) "
              f"and dumped values into an np.array in ({round(timer_end - timer_start, 6)} seconds)")
        print(self.sep_bar)

        # save array to file, (dirty (it wants an int instead of an array) but it works, regardless)
        if store is True:
            file_format = ".txt"

            np.savetxt(f'{filename}({start}_{finish}){file_format}',
                       df,  # dirty
                       fmt="%d")
#


#
if __name__ == "__main__":
    # call and store class
    op = OptimusPrime()

    # say hello
    print(op.sep_bar)
    print("Welcome to PrimeFinder!")
    print(op.sep_bar)
    print("Find prime numbers within a range!\n")

    # example of OptimusPrime.get_primes() functionality
    def test_file():
        # set file name (excluding extension)
        testfile = "test_prime_file"

        # y/n prompt for manually selecting range

        config_choice = input("Would you like to configure the search range? (y/n): ")

        # call manual input instead of defaults
        if config_choice == "Y" or config_choice == "y":
            c_start = int(input("start: "))
            c_finish = int(input("finish: "))

            if c_start > c_finish:
                print("lower range cannot be larger than upper range!")
                test_file()

            if c_start <= 1:
                print("lower range cannot be less than 2!")
                test_file()

        # call defaults instead of manual input
        elif config_choice == "N" or config_choice == "n":
            c_start = op.default_start
            c_finish = op.default_finish

        else:
            c_start = op.default_start
            c_finish = op.default_finish
            print(f" - Invalid input, reverting to default ({c_start}, {c_finish})\n")

        # y/n prompt for storing output to a .txt file in same directory
        store_choice = input("Would you like to store output to a txt file? (y/n): ")

        if store_choice == "Y" or store_choice == "y":
            op.get_primes(start=c_start, finish=c_finish, store=True, filename=testfile)

        elif store_choice == "N" or store_choice == "n":
            op.get_primes(start=c_start, finish=c_finish)
        else:
            print(" - Invalid input, defaulting to no \n")
            op.get_primes(start=c_start, finish=c_finish)

        # attempt to request another go
        again = input("\nWould you like to search another range for prime numbers? (y/n): ")

        if again == "Y" or again == "y":
            test_file()

        elif again == "N" or again == "n":
            print("Exiting...")
            exit()

        else:
            print(" - Invalid input, exiting...")
            exit()


    test_file()
