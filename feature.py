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


def feature_select(data_file, feature_dict_file):
    in_data = open(data_file, "r")
    first = True
    head_list = []
    fea_dict = {}
    curr_max_index = 0
    for line in in_data:
        line = line.strip()

        arr = line.split(",")
        if first == True:
            first = False
            for i in range(len(arr)):
                head_list.append(arr[i])
            continue
        print line
        print len(head_list)
        print len(arr)
        for i in range(len(arr)):
            head = head_list[i]
            value = arr[i]
            value = deal_fea(head, value)
            if value == "":continue
            fea_name = head + "_" + value
            if fea_name in fea_dict: continue
            fea_dict[fea_name] = curr_max_index
            curr_max_index += 1
    in_data.close()

    ou_feadict = open(feature_dict_file, "w")
    for k, v in fea_dict.iteritems():
        ou_feadict.write(str(k) + "\t" + str(v) + "\n")
    ou_feadict.close()

if __name__ == "__main__":
    data_file = "D:/program/kaggle/crime/data/train1.csv"
    feadict_file = "D:/program/kaggle/crime/data/fea_dict.txt"
    feature_select(data_file, feadict_file)
    print "ok"
