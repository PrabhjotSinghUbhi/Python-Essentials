# 03_datatypes_in_python.py

# Introduction to Data Types in Python (with Java Comparison)

# 1. Integer
# Python: int (no size limit)
# Java: int (32-bit), long (64-bit), etc.
python_int = 42
print("Python int:", python_int, type(python_int))
# Java: int x = 42;

# 2. Floating Point Number
# Python: float (double-precision)
# Java: float (32-bit), double (64-bit)
python_float = 3.14
print("Python float:", python_float, type(python_float))
# Java: double y = 3.14;

# 3. String
# Python: str (immutable)
# Java: String (immutable)
python_str = "Hello, World!"
print("Python str:", python_str, type(python_str))
# Java: String s = "Hello, World!";

# 4. Boolean
# Python: bool (True/False)
# Java: boolean (true/false)
python_bool = True
print("Python bool:", python_bool, type(python_bool))
# Java: boolean b = true;

# 5. List (like ArrayList in Java)
# Python: list (mutable, can hold mixed types)
# Java: ArrayList (must specify type, e.g., ArrayList<Integer>)
python_list = [1, 2, 3, "four"]
print("Python list:", python_list, type(python_list))
# Java: ArrayList<Object> list = new ArrayList<>();

# 6. Tuple (like immutable list)
# Python: tuple (immutable)
# Java: No direct equivalent, but can use arrays with final
python_tuple = (1, 2, 3)
print("Python tuple:", python_tuple, type(python_tuple))

# 7. Dictionary (like HashMap in Java)
# Python: dict (key-value pairs)
# Java: HashMap<Key, Value>
python_dict = {"name": "Alice", "age": 25}
print("Python dict:", python_dict, type(python_dict))
# Java: HashMap<String, Object> map = new HashMap<>();

# 8. Set (unique elements, unordered)
# Python: set
# Java: HashSet
python_set = {1, 2, 3, 2}
print("Python set:", python_set, type(python_set))
# Java: HashSet<Integer> set = new HashSet<>();

# Summary Table:
# | Concept      | Python         | Java                |
# |--------------|---------------|---------------------|
# | Integer      | int           | int, long           |
# | Float        | float         | float, double       |
# | String       | str           | String              |
# | Boolean      | bool          | boolean             |
# | List         | list          | ArrayList           |
# | Tuple        | tuple         | (no direct)         |
# | Dictionary   | dict          | HashMap             |
# | Set          | set           | HashSet             |