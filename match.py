

def name_match(aliases,given):
    """return True if name matches alias.


        >>> known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
        >>> name_match(known_aliases, 'Alphonse G Capone')
        True
        >>> name_match(known_aliases, 'Alphonse E Capone')
        False
        >>> name_match(known_aliases, 'Alphonse Gregory Capone')
        False 

    """

    
    # if given name matches exactly with alias return True
    if given in aliases:
        return True

    else:

        # split given int a list by spaces in given string
        giv_name = given.split(" ")

        # assign giv_first to first name and giv_last to last name
        giv_first = giv_name[0]
        giv_last = giv_name[-1]

        # if given name has a middle name assign giv_mid to middle name 
        if len(giv_name) > 2:
            giv_mid = giv_name[1:-1][0]
  
        # split each name in aliases. Assign first_name and last_name
        for alias in aliases:
            alias = alias.split(" ")
            
            alias_first = alias[0]
            alias_last = alias[-1]
            
            # if middle name exists assign mid_name, else it is None
            if len(alias)>2:
                alias_mid = alias[1:-1][0]
            else:
                alias_mid=None

            # if alias name matches given name, confirm middle name
            if alias_first == giv_first and alias_last == giv_last:
                
                # if middle name exists for given and alias name compare them
                if len(giv_name)>2:
                    if len(alias_mid)>1 and len(giv_mid)>1:
                        return giv_mid == alias_mid
                    elif len(alias_mid)==1 and len(giv_mid)>1:
                        return alias_mid == giv_mid[0]
                    elif len(alias_mid)>1 and len(giv_mid)==1:
                        return alias_mid[0] == giv_mid
                return True

        return False




if __name__=="__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print(" **** Correct **** ")

