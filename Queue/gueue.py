from collections import deque

# ایجاد صف خالی
queue = deque()

# افزودن مشتری به صف
queue.append("مشتری 1")
queue.append("مشتری 2")
queue.append("مشتری 3")

# نمایش وضعیت صف
print("وضعیت صف:", queue)

# حذف مشتری از صف
queue.popleft()

# نمایش وضعیت صف بعد از حذف
print("وضعیت صف بعد از حذف:", queue)
