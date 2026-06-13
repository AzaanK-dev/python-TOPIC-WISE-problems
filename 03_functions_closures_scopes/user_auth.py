# Create a user authentication function.
# After login:
# Return functions that allow specific actions.
# Permissions depend on the logged-in role.
# Roles and permissions must remain remembered after login.



def auth(user):
    content = "Hello this is me"
    def view():
        return content  # just reading 'content'
    def edit(new_cont): 
        nonlocal content   # for editing that content also
        content = new_cont
        return print("Edited!")
    def delete():
        nonlocal content
        content = ""
        return print("Deleted!")
    if user=="admin":
        return view,edit,delete
    elif user=="editor":
        return view,edit
    elif user=="guest":
        return view
    else:
        return print("Invalid")

v,e,d = auth("admin")
print(v())
e("No this is not you")
print(v())
d()
print(v())

