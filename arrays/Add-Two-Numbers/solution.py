# LeetCode: 2. Add Two Numbers
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))

# First is a reference to the first node we'll create.
first = None

# Carry stores the value that needs to be carried
# to the next digit.
carry = 0

# Continue while at least one linked list still has nodes.
while l1 or l2:

    # Get the current value from l1.
    # If l1 is finished, use 0.
    if l1:
        x = l1.val
    else:
        x = 0

    # Get the current value from l2.
    # If l2 is finished, use 0.
    if l2:
        y = l2.val
    else:
        y = 0

    # Add the two digits together with the carry
    # from the previous calculation.
    total = x + y + carry

    # The current node stores only the last digit.
    node_value = total % 10

    # Calculate the carry for the next digit.
    carry = total // 10

    # Create a new node containing the calculated digit.
    new_node = ListNode(node_value)

    # If this is the first node, save it as the head.
    if first is None:
        first = new_node
        previous = new_node
    else:
        # Attach the new node to the previous node.
        previous.next = new_node
        previous = new_node

    # Move to the next node in l1 if it exists.
    if l1:
        l1 = l1.next

    # Move to the next node in l2 if it exists.
    if l2:
        l2 = l2.next

# If there is still a carry after processing both lists,
# create one final node for it.
if carry:
    previous.next = ListNode(carry)

# Return the head of the resulting linked list.
return first
