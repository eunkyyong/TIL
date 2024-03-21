def make_set(date):
    idx = data.index(date)
    p[idx] = idx
    rank[idx] = 0
    # print(p)
# data가 포함된 셋의 대표의 idx를 return
def find_set(date):
    idx = data.index(date)
    while idx != p[idx]:
        idx = p[idx]
    return idx
def link(idx1, idx2):
    if rank[idx1] < rank[idx2]:
        p[idx1] = idx2
    else:
        p[idx2] = idx1
        if rank[idx1] == rank[idx2]:
            rank[idx1] += 1
def union(date1, date2):
    idx1 = find_set(date1)
    idx2 = find_set(date2)
    link(idx1, idx2)
def union_old(date1,date2):
    idx1 = find_set(date1)
    idx2 = find_set(date2)
    if idx1 < idx2:
        p[idx2] = idx1
    else:
        p[idx1] = idx2


data = ['a', 'b', 'c', 'd', 'e', 'f']
p = [-1] * len(data)
rank = [-1] * len(data)
for d in data:
    make_set(d)
# p[3] = 2
# print(find_set('c'))
# print(find_set('d'))
union('c', 'd')
print(p)
union('e', 'f')
print(p)
print(find_set('e'))
print(find_set('d'))