class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """


    if user in group.users:
        return True

    for group in group.groups:
        if is_user_in_group(user, group):
            return True
    return False


# Test Case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group('sub_child_user', child))
# Returns True because subchild belongs to child group

print(is_user_in_group('another_sub_child_user', child))
# Returns False because user does not exist

# Test Case 2: Create a new detached group and search for a user
grand_parent = Group('grand_parent')
uncle = Group('uncle')

print(is_user_in_group('sub_child_user', grand_parent))
# Returns False

# Test Case 3: Attach group to an olders group
grand_parent.add_group(parent)
grand_parent.add_group(uncle)
uncle.add_user('uncle_user')

print(is_user_in_group('sub_child_user', grand_parent))
# Returns True because subchild is now a child of grandparent

print(is_user_in_group('uncle_user', grand_parent))
# Returns True
print(is_user_in_group('uncle_user', parent))
# Returns False
print(is_user_in_group(None, parent))
# Returns False

