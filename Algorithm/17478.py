#재귀함수가 뭔가요?
#함수를 선언을 해주고 나에 부르면 될거같은데 
#프린트로 바로 하나 나오고 
#1.재귀함수가 뭔가요?




# def recursive(m):
#     print("_"(4*(n-m))+"재귀함수가 뭔가요?")
    
#     if not m:
#         print("_"*(4*(n-m))+"재귀함수는 자기 자신을 호출하는 함수라네")
#         print("_"*(4*(n-m))+"라고 답변하였지.")
#         return

# print("_" * (4))
    
    
# n= int(input())
# print("어느 한 컴퓨터 공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recursive(n)

n= int(input())

def recur(i,n):
    print("____"*i+'"재귀함수가 뭔가요?')
    if i==n:
        print("____"*i+'"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print("____"*i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어')
        print("____"*i + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고. 모두 지혜롭게 대답해 주었지.')
        print("____"*i + '그의 답은 대부분 옳았다고 하ㄴ. 그런데 어느날 그 선인에게 한 선비가 찾아와서 물었어')
        recur(i+1,n)
    print("____"*i+"라고 답변하였지")
    
print("어느 한 컴공과 학생이 유명한 교수를 찾아가 물었다")
recur(0,n)

def recur(i,n):
    print("____"* i + '"재귀함수가 뭔가요?"')
    if i==n:
        print("____"*i+"dd")
    else:
        print("____"*i+"dd")
        recur(i+1,n)
    print("____"*i+"fkrh ")
    
print("djsm")
recur(0,n)


def recur(i,n):
    print("___"*i+'"dfdf"')
    if i==n:
        print()
    


