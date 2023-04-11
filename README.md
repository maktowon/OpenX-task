# OpenX-task
Recruitment task for OpenX.

## tree.py
Implements the functions asked in the task.
### Structure
Node contains of:
  - left Node
  - value
  - right Node

### Functions:
- count_leaves(root):
  * return the numbers of leaves in a tree starting at given root.
- length(root):
  * return the maximum length of a tree starting at given root (by edges).
- are_equal(t, u):
  * return whether the trees starting at roots t and u are equal (has the same structure and values in corresponding nodes).

- test(t1, t2, l1, l2, d1, d2, eq):
  * compare results of implemented functions (on t1, t2) to corresponding values passed as an arguments.
 
## main.py
Tests the implemented functions on some given inputs. Uses the methods imported from __tree.py__ file.
