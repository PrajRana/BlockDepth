def readfile():
    # counter stores the block value to be printed
    counter = 0
    with open("input.txt", "r") as info:
        for words in info:
            # get rid of space before words and new line
            hold = (words.strip(" ")).strip("/n")
            # if hold has { or } in it
            if '}' in hold or '{' in hold:
                # if hold starts with {
                if hold.startswith('{'):
                    # block started so increase counter
                    counter = counter + 1
                    print(counter, words, end='')

                # if hold starts with }
                elif hold.startswith('}'):
                    # leaving block so print block value and
                    # then decrement block value
                    print(counter, words, end='')
                    counter = counter - 1

                # hold has { or } but its not starting with { or }
                # so just ignore it
                else:
                    print(counter, words, end='')

                # if hold does not have { or } just print it
            else:
                print(counter, words, end='')

        # counter should be zero when we leave the blocks
        if counter != 0:
            print("Mismatching parenthesis. Counter should be 0 in the end but counter is ", counter)


# call the function
readfile()
