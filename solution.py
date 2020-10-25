# found here : https://stackoverflow.com/questions/42475706/google-foobar-number-station-coded-messages
def solution(x,y):
    a=[-1,-1]
    c=list(x)
    for keyi,i in enumerate(c):
        for keyj,j in enumerate(c):
            if sum(x[keyi:keyj+1]) == y:
                return [keyi, keyj]
    return a
