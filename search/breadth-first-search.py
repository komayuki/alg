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

#breadth first search
stack = data
safe = 0
visited = []
while stack:
    print(",".join(str(_['id']) for _ in stack))
    current = stack[0]
    visited.append(current)
    stack.pop(0)
    if len(current['children']) > 0:
        stack.extend(current['children'])

print (",".join([str(v['id']) for v in visited]))

# breadth first search
def bfs (list):
    stack = []
    for _ in list:
        print(str(_['id']) + '->')
        if len(_['children']) > 0:
            stack.extend(_['children'])

    if len(stack) > 0:
        bfs(stack)
bfs(data)
