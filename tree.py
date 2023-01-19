class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None


    def add_child(self,child):
       child.parent =self
       self.children.append(child)

def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("laptop")

    root.add_child(laptop)


 if __name__=='__main__':
   build_product_tree()