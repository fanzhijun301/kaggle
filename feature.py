__author__ = 'fzj'

import utils

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
        arr = utils.split_str(line, ",")
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

def load_target_dict(target_file):
    in_target = open(target_file,"r")
    for line in in_target:
        line = line.strip()
        target_list = utils.split_str(line, ",");
        break
    target_dict = {}
    for i in range(len(target_list)):
        target = target_list[i]
        target_dict[target] = i
    return target_dict

def feature_extract(data_file, fea_dict, target_dict, fea_file):
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
        arr = utils.split_str(line, ",")
        tmp_fea_dict = {}
        cate_num = ""
        for i in range(len(arr)):
            head = head_list[i]
            value = arr[i]
            if head == "Category":
                if value not in target_dict:
                    print "{0} not in dict".format(value)
                    exit(0)
                cate_num = target_dict[value]
            value = deal_fea(head, value)

            if value == "":continue
            fea_name = "{0}={1}".format(head,value)
            if fea_name in fea_dict:
                index = int(fea_dict[fea_name])
                tmp_fea_dict[index] = "{0}:{1}".format(index, 1)
        keys = tmp_fea_dict.keys()
        keys.sort()
        fea_list = [tmp_fea_dict[key] for key in keys]
        fea_str = " ".join(fea_list)
        ou_fea.write(str(cate_num) + " " + fea_str + "\n")
    ou_fea.close()


if __name__ == "__main__":
    data_file = "D:/program/kaggle/crime/data/train1.csv"
    feadict_file = "D:/program/kaggle/crime/data/fea_dict.txt"
    train_fea_file = "D:/program/kaggle/crime/data/train_fea.txt"
    target_file = "D:/program/kaggle/crime/data/sampleSubmission.csv"
    #feature_dict(data_file, feadict_file)
    fea_dict = dict_load(feadict_file)
    target_dict = load_target_dict(target_file)
    feature_extract(data_file, fea_dict, target_dict, train_fea_file)
    print "ok"
