import unittest
from exlist import ExList

class clacTest(unittest.TestCase):
    def test_map(self):
        print('Test map')
        orig = ExList([1,2,3,4,5])
        ideal = ExList([2,4,6,8,10])
        self.assertEqual(orig.map(lambda x:x*2), ideal)

    def test_filter(self):
        print('Test filter')
        orig = ExList([1,2,3,4,5])
        ideal = ExList([2,4])
        self.assertEqual(orig.filter(lambda x: x%2==0), ideal)

    def test_fold(self):
        print('Test fold')
        orig = ExList([1,2,3,4,5])
        ideal = 15
        self.assertEqual(orig.fold(0, lambda x,y: x+y), ideal)

    def test_foreach(self):
        import sys
        from io import StringIO

        print('Test foreach')
        io = StringIO()
        sys.stdout = io
        orig = ExList([1,2,3,4,5])
        orig.foreach(print)
        self.assertEqual(io.getvalue(), '1\n2\n3\n4\n5\n')
        sys.stdout = sys.__stdout__

    def test_flatten(self):
        print('Test flatten')
        lst = ExList([1,2])
        orig = ExList([lst,lst,lst])
        ideal = ExList([1,2,1,2,1,2])
        self.assertEqual(orig.flatten(), ideal)

    def test_flatmap(self):
        print('Test flatmap')
        orig = ExList([1,2,3,4,5])
        def f(x):
            return ExList([x])
        self.assertEqual(orig.flatmap(f), orig)

    def test_slice(self):
        print('Test drop')
        orig = ExList([1,2,3,4,5])
        ideal = ExList([3,4])
        self.assertEqual(orig[2:4], ideal)

    def test_drop(self):
        print('Test drop')
        orig = ExList([1,2,3,4,5])
        ideal = ExList([3,4,5])
        self.assertEqual(orig.drop(2), ideal)

    def test_take(self):
        print('Test take')
        orig = ExList([1,2,3,4,5])
        ideal = ExList([1,2,3])
        self.assertEqual(orig.take(3), ideal)

if __name__ == '__main__':
    unittest.main()
