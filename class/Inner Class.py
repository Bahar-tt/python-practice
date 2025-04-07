class MySet(set):
    def union_and_square(self, other_set):
        result = self.union(other_set)
        squared_result = {x**2 for x in result}
        print(squared_result)


set1 = MySet({1, 2, 3})
set2 = MySet({3, 4, 5})
set1.union_and_square(set2)
