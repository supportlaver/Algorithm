def reverse_list(head):
    node, prev = head, None
    while node:
        # 3개의 포인터가 필요하다 (prev , node , next)
        # prev 에 None 을 먼저 넣어주고 현재 노드가 prev 를 가리키게 한다.
        # 그렇게 되면 현재 노드의 next 링크가 끊어지기 떄문에 참조할 수 없어서 next 라는 포인터가 필요하다.
        # 그래서 next 에 node.next 를 넣어주면서 , node.next 는 prev 를 넣는다.
        # 이렇게 1->None 을 가리키게 되고 원래의 1->2 를 가리키는 포인터는 next 에 저장되어 있다.
        # 그 후에 한 칸씩 옆으로 옮겨주기 위해서 prev 에는 현재 노드를 , 현재 노드는 next 로 옮긴다.
        next, node.next = node.next, prev
        prev, node = node, next
    return prev