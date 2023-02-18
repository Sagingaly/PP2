import json

file =open("TSIS4/date.json", "r")

js = json.load(file)
print("Interface Status\n================================================================================")

template = "{:<50} {:<20} {:<8} {:<8}"

print(template.format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for i in js['imdata']:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print(template.format(dn, descr, speed, mtu))



