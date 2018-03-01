data = [
    {
        'id': 1,
        'children': [
            {
                'id': 8,
                'children': []
            }
        ]
    },
    {
        'id': 2,
        'children': [
            {
                'id': 3,
                'children': [
                    {
                        'id': 4,
                        'children': []
                    },
                    {
                        'id': 7,
                        'children': []
                    }
                ]
            }
        ]
    },
    {
        'id': 5,
        'children': [
            {
                'id': 6,
                'children': []
            }
        ]
    }
]

#depth first search
stack = data
safe = 0
visited = []
while stack:
    print(",".join(str(_['id']) for _ in stack))
    current = stack[0]
    visited.append(current)
    stack.pop(0)
    if len(current['children']) > 0:
        for a in current['children']:
            stack.insert(0, a)


    if safe > 50:
        break
    safe = safe + 1

print (",".join([str(v['id']) for v in visited]))

# depath first search
def dfs(list):
    for _ in list:
        print (_)
        if len(_['children']) > 0:
            dfs(_['children'])
dfs (data)
