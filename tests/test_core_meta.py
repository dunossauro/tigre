from unittest import TestCase
from tigre.core.meta import Builder


class TestBuilder(TestCase):
    def test_Builder_should_check_subclass_builder(self):
        class BuilderTest(Builder):
            build = None

        self.assertIsInstance(BuilderTest(), Builder)

    def test_Builder_raises_when_builder_no_has_build_method(self):
        class BuilderTest(Builder):
            ...

        with self.assertRaises(TypeError):
            b = BuilderTest()
