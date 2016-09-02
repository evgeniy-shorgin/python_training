from model.group import Group
from random import randrange
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


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modify_some_group_name(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="name_edited")
    group.ident = old_groups[index].ident
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups) == sorted(new_groups)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="header_edited"))
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
