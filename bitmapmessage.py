import sys

bitmap = """
....................................................................

   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
                    
...................................................................."""


# There are 68 periods along the top and bottom
# But let's be honest, who asked?

print('Enter the message to display with the bitmap.')
message = input('> ')

if message == '':
    sys.exit()

    # If nothing is entered by the user,
    # we boot him off the program!

for line in bitmap.splitlines():
    # For each line in bitmap image,
    for i, bit in enumerate(line):
        # For each character in the line,

        if bit == ' ':

            print(' ', end='')

            # Print an empty space since there's space
            # In the bitmap image
            # Does not replace text in message
            # but rather hides it away instead

        else:
            print(message[i % len(message)], end='')

            # Prints a character from the message

            # When the message length is divided
            # by the index of the message's characters
            # to equal a net value of 1,
            # it then loops and resets the value
            # to 0

            # Or, in other terms:
            # - When i % len(message) = 1,
            # the message resets itself.
            # If the message was 'beans',
            # When the value of i % len(message) is 1,
            # the program loops backwards and rewrites the word beans
            # like so:

            # beansbeansbeansbeans
            # The word is repeated when the value
            # changes from 0 to 1

    print()
