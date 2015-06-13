# first line: 7
@mem.cache
def get_data(fea_file):
    data = load_svmlight_file(fea_file)
    return data[0], data[1]
