def format_name(f_name, l_name):
    """The format name function allow me to change the first letter of the
    first and last name to captialize"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
