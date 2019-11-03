

def print_path(head, end):         #输出路径
    print("#",head,"-->",end)

def move(n, head, middle, end):    #递归过程
    if(n == 1):
        print_path(head,end)
    else:
        move(n-1, head, end, middle)
        print_path(head, end)
        move(n-1, middle, head, end)



n = int(input('enter a number '))                   #输入盘子数量

move(n, 'a', 'b', 'c') 
