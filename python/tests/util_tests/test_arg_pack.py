import ecl
from ecl import EclPrototype
from tests import EclTest
from ecl.util import ArgPack, StringList

TEST_LIB = EclPrototype.lib


class ArgPackTest(EclTest):
    def test_create(self):
        arg = ArgPack()
        self.assertEqual(len(arg), 0)

        arg.append(StringList())
        self.assertEqual(len(arg), 1)

        arg.append(3.14)
        self.assertEqual(len(arg), 2)

        o = object()
        with self.assertRaises(TypeError):
            arg.append(o)

    def test_args(self):
        arg = ArgPack(1, 2, 3)
        self.assertEqual(len(arg), 3)

    def test_append_ptr(self):
        arg = ArgPack(StringList())
        self.assertEqual(len(arg), 1)

        func = getattr(TEST_LIB, "test_argpack_is_stringlist")
        func.restype = None
        func.argtypes = [ArgPack]

        func(arg)
