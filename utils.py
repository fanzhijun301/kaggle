__author__ = 'zhijunfan'

def split_str(line, spliter):
    if line.find("\"") < 0: return line.split(spliter)
    arr_list = []
    pos = line.find(spliter)
    while pos > 0:
        field = line[:pos]
        if field.find("\"") < 0:
            arr_list.append(field)
            line = line[pos+1:]
            pos = line.find(spliter)
            continue
        npos = line.find("\"", pos)
        pos = line.find(spliter, npos)
        field = line[:pos]
        arr_list.append(field)
        line = line[pos+1:]
        pos = line.find(spliter)
    arr_list.append(line)
    return arr_list

if __name__ == "__main__":
    str = "2015-05-13 23:53:00,OTHER OFFENSES,TRAFFIC VIOLATION ARREST,Wednesday,NORTHERN,\"ARREST, BOOKED\",OAK ST / LAGUNA ST,-122.425891675136,37.7745985956747"
    arr = split_str(str, ",")
    print arr
