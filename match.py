
def middle_evaluate(alias_mid, giv_mid):
    """evaluate middle name with or without initials"""

    if len(alias_mid)>1 and len(giv_mid)>1:
        return giv_mid == alias_mid

    elif len(alias_mid)==1 and len(giv_mid)>1:
        return alias_mid == giv_mid[0]

    elif len(alias_mid)>1 and len(giv_mid)==1:
        return alias_mid[0] == giv_mid

def split_name(name):

    name = name.split(" ")

    # assign first and last from name list
    first = name[0]
    last = name[-1]

    # if given name has over 2 names assign mid 
    if len(name) > 2:
        mid = name[1:-1][0]
    else:
        mid = None
    return (first,mid,last)


def name_match(aliases,given):
    """return True if name matches alias.


        >>> known_aliases = ['Alphonse Gabriel Capone']
        >>> name_match(known_aliases, 'Gabriel Alphonse Capone')
        True
        >>> name_match(known_aliases, 'Gabriel A Capone')
        True
        >>> name_match(known_aliases, 'Gabriel Capone')
        True
        >>> name_match(known_aliases, 'Gabriel Francis Capone')
        False
        >>>

    """

    # if given name matches exactly with alias return True
    if given in aliases:
        return True

    else:
        # split given name into a list
        giv_first, giv_mid, giv_last = split_name(given)
  
        # split each name in aliases.
        for alias in aliases:
            alias_first, alias_mid, alias_last = split_name(alias)

            # if middle name exists evaluate name with middle name
            if giv_mid:
                # if alias name matches given name, confirm middle name
                if alias_first == giv_first and alias_last == giv_last:
                    return middle_evaluate(alias_mid, giv_mid)
             
                # if name is transposed 
                elif alias_first == giv_mid and alias_mid == giv_first:
                    # switch first and middle name of given
                    temp = giv_first
                    giv_first = giv_mid
                    giv_mid = temp

                    return middle_evaluate(alias_mid, giv_mid)
                
                # if name is transposed with initial
                elif alias_first[0] == giv_mid and alias_mid == giv_first:
                    return True   

            # if given name only includes middle and last name
            elif alias_mid == giv_first and alias_last == giv_last:
                return True

        return False




if __name__=="__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print(" **** Correct **** ")

