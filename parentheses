#user will enter number and the program will display valid parenthesis pair
#example if the user enter 2
#output will be (),(()),()()
def bracket(n):
    for i in range(1, n+1):
        makeBracket('',0,0,i)

def makeBracket(output, openP, closeP, pairs):
    if openP == pairs and closeP == pairs:
        print output
    if openP < pairs:
        makeBracket(output+'(' , openP+1, closeP, pairs)
    if closeP < openP:
        makeBracket(output+')', openP, closeP+1, pairs)
