def is_safe(board, row, col, n):
    # چک کردن ستون‌ها
    for i in range(row):
        if board[i][col] == 1:
            return False

    # چک کردن قطر اصلی
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # چک کردن قطر فرعی
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:  # شرط پایه: اگر به سطر n برسیم، یک جواب کامل داریم
        solutions.append([row[:] for row in board])  # کپی برداری از بورد
        return

    for col in range(n):
        if is_safe(board, row, col, n):  # اگر این مکان امن است
            board[row][col] = 1        # ملکه را قرار دهید
            solve_n_queens(board, row + 1, n, solutions)  # رفتن به سطر بعدی
            board[row][col] = 0         # بازگرداندن ملکه (backtracking)

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

# اجرای الگوریتم برای تعداد مشخصی از n
n = 5
solutions = n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
