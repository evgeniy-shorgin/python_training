

def test_add_group(app, db, json_groups, check_ui):
    a_group = json_groups
    old_groups = db.get_group_list()
    group = app.group.create(a_group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)
    if check_ui:
        assert sorted(new_groups) == sorted(app.group.get_group_list())
