def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    match obj_type.__name__:
        case 'NoneType' if object is None:
            print(f"Nothing: {object} {obj_type}")
            return 0
        case 'float' if object != object:
            print(f"Cheese: {object} {obj_type}")
            return 0
        case 'int' if object == 0:
            print(f"Zero: {object} {obj_type}")
            return 0
        case 'str' if object == "":
            print(f"Empty: {object} {obj_type}")
            return 0
        case 'bool' if object is False:
            print(f"Fake: {object} {obj_type}")
            return 0
        case _:
            print(f"Type not Found")
            return 1
