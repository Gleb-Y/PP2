import json

f = open("Lab_4\sample-data.json", 'r')
json_data = json.loads(f.read())

print('Interface Status' '\n' '================================================================================' '\n' 'DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')

for i in range(len(json_data['imdata'])):
    x = json_data['imdata'][i]['l1PhysIf']['attributes']
    #if elif нужны чтобы корректировать расстояние в пробелах (:
    if len(json_data['imdata'][i]['l1PhysIf']['attributes']['dn']) == len('topology/pod-1/node-201/sys/phys-[eth1/33]'):
        print(x['dn'], '                            ', x['speed'], ' ', x['mtu'])

    elif len(json_data['imdata'][i]['l1PhysIf']['attributes']['dn']) < len('topology/pod-1/node-201/sys/phys-[eth1/33]'):
        f = abs(len('topology/pod-1/node-201/sys/phys-[eth1/33]') - len(json_data['imdata'][i]['l1PhysIf']['attributes']['dn']))
        plus_space = '                            ' + ' '*f
        print(x['dn'], plus_space, x['speed'], ' ', x['mtu'])

    elif len(json_data['imdata'][i]['l1PhysIf']['attributes']['dn']) > len('topology/pod-1/node-201/sys/phys-[eth1/33]'):
        f = abs(len('topology/pod-1/node-201/sys/phys-[eth1/33]') - len(json_data['imdata'][i]['l1PhysIf']['attributes']['dn']))
        minus_space = '                            ' - ' '*f
        print(x['dn'], minus_space, x['speed'], ' ', x['mtu'])




"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
"""