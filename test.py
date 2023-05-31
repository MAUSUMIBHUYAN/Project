def print(cards,conceal):
    c = ""
    for i in cards:
        c = c + "\t ________________"
    if conceal:
        c += "\t ________________"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|                |"
    if conceal:
        c += "\t|                |"
    print(c)

    c = ""
    for i in cards:
        if i.value == '10':
            c = c + "\t|   {}               |".format(i.value)
        else:
            c = c + "\t|   {}                |".format(i.value)
    if conceal:
        c += "\t|                |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|                |"  
    if conceal:
        c += "\t|      * *      |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|                |"  
    if conceal:
        c += "\t|     *   *     |"
    print(c)

    c = "" 
    for i in cards:
        c = c + "\t|               |"  
    if conceal:
        c += "\t|    *     *    |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|               |"  
    if conceal:
        c += "\t|   *       *   |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|        {}       |".format(i.shape)
    if conceal:
        c += "\t|           *   |" 
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|          *    |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|         *     |"
    print(c)

    c = "" 
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|               |"
    print(c)

    c = "" 
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|               |"
    print(c)

    c = ""
    for i in cards:
        if i.value == '10':
            c = c + "\t|           {}        |".format(i.value)
        else:
            c = c + "\t|           {}         |".format(i.value)
    if conceal:
        c += "\t|        *       |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|________________|"
    if conceal:
        c += "\t|________________|"
    print(c)   
    print()
    


                






