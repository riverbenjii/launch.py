name = "Mr_Taylor"
title = "Teacher"
has_magic = True
wears_armour = False
uses_weapon = False
old = False

name2 = "Mr_Martinez"
title2 = "Teacher"
has_magic2 = False
wears_armour2 = False
uses_weapon2 = False
old2 = True

name3 = "Coach_Ramsey"
title3 = "Teacher/Coach"
has_magic3 = True
wears_armour3 = True
uses_weapon3 = True
old3 = False

name4 = "Mr_Brashears"
title4 = "Teacher/Coach"
has_magic4 = False
wears_armour4 = False
uses_weapon4 = True
old4 = False


# mr. taylor!

if has_magic and uses_weapon:
    print(name + " is a Battlemage")

elif has_magic or wears_armour:
    print(name + " is a Wizard")

elif uses_weapon:
    print(name + " is a Warrior")

else:
    print(name + " is boring.")


# mr. martinez

if has_magic2 and uses_weapon2:
    print(name2 + " is a Battlemage")

elif has_magic2 or wears_armour2:
    print(name2 + " is a Wizard")

elif uses_weapon2:
    print(name2 + " is a Warrior")

else:
    print(name2 + " is boring.")


# coach ramsey

if has_magic3 and uses_weapon3:
    print(name3 + " is a Battlemage")

elif has_magic3 or wears_armour3:
    print(name3 + " is a Wizard")

elif uses_weapon3:
    print(name3 + " is a Warrior")

else:
    print(name3 + " is boring.")


# mr. brah!

if has_magic4 and uses_weapon4:
    print(name4 + " is a Battlemage")

elif has_magic4 or wears_armour4:
    print(name4 + " is a Wizard")

elif uses_weapon4:
    print(name4 + " is a Warrior")

else:
    print(name4 + " is boring.")