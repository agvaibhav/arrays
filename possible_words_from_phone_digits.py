#code
keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

def print_keypad(no, out, i, j):
    if i == len(no):
        print(''.join(out),end=' ')
        return
    
    digit = no[i]
    
    for k in range(len(keypad[digit])):
        out[j] = keypad[digit][k]
        print_keypad(no, out, i+1, j+1)

t = int(input())
for _ in range(t):
    n = int(input())
    no = list(map(int, input().split()))
    out = ['']*n
    print_keypad(no,out,0,0)
    print()
