def decorate_message(fun):
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)

    return addWelcome


@decorate_message
def site(site_name):
    return site_name


print(site("GeeksforGeeks"))
