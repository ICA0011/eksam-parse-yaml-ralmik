[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7975821&assignment_repo_type=AssignmentRepo)
## Parsing yaml

You need to find out what user has admin permissions and return the **full name** of the user.

File structure information is available:
```
- username
  - name
  - permission
```
use ```text``` method for ```requests.get``` to obtain file content before parsing.

The number of users and their properties may vary (theoretically), so **do not use numerical indexes** for them, but cycles instead.
```['users'][1]['permission']``` will probably return the correct answer, but is not considered a correct solution.
