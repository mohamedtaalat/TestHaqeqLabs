
class Utility:
    def test_element_is_present(self,element):
        assert element is not None

    def test_element_is_not_present(self,element):
        assert element is None

    def test_element_is_enabled(self,element):
        assert element.is_enabled() is True

    def test_element_is_disabled(self,element):
        assert element.is_disabled() is True