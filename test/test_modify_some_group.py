from model.group import Group
from random import randrange


def test_modify_some_group_name(app, data_groups):
    group = data_groups
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.ident = old_groups[index].ident
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups) == sorted(new_groups)
