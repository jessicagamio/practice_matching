

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
    
    # assign giv_first to first name and giv_last to last name
    giv_first = giv_name[0]
    giv_last = giv_name[-1]

    # if given name has a middle name assign giv_mid to middle name 
    if len(giv_name) > 2:
        giv_mid = giv_name[1:-1]

    else:
        if len(aliases) > 1:

            for name in aliases:
                name=name.split(" ")
                first_name=name[0]
                last_name=name[-1]

                if len(name)>2:
                    mid_name=name[1:-1]

                if first_name == giv_first and last_name == giv_last:
                    if len(giv_name) > 2:
                        if giv_mid == mid_name:
                            return True
                        else:
                            return False
                    else:
                        return True
        return False



if __name__=="__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print(" **** Correct **** ")

