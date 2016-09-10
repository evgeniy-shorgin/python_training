from model.group import Group
import random


def test_modify_some_group_name(app, db, json_groups):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_to_modify = random.choice(old_groups)
    app.group.modify_group_by_id(group_to_modify.ident, group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_to_modify)] = group
    assert old_groups == new_groups
