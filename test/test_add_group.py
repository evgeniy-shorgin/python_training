from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


@pytest.mark.parametrize("a_group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, a_group):
    old_groups = app.group.get_group_list()
    group = app.group.create(a_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    group.ident = new_groups[new_groups.index(group) + new_groups.count(group) - 1].ident
    old_groups.append(group)
    # new_groups already sorted
    assert sorted(old_groups) == sorted(new_groups)
