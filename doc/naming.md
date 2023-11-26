# File naming
## Naming
File and folder names should be only in lowercase, short and concise, and only use underscores where necessary. <br/>

## Special files
Configuration files (excluding pip requirements) should be `.json` files. <br/>
Text files, for example docs, should be `.md` files. <br/>
Pip requirements should be a `.txt` file. <br/>

# Coding 

## Naming
- Functions should use camel case: e.g. `onMessageRecieved`. Methods should also follow this style.
- Variables should be lowercase, with underscores if needed: e.g. `current_iter`
- Classes should start with a captial letter: e.g. `WebappClient`
- Modules should be all-lowercase with underscores where necessary: e.g. `client_module`
- Constants should be in all-caps, with underscores where necessary: e.g.`EXAMPLE_CONST`
- Strings should use double-quotes for natural language (e.g. `"An error has occured"`) and single-quotes for string literals (e.g. `'module-name'`)

# Additional
If supported by the python version, type hints should be used. <br/>
For example: `def f(x): return False   ->   def f(x: int) -> bool: return False` 