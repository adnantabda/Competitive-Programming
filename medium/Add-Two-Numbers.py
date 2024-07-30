def addTwo(l1,l2):
    current = ListNode()
    carry = 0
    while l1 or l2 or carry:
        value_1 = l1.val if l1 else 0
        value_2 = l2.val if l1 else 0

        val = value_1 + value_2 + carry
        carry = val // 10 
        val = val%10
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None


    return current.next


 

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(addTwo(l1, l2))




