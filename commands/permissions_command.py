from util.plugin import command
import util.permissions as permissions


@command(name="perms", help="Permissions management command", aliases="permissions, perm",
         permission="command.permissions")
def perms(chat, message, args, sender):
    if len(args) == 0:
        chat.SendMessage("Provide parameters")
        return
    if len(args) < 2:
        chat.SendMessage("Provide a subparam and a user.")
        return
    handle = args[1]
    if args[0] == "add":
        if len(args) < 3:
            chat.SendMessage("Provide a permission to set.")
            return
        permissions.add_permission(handle, args[2])
        chat.SendMessage("Permission added.")
    elif args[0] == "remove":
        if len(args) < 3:
            chat.SendMessage("Provide a permission to remove.")
            return
        permissions.remove_permission(handle, args[2])
        chat.SendMessage("Permission removed.")
    elif args[0] == "list":
        temp = ''
        for perm in permissions.get_permissions(handle):
            temp += perm + ", "
        temp = temp[:2]
        chat.SendMessage("Permissions: " + temp)
    else:
        chat.SendMessage("Invalid argument.")
        return


@command(name='op', help='Make a user operator.')
def op_command(chat, message, args, sender):
    if len(args) == 0:
        chat.SendMessage("Provide a user to make operator.")
        return
    operator = args[0].lower()
    valid = permissions.add_operator(operator)
    if valid:
        chat.SendMessage("Successfully made {} operator.".format(operator))
    else:
        chat.SendMessage("Unable to make {} operator.")


@command(name='deop', help='Remove a user\' operator status.')
def deop_command(chat, message, args, sender):
    if len(args) == 0:
        chat.SendMessage("Provide a user to remove as operator.")
        return
    operator = args[0].lower()
    valid = permissions.remove_operator(operator)
    if valid:
        chat.SendMessage("Successfully removed {} as operator.".format(operator))
    else:
        chat.SendMessage("Unable to remove {} as operator.")