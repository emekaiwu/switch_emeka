def mod_list(stringchar):
    item_list = []
    for index in range(len(stringchar)):
        if index ==0:
            modulo='NAN'
        else:
            modulo = len(stringchar)%index
        item_listappend(modulo)
    return item_list
mod_list(stringchar)

