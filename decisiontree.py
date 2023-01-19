class TreeNode:
    def __init__(self,condwordic):
        self.num = None
        self.left=None
        self.right=None
        self.decision=None
        self.condwordic=condwordic
        self.parent = None

    def add_leftchild(self, child,number):
        child.parent = self
        child.num=number
        self.left=child

    def add_rightchild(self, child,number):
        child.parent = self
        child.num = number
        self.right=child

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.condwordic)+'-->'+str(self.decision) + '-->'+str(self.num))
        if self.left:
                self.left.print_tree()
        elif self.right:
            self.right.print_tree()


def build_tree(p,q):
    isrational = TreeNode("Is rational")
    isrational.num=str(p)+'/'+str(q)
    irrational = TreeNode("Irrational")
    isinteger = TreeNode("IsInteger")
    fractional=TreeNode("Fractional")
    ispositive=TreeNode("IsPositive")
    Negative=TreeNode("Negative")
    isNaturalorWhole=TreeNode("isNaturalorWhole")
    NaturalAndWhole=TreeNode("Natural")
    OnlyWholeNumber=TreeNode("OnlyWholeNumber")
    if(q==0):
        isrational.add_leftchild(irrational,str(p)+'/'+str(q))
        isrational.decision="No"

    else:
        isrational.add_rightchild(isinteger,str(p)+'/'+str(q))
        isrational.decision="Yes"
        if(p%q!=0):
            isinteger.add_leftchild(fractional,str(p)+'/'+str(q))
            isinteger.decision="No"
        else:
            isinteger.add_rightchild(ispositive,str(p)+'/'+str(q))
            isinteger.decision="Yes"
            if (p / q >= 0):
                ispositive.add_rightchild(isNaturalorWhole,str(p)+'/'+str(q))
                ispositive.decision="Yes"
                if p==0:
                    isNaturalorWhole.add_rightchild(OnlyWholeNumber,str(p)+'/'+str(q))
                    isNaturalorWhole.decision="Whole"
                else:
                    isNaturalorWhole.add_leftchild(NaturalAndWhole,str(p)+'/'+str(q))
                    isNaturalorWhole.decision="Natural and Whole"
            else:
                ispositive.add_leftchild(Negative,str(p)+'/'+str(q))
                ispositive.decision="No"

    return isrational


if __name__=='__main__':
    p = int(input("\nEnter Number 1 which is p in p/q form :-\n"))
    q = int(input("\nEnter Number 2 Which is q in p/q from :-\n"))
    root = build_tree(p,q)

    root.print_tree()
    print(root.num)
