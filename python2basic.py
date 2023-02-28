import ast

def generate_basic_code(node):
    if isinstance(node, ast.Module):
        return "\n".join([generate_basic_code(child_node) for child_node in node.body])
    elif isinstance(node, ast.Assign):
        return f"{node.targets[0].id} = {generate_basic_code(node.value)}"
    elif isinstance(node, ast.BinOp):
        return f"{generate_basic_code(node.left)} {generate_basic_operator(node.op)} {generate_basic_code(node.right)}"
    elif isinstance(node, ast.Compare):
        return f"{generate_basic_code(node.left)} {generate_basic_operator(node.ops[0])} {generate_basic_code(node.comparators[0])}"
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Num):
        return str(node.n)
    elif isinstance(node, ast.If):
        basic_code = "IF " + generate_basic_code(node.test) + " THEN\n"
        for child_node in node.body:
            basic_code += generate_basic_code(child_node) + "\n"
        if node.orelse:
            basic_code += "ELSE\n"
            for child_node in node.orelse:
                basic_code += generate_basic_code(child_node) + "\n"
        basic_code += "END IF"
        return basic_code
    elif isinstance(node, ast.Expr):
        return "PRINT " + str(generate_basic_code(node.value))
    else:
        pass
        #raise ValueError(f"Unsupported node type: {node}")

def generate_basic_operator(op):
    if isinstance(op, ast.Add):
        return "+"
    elif isinstance(op, ast.Sub):
        return "-"
    elif isinstance(op, ast.Mult):
        return "*"
    elif isinstance(op, ast.Div):
        return "/"
    elif isinstance(op, ast.Mod):
        return "MOD"
    elif isinstance(op, ast.Gt):
        return ">"
    elif isinstance(op, ast.GtE):
        return ">="
    elif isinstance(op, ast.Lt):
        return "<"
    elif isinstance(op, ast.LtE):
        return "<="
    elif isinstance(op, ast.Eq):
        return "="
    elif isinstance(op, ast.NotEq):
        return "<>"
    else:
        raise ValueError(f"Unsupported operator: {op}")

py_code = '''
x = 2
y = 3
z = x + y
if z > 5:
    print("Result is greater than 5")
else:
    print("Result is less than or equal to 5")
'''

ast_tree = ast.parse(py_code)
basic_code = generate_basic_code(ast_tree)
print(basic_code)

