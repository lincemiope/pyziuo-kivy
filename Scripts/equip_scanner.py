Props = ['Defense Chance Increase', 'Mana Regeneration', 'Stamina Regeneration',
         'Energy Resist', 'Poison Resist', 'Cold Resist', 'Fire Resist',
         'Physical Resist', 'Mana Increase', 'Lower Reagent Cost',
         'Lower Mana Cost', 'Spell Damage Increase', 'Intelligence Bonus',
         'Dexterity Bonus', 'Strength Bonus', 'Faster Casting', 'Faster Cast Recovery',
         'Hit Point Increase', 'Stamina Increse', 'Hit Point Regeneration',
         'Hit Chance Increase']
CloseGumps()
LTargetID(0)
TargCurs(True)
while LTargetID() == 0:
    EUOWait(10)
WaitForContext(LTargetID(), 1, 3000)
WaitForGump(58924, 3000) #Paperdoll
items = FindItem(-1, True, ContID())
totalvalue = {}
for itm in items:
    props = WaitForProps(itm.ID, 3000)
    for prop in props:
        val = 0
        try:
            val = int(prop.Value)
        except ValueError:
            val = 0
        if prop.Name in totalvalue:
            totalvalue[prop.Name] += val
        else:
            totalvalue[prop.Name] = val
print('======== Equip Scanner ========')
for k,v in totalvalue.items():
    if not k.lower() in list(i.lower() for i in Props):
        continue
    if v != 0:
        print('{0}: {1}'.format(k,v))
    else:
        print(k)
print('===============================')
