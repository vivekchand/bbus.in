from BeautifulSoup import BeautifulSoup
def table2json(rows):
    table_data = [[cell.text for cell in (row("td") or row("th"))]
                             for row in rows]

    keys = table_data[0]
    values = table_data[1:]
    hops = []
    for value in values:
        json_dict = {}
        c = 0
        for ele in value:
            json_dict[keys[c]] = ele
            c+=1
        hops.append(json_dict)
    return hops


