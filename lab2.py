####### вариант 2 задача 1
# print(len(set(input().split()) & set(input().split())))


####### вариант 12 задача 2
p = {}
n = int(input())  # число записей о родстве
for _ in range(n):
    child, parent = input().split()
    p[child] = parent

def is_ancestor(anc, desc):
    while desc in p:
        if p[desc] == anc:
            return True
        desc = p[desc]
    return False

k = int(input())  # число запросов
for _ in range(k):
    a, b = input().split()
    if is_ancestor(a, b):
        print(1)
    elif is_ancestor(b, a):
        print(2)
    else:
        print(0)