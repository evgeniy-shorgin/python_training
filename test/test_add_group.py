

def test_add_group(app, json_groups):
    a_group = json_groups
    old_groups = app.group.get_group_list()
    group = app.group.create(a_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    group.ident = new_groups[new_groups.index(group) + new_groups.count(group) - 1].ident
    old_groups.append(group)
    # new_groups already sorted
    assert sorted(old_groups) == sorted(new_groups)
