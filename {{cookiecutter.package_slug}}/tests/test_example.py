from {{ cookiecutter.package_module }}.example import org_details


def test_org_details():
    org = org_details('deepfield')
    assert org['name'] == 'Nokia Deepfield'
    assert org['blog'] == 'http://www.deepfield.com'
