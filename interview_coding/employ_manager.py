from typing import Tuple, List, Dict, Any, Set
import rich, json

ids: Dict[int, List[int]] = {}

def gen_dict(root: int) -> Dict[Any, Any]:
    sub: List[Dict[Any, Any]] = []
    for i in ids[root]:
        sub.append(gen_dict(i))
    ret: Dict[Any, Any] = {
        "id": root
    }
    if sub:
        ret["sub"] = sub
    return ret

def main(rel: List[Tuple[int, int]]):
    for employ, manager in rel:
        if employ not in ids:
            ids[employ] = []
        if manager not in ids:
            ids[manager] = []
        if employ not in ids[manager]:
            ids[manager].append(employ)
    root: Set[int] = set(i[1] for i in rel) - set(i[0] for i in rel)
    ret: List[Dict[Any, Any]] = []
    for id in root:
        ret.append(gen_dict(id))
        
    rich.print_json(json.dumps(ret))

test = [(2, 5), (5, 6), (1, 6)]

main(test)

'''
[
  {
    "id": 6,
    "sub": [
      {
        "id": 5,
        "sub": [
          {
            "id": 2
          }
        ]
      },
      {
        "id": 1
      }
    ]
  }
]
'''

class Node:
    def __init__(self, value: int, left, right):
        self.value = value
        self.left = left
        self.right = right

TreeType = List[Tuple[int, List[int]]]
tree: TreeType = [
    (100, [7, 9, 6]),
    (7, [33, 10]),
    (9, [5]),
    (6, [22, 8, 1]),
]
