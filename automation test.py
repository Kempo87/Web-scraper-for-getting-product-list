from M05L20_projekt import extract

def test_extract_should_strip_texts():
    html = '<b> this should be stripped </b>'
    got = extract(html, '//b')
    expected = ['this should be stripped']
    assert got == expected

def test_extract_converts_newlines_to_spaces():
    html = '<b> this should be stripped/nthis is a new line</b>'
    got = extract(html, '//b')
    expected = ['this should be stripped this is a new line']
    assert got == expected
