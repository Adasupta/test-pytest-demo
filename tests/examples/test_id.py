from qase.pytest import qase


@qase.id(
    440
)  # Please, replace the id (1), with an existing test case Id from your project.
def test_qase_id():
    assert True


@qase.id(
    [439, 441]
)  # The result of this test case will be posted against the linked test cases.
def test_multiple_qase_id():
    assert True
