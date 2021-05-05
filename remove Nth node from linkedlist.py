# Custom list node. DO NOT MODIFY.
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class RemoveNthNode:
    def removeNthNodeFromEnd(self, list, N):
        f = list
        b = f
        n = 0
        while n < N:
            if b.next:
                b = b.next
            else:
                if N - n == 1:
                    print("Out of range", n)
                    list = f.next
                    return list
            n += 1
        if n != N:
            print(n, N, "false")

        while b.next:
            f = f.next
            b = b.next
        f.next = f.next.next
        return list


if __name__ == "__main__":
    # lst = [1, 4, 3, 2, 5]
    # n = 2
    lst = [2, 4, 5]
    n = 3
    rnth = RemoveNthNode()
    hd = ListNode(lst[0])
    ll = hd
    for i in range(1, len(lst)):
        ll.next = ListNode(lst[i])
        ll = ll.next
    rlst = rnth.removeNthNodeFromEnd(hd, n)
    h = rlst
    while h:
        print(h.value)
        h = h.next
