class Type:
    def __str__(self) -> str:
        return "Type()"

class AutoType(Type):
    def __str__(self) -> str:
        return "AutoType()"

class MT22:
    increate_ID = 0
    def __init__(self, name : str, typ : Type):
        self.ID = MT22.increate_ID
        self.name = name
        self.typ = typ
        MT22.increate_ID += 1
        
class VarMT22(MT22):
    def __init__(self, name : str, typ: Type):
        super().__init__(name, typ)

    def __str__(self):
        return f"VarMT22(#{self.ID}, {self.name}, {str(self.typ)})"
        
class ParamMT22(MT22):
    def __init__(self, name : str, typ: Type, out : bool = False, inherit : bool = False):
        super().__init__(name, typ)
        self.out = out
        self.inherit = inherit

    def __str__(self):
        return f"ParamMT22(#{self.ID}, {self.name}, {str(self.typ)}, {self.out}, inherit={self.inherit})"

class FuncMT22(MT22):
    def __init__(self, name : str, typ: Type, param : list[ParamMT22], parent : MT22 | None = None):
        super().__init__(name, typ)
        self.param = param
        self.parent = parent
        
    def __str__(self):
        return f"FuncMT22(#{self.ID}, {self.name}, {str(self.typ)}, [{", ".join([str(param) for param in self.param])}]{f", inherit=#{self.parent.ID}" if self.parent else ""})"      

class Access():
    def __init__(self, symbol : list[list[VarMT22 | ParamMT22]], typeLeft : Type = AutoType()):
        self.symbol = symbol 
        self.typeLeft = typeLeft
    
    def __str__(self):
        symbol_str = '\n\t\t\t   '.join([ '[' + (', '.join(map(str, row))) + ']' for row in self.symbol])
        return f"Access({self.typeLeft}, [{symbol_str}])"

class Tool():
    def printVarMT22(varMT22 : VarMT22 | ParamMT22):
        return str(varMT22)
    
    def printListVarMT22(ListVarMT22 : list[VarMT22 | ParamMT22]):
        return f"[ {', '.join(map(Tool.printVarMT22, ListVarMT22))} ]"

    def printListInListVarMT22(ListVarMT22 : list[list[VarMT22 | ParamMT22]]):
        return f"[\n\t{'\n\t'.join(map(Tool.printListVarMT22, ListVarMT22))}\n]"
    
    def printFunctionMT22(funcMT22 : FuncMT22):
        return str(funcMT22)
    
    def printListFunctionMT22(ListfuncMT22 : list[FuncMT22]):
        return f"[\n\t{'\n\t'.join(map(Tool.printFunctionMT22, ListfuncMT22))}\n]"
    
    def printAccess(access : Access):
        return f"Access(\n typeLeft = {access.typeLeft}\n symbol = {Tool.printListInListVarMT22(access.symbol)})"
    
class __main__():
    listVarMT22 = [
        VarMT22("var_a", Type()),
        VarMT22("var_b", Type()),
        ParamMT22("param_a", AutoType(), True, False),
        VarMT22("var_c", Type()),
    ]
    print("printVarMT22 : " + Tool.printVarMT22(listVarMT22[0]))
    print("printVarMT22 : " + Tool.printVarMT22(listVarMT22[2]))
    print("printListVarMT22 :" + Tool.printListVarMT22(listVarMT22))

    listInListVarMT22 = [
        listVarMT22,
        [ParamMT22("param_b", AutoType(), True, False)],
        [VarMT22("var_d", Type()), VarMT22("var_e", Type()),]
    ]
    print("printListInListVarMT22 :" + Tool.printListInListVarMT22(listInListVarMT22))


    listFunctionMT22 = [
        FuncMT22("fun_a", AutoType(), [listVarMT22[2], ParamMT22("param_b", AutoType(), True, False)], None)
    ]
    listFunctionMT22.append(FuncMT22("fun_b", AutoType(), [ParamMT22("param_c", AutoType(), False, True)], listFunctionMT22[0]))
    print("printFunctionMT22 : " + Tool.printFunctionMT22(listFunctionMT22[0]))
    print("printFunctionMT22 : " + Tool.printFunctionMT22(listFunctionMT22[1]))
    print("printListFunctionMT22 :" + Tool.printListFunctionMT22(listFunctionMT22))


    access = Access(listInListVarMT22, Type())
    print("access :" + Tool.printAccess(access))
