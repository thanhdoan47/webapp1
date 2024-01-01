def get_todos(filepath="todos.txt"):
  """
  To read a text file and return the list of
  that text file
  """
  with open(filepath, 'r') as file_local:
      todos_local = file_local.readlines()
  return todos_local

def write_todos(todo_arg, filepath="todos.txt"):
  with open(filepath, 'w') as file:
      file.writelines(todo_arg)

if "__name__" == "__main__":
   print("hello")
   print(get_todos())