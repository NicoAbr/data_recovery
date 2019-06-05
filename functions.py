# find more than one index (from: https://stackoverflow.com/questions/...
# 			6294179/how-to-find-all-occurrences-of-an-element-in-a-list)
def getIdx(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)