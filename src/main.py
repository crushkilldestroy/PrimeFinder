# import modules
import sys
import numpy as np


'''technique does not work well with larger numbers, at least not on a Ryzen 1700x'''
'''it bogs down the larger the number gets, dropping to a prime roughly every 3 seconds around 50 million mark'''


# Initialize a list
class OptimusPrime:
    def __init__(self):
        # declare range defaults
        self.default_start = 2
        self.default_finish = 29

        # declare empty self.primes list for use by class
        self.primes = []

    def get_primes(self, start=None, finish=None, store=False, filename=None):
        # catch empty arguments and insert defaults
        if start is None or finish is None:
            start = self.default_start
            finish = self.default_finish
            print(f"unconfigured arguments, defaulting to ({start}, {finish})")

        print(f"Beginning search for prime numbers within range ({start}, {finish})")
        for possiblePrime in range(start, finish+1):

            # Assume number is prime until shown it is not.
            is_prime = True
            for num in range(2, possiblePrime):
                if possiblePrime % num == 0:
                    is_prime = False
                    break

            # add prime numbers to list and print in place
            if is_prime:
                self.primes.append(possiblePrime)
                sys.stdout.write("\r" + "Processing Primes: " + str(self.primes[-1]))

        # force next line after for loop to line down from stdout output
        print("\n")

        # assemble primes list into an np array and print output for wrap effect
        df = np.array(self.primes)
        print(df)

        # save array to file, (dirty)
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
    print("------------------------")
    print("Welcome to PrimeFinder!")
    print("------------------------\n")
    print("Find prime numbers within a range!\n")

    # example of OptimusPrime.get_primes() functionality
    def test_file():
        # set file name (excluding extension)
        testfile = "test_prime_file"

        # y/n prompt for manually selecting range
        print("Would you like to configure the search range? (y/n)")
        config_choice = input(" > ")

        # call manual input instead of defaults
        if config_choice == "Y" or config_choice == "y":
            c_start = int(input("start > "))
            c_finish = int(input("finish > "))

            if c_start > c_finish:
                print("lower range cannot be larger than upper range!")
                print("restarting test function")
                test_file()

        # call defaults instead of manual input
        else:
            c_start = op.default_start
            c_finish = op.default_finish

        # y/n prompt for storing output to a .txt file in same directory
        print("Would you like to store output to a txt file? (y/n)")
        store_choice = input(" > ")

        if store_choice == "Y" or store_choice == "y":
            op.get_primes(start=c_start, finish=c_finish, store=True, filename=testfile)

        elif store_choice == "N" or store_choice == "n":
            op.get_primes(start=c_start, finish=c_finish)

        # attempt to request another go
        print("\nwould you like to search another range for prime numbers? (y/n)")
        again = input(" > ")

        if again == "Y" or again == "y":
            test_file()
        else:
            exit()


    test_file()
