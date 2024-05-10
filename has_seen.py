# Ett global set för att lagra observerade objekt allt utanför 4-11 2an hittar 14-18, set som är lagd utanför has seen funktionen.
#Det gör att den kontrollerar allt och inte bara funktionen. Då den ger True/False
seen_objects = set()

def has_seen(obj: int | str) -> bool:
    global seen_objects

    if obj in seen_objects:
        return True
    else:
        seen_objects.add(obj)
        return False

# Testfall
print(has_seen(999))  # False. Varför det blir false är för att värdet inte har identifierats än.
print(has_seen("39"))  # False. Varför det blir false är för att värdet inte har identifierats än.
print(has_seen(999))  # True. Blir true pågrund utav att den har identifierats ovan.
print(has_seen(2))  # False. Varför det blir false är för att värdet inte har identifierats än.
print(has_seen("39"))  # True. Blir true pågrund utav att den har identifierats ovan.