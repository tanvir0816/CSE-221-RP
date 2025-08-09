def solve(inorder, postorder):
    if not inorder:
        return []
    root = postorder[-1]
    idx = inorder.index(root)
    Linorder = inorder[:idx]
    Lpost = postorder[:idx]
    Rinorder = inorder[idx+1:]
    Rpost = postorder[idx:-1]
    return [root] + solve(Linorder, Lpost) + solve(Rinorder, Rpost)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = solve(inorder, postorder)
print(" ".join(map(str, preorder)))
