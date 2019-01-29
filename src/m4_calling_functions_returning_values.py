"""
This module demonstrates and practices:
  -- using ARGUMENTs in function CALLs,
  -- having PARAMETERs in function DEFINITIONs, and
  -- RETURNING a value from a function,
        possibly CAPTURING the RETURNED VALUE in a VARIABLE.
  -- UNIT TESTING.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Billy Davignon.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m4t_tester


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_of_digits()
    run_test_digits_in_cube()
    run_test_digits_in_power()
    run_test_fancy_sums_of_digits()

    # -------------------------------------------------------------------------
    # Done: 9. DO THIS LAST!
    #    -- Uncomment the line of code below to run the main function
    #         in m4t_tester.py (do not make changes to it).
    #         It runs OUR tests on your code.
    #    -- Check to see whether all test cases indicate they
    #          "COMPLETED SUCCESSFULLY!"
    #    -- If your code fails any of OUR tests but passes YOUR tests,
    #         then you are likely not TESTING the methods correctly.
    #       ** Ask a TA or your professor for help in that case. **
    # -------------------------------------------------------------------------

    m4t_tester.main()


def run_test_sum_of_digits():
    """ Tests the  sum_of_digits   function. """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this TEST function, as follows:
    #
    #  Step 1:  This TEST function tests the  sum_of_digits  function.
    #    So read the doc-string of the  sum_of_digits  function
    #    defined below.  Be sure that you understand from the
    #    doc-string what the  sum_of_digits  function SHOULD return.
    #
    #  Step 2:  Pick a test case:  a number that you could send as
    #    an actual argument to the  sum_of_digits  function.
    #      - For example, you could pick the test case  826.
    #
    #  Step 3: Figure out the CORRECT (EXPECTED) answer for your
    #    test case.  In the example of  826  the correct answer
    #    for the sum of its digits is  8 + 2 + 6, which is 16.
    #
    #  Step 4: Write code that prints both the EXPECTED answer
    #    and the ACTUAL answer returned when you call the function.
    #    See the example below.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_of_digits   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 8 + 2 + 6
    answer = sum_of_digits(826)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # -------------------------------------------------------------------------
    # TO DO: 2 (continued).
    # Below this comment, add 3 more test cases of your own choosing.
    # -------------------------------------------------------------------------

    # Test 2: 12345
    expected2 = 1 + 2 + 3 + 4 + 5
    answer2 = sum_of_digits(12345)
    print('Test 2 expected:', expected2)
    print('        actual', answer2)

    # Test 3: 678
    expected3 = 6 + 7 + 8
    answer3 = sum_of_digits(678)
    print('Test 3 expected:', expected3)
    print('        actual:', answer3)

    # Test 4: 1000000
    expected4 = 1 + 0 + 0 + 0 + 0 + 0 + 0
    answer4 = sum_of_digits(1000000)
    print('Test 4 expected', expected4)
    print('        actual', answer4)


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  The sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    #
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the doc-string above.  Treat this function as a black box.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_digits_in_cube():
    """ Tests the   digits_in_cube   function. """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function.
    #   It TESTS the  digits_in_cube  function defined below.
    #   Include at least **   3   ** tests.
    #
    # To implement this TEST function, use the same 4 steps as above:
    #
    #   Step 1: Read the doc-string of  digits_in_cube  below.
    #     Understand what that function SHOULD return.
    #
    #   Step 2:  Pick a test case:  a number(s) that you could send as
    #     actual argument(s) to the  digits_in_cube  function.
    #
    #  Step 3: Figure out the CORRECT (EXPECTED) answer for your test case.
    #
    #  Step 4: Write code that prints both the EXPECTED answer
    #    and the ACTUAL answer returned when you call the function.
    #    Follow the same form as in previous examples.
    #
    #   Include at least **   3   ** tests.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------')
    print('Testing the   digits_in_cube   function:')
    print('-----------------------------------------------------')

    # Test 1: 9
    expectedcube1 = 7 + 2 + 9
    answercube1 = digits_in_cube(9)
    print('Test 1 expected:', expectedcube1)
    print('        actual', answercube1)

    # Test 2: 5
    expectedcube2 = 1 + 2 + 5
    answercube2 = digits_in_cube(5)
    print('Test 2 expected:', expectedcube2)
    print('        actual', answercube2)

    # Test 3: 3
    expectedcube3 = 2 + 7
    answercube3 = digits_in_cube(3)
    print('Test 3 expected:', expectedcube3)
    print('        actual:', answercube3)




def digits_in_cube(n):
    """
    What comes in:  A positive integer.
    What goes out:  The sum of the digits in the CUBE of the integer.
    Side effects:   None.
    Example:
      If the integer (n) is 5    (so n cubed is 125),
      this function returns (1 + 2 + 5), which is 8.
    """
    k = n ** 3
    return sum_of_digits(k)

    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    ###########################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------


def run_test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    # -------------------------------------------------------------------------
    # Done: 5. Implement this function.
    #   It TESTS the  digits_in_power  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   digits_in_power   function:')
    print('--------------------------------------------------')

    # Test 1: 3, 4
    expectedpower1 = 8 + 1
    answerpower1 = digits_in_power(3, 4)
    print('Test 1 expected:', expectedpower1)
    print('        actual', answerpower1)

    # Test 2: 4, 4
    expectedpower2 = 2 + 5 + 6
    answerpower2 = digits_in_power(4, 4)
    print('Test 2 expected:', expectedpower2)
    print('        actual', answerpower2)

    # Test 3: 2, 5
    expectedpower3 = 3 + 2
    answerpower3 = digits_in_power(2, 5)
    print('Test 3 expected:', expectedpower3)
    print('        actual', answerpower3)



def digits_in_power(n, k):
    """
    What comes in:  Two positive integers, n and k.
    What goes out:
      The sum of the digits in x, where x is n raised to the kth power.
    Side effects:   None.
    Example:
      If the arguments are 12 and 3, respectively,
      this function returns 18
      since 12 to the 3rd power is 1728 (whose digits sum to 18).
    """
    p = n ** k
    return sum_of_digits(p)
    # -------------------------------------------------------------------------
    # Done: 6. Implement and test this function.
    #
    ###########################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------


def run_test_fancy_sums_of_digits():
    """ Tests the   fancy_sums_of_digits   function. """
    # -------------------------------------------------------------------------
    # Done: 7. Implement this function.
    #   It TESTS the  fancy_sums_of_digits  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing the previous
    # TEST functions.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   fancy_sums_of_digits   function:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # HINT:  For your 1st test, consider  n=10.  Figure out BY HAND
    # the correct (expected) answer for that test case.  (It's easy.)
    # The doc-string below gives test cases you can use for
    # your 2nd and 3rd tests but READ THOSE TEST CASES CAREFULLY
    # in the doc-string to be sure that you understand the specification.
    # -------------------------------------------------------------------------

    # Test 1: 10
    expectedfancy1 = 1
    answerfancy1 = fancy_sums_of_digits(10)
    print('Test 1 expected:', expectedfancy1)
    print('        actual', answerfancy1)

    # Test 2: 2
    expectedfancy2 = 19084
    answerfancy2 = fancy_sums_of_digits(2)
    print('Test 2 expected:', expectedfancy2)
    print('        actual', answerfancy2)

    # Test 3: 35
    expectedfancy3 = 124309
    answerfancy3 = fancy_sums_of_digits(35)
    print('Test 3 expected:', expectedfancy3)
    print('        actual', answerfancy3)



def fancy_sums_of_digits(n):
    """
    What comes in:  A positive integer n.
    What goes out:
      -- Let X denote the   sum   of the digits in (n ** 1000).
      -- Let Y denote the   sum   of the digits in (n ** 999).
      This function RETURNs the sum of the digits in (X ** Y).
    Side effects:   None.
    Examples:
      -- If n is 2, then:
            -- the   sum   of the digits in n ** 1000 is 1366 (trust me!).
            -- the   sum   of the digits in n ** 999 is 1367 (trust me!).
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- the   sum   of the digits in (X ** Y) is 19084 (trust me!)
            -- so this function returns 19084.
      -- If n is 35, then:
            -- the sum of the digits in n ** 1000 is 7021 (trust me!).
            -- the sum of the digits in n ** 999 is 7145 (trust me!).
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- the sum of the digits in (X ** Y) is 124309 (trust me!)
            -- so this function returns 124309.
    """
    #m = ((n ** 1000) ** (n ** 999))
    #return sum_of_digits(m)

    # -------------------------------------------------------------------------
    # Done: 8. Implement and test this function.
    #
    ###########################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
