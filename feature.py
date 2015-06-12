__author__ = 'fzj'


def deal_fea(head, value):
    """
    :param head:
    :param value:
    :return:
    """
    r_value = ""
    if head == "Dates":
        value = value.split(" ")[1]
        r_value = value.split(":")[0]
    elif (head == "DayOfWeek") | (head == "PdDistrict"):
        r_value = value

    return r_value

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


def feature_dict(data_file, feature_dict_file):
    in_data = open(data_file, "r")
    first = True
    head_list = []
    fea_dict = {}
    curr_max_index = 0
    for line in in_data:
        line = line.strip()

        if first == True:
            first = False
            arr = line.split(",")
            for i in range(len(arr)):
                head_list.append(arr[i])
            continue
        arr = split_str(line, ",")
        for i in range(len(arr)):
            head = head_list[i]
            value = arr[i]
            value = deal_fea(head, value)
            if value == "":continue
            fea_name = head + "=" + value
            if fea_name in fea_dict: continue
            fea_dict[fea_name] = curr_max_index
            curr_max_index += 1
    in_data.close()

    ou_feadict = open(feature_dict_file, "w")
    for k, v in fea_dict.iteritems():
        ou_feadict.write(str(v) + "\t" + str(k) + "\n")
    ou_feadict.close()

def dict_load(fea_dict_file):
    fea_dict = {}
    in_fea_dict = open(fea_dict_file, "r")
    for line in in_fea_dict:
        line = line.strip()
        tab_pos = line.find("\t")
        index = line[:tab_pos]
        value = line[tab_pos+1:]
        fea_dict[value] = index
    in_fea_dict.close()
    return fea_dict

def feature_extract(data_file, fea_dict, fea_file):
    ou_fea = open(fea_file, "w")
    in_data = open(data_file, "r")
    head_list = []
    first = True
    for line in in_data:
        line = line.strip()
        if first == True:
            first = False
            arr = line.split(",")
            for i in range(len(arr)):
                head_list.append(arr[i])
            continue
        arr = split_str(line, ",")
        fea_list = []
        for i in range(len(arr)):
            head = head_list[i]
            value = arr[i]
            value = deal_fea(head, value)
            if value == "":continue
            fea_name = head + "=" + value
            if fea_name in fea_dict:
                index = fea_dict[fea_name]
                fea_list.append("{0}:{1}".format(index, 1))
        fea_str = " ".join(fea_list)
        ou_fea.write(fea_str + "\n")
    ou_fea.close()


if __name__ == "__main__":
    data_file = "D:/program/kaggle/crime/data/train1.csv"
    feadict_file = "D:/program/kaggle/crime/data/fea_dict.txt"
    train_fea_file = "D:/program/kaggle/crime/data/train_fea.txt"
    #feature_dict(data_file, feadict_file)
    fea_dict = dict_load(feadict_file)
    feature_extract(data_file, fea_dict, train_fea_file)
    print "ok"
