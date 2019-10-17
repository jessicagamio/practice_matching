

def name_match(aliases,given):
    """return True if name matches alias.


        >>> known_aliases = ['Alphonse Capone']
        >>> name_match(known_aliases, 'Alphonse Gabriel Capone')
        True
        >>> name_match(known_aliases, 'Alexander Capone')
        False
        >>> name_match(known_aliases, 'Alphonse Francis Capone')
        True 

    """

    
    # if given name matches exactly with alias return True
    if given in aliases:
        return True

    # split given int a list by spaces in given string
    giv_name = given.split(" ")
    print(giv_name)

    # assign giv_first to first name and giv_last to last name
    giv_first = giv_name[0]
    giv_last = giv_name[-1]

    # if given name has a middle name assign giv_mid to middle name 
    if len(giv_name) > 2:
        giv_mid = giv_name[1:-1][0]
    
    print("given_name====>", giv_first, giv_last)

    if aliases:
        # split each name in aliases. Assign first_name and last_name
        for name in aliases:
            name=name.split(" ")
            first_name=name[0]
            # print('first name---->', first_name)
            last_name=name[-1]
            # print('last name----->', last_name)

            # if middle name exissts assign mid_name
            if len(name)>2:
                mid_name=name[1:-1][0]
                # print('middle name----->', mid_name)
            else:
                mid_name=None

            # if alias name matches given name
            if first_name == giv_first and last_name == giv_last:
                if len(giv_name)>2:
                    # print("you should be here!!!!")
                    if mid_name:
                        return giv_mid == mid_name
                    return True

        return False

known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']
answer=name_match(known_aliases, 'Alphonse Gabriel Capone')
print(answer)

# if __name__=="__main__":
#     from doctest import testmod
#     if testmod().failed == 0:
#         print(" **** Correct **** ")

