"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Billy Davignon.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    # Test 1: 4, 2
    expected = (1 ** 2) + (2 ** 2) + (3 ** 2) + (4 ** 2)
    answer = sum_powers(4, 2)
    print('Test 1 expected:', expected)
    print('        actual', answer)

    # Test 2: 4, 4
    expected = (1 ** 4) + (2 ** 4) + (3 ** 4) + (4 ** 4)
    answer = sum_powers(4, 4)
    print('Test 2 expected:', expected)
    print('        actual', answer)

    # Test 2: 2, 5
    expected = (1 ** 5) + (2 ** 5)
    answer = sum_powers(2, 5)
    print('Test 3 expected:', expected)
    print('        actual', answer)



def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    total = 0
    for k in range(n):
        total = total + ((k + 1) ** p)
    return total
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # -------------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')
    # Test 1: 4, 2, 3
    expected = ((4 + 0) ** 3) + ((4 + 1) ** 3)
    answer = sum_powers_in_range(4, 2, 3)
    print('Test 1 expected:', expected)
    print('        actual', answer)

    # Test 2: 5, 3, 1
    expected = ((5 + 0) ** 1) + ((5 + 1) ** 1) + ((5 + 2) ** 1)
    answer = sum_powers_in_range(5, 3, 1)
    print('Test 1 expected:', expected)
    print('        actual', answer)

    # Test 3: 2, 4, 3
    expected = ((2 + 0) ** 3) + ((2 + 1) ** 3) + ((2 + 2) ** 3) + ((2 + 3) ** 3)
    answer = sum_powers_in_range(2, 4, 3)
    print('Test 1 expected:', expected)
    print('        actual', answer)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    total = 0
    for k in range(n):
        total = total + ((m + k) ** p)
    return total

    # -------------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
