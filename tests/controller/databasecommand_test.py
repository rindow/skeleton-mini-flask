
def test_create_schema(runner):
    result = runner.invoke(args=['create-schema'])
    assert 'Initialized the database' in result.output


def test_drop_schema(runner):
    result = runner.invoke(args=['drop-schema'])
    assert 'Drop the database' in result.output
