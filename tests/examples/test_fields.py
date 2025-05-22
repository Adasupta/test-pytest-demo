import pytest
from qase.pytest import qase


def load_markdown_content():
    with open("tests/examples/markdown.md", "r") as file:
        return file.read()


markdowncontent = load_markdown_content()


class Test_Priority:
    @qase.title("Test case with field: Priority - low")
    @qase.priority("low")
    def test_priority_low(self):
        assert True, "Test failed with priority: low"

    @qase.title("Test case with field: Priority - medium")
    @qase.priority("medium")
    def test_priority_medium(self):
        assert True, "Test failed with priority: medium"

    @qase.title("Test case with field: Priority - high")
    @qase.priority("high")
    def test_priority_high(self):
        assert True, "Test failed with priority: high"

class Test_Layer:
    @qase.title("Test case with field: Layer - e2e")
    @qase.layer("e2e")
    def test_layer_e2e(self):
        assert True, "Test failed with layer: e2e"

    @qase.title("Test case with field: Layer - api")
    @qase.layer("api")
    def test_layer_api(self):
        assert True, "Test failed with layer: api"

    @qase.title("Test case with field: Layer - unit")
    @qase.layer("unit")
    def test_layer_unit(self):
        assert True, "Test failed with layer: unit"


class Test_Description:
    @qase.title("Test case with Description field")
    @qase.description(markdowncontent)
    def test_description(self):
        assert markdowncontent is not None, "Description content is empty"


class Test_Preconditions:
    @qase.title("Test case with Preconditions field")
    @qase.preconditions(markdowncontent)
    def test_preconditions(self):
        assert markdowncontent is not None, "Preconditions content is empty"


class Test_Postconditions:
    @qase.title("Test case with Postconditions field")
    @qase.postconditions(markdowncontent)
    def test_postconditions(self):
        assert markdowncontent is not None, "Postconditions content is empty"


class Test_All_Fields:
    @qase.title("Test cases with all fields")
    @qase.fields(
        ("severity", "normal"),
        ("custom_field", "value"),
        ("priority", "high"),
        ("layer", "unit"),
        ("description", "Try logging to Qase TestOps using login and password"),
        ("preconditions", "*Precondition 1*. Markdown is supported."),
        ("postconditions", "*Postcondition 1*. Markdown is supported."),
    )
    def test_with_fields_success(self):
        assert 1 == 1
