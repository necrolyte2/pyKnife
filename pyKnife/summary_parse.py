import pyKnife

knife = pyKnife.pyKnife()

output = knife.command( ['node', 'show', 'chef'], 'summary' ).replace( ' ', '' ).splitlines( )
print output

temp = {}
for kp in output:
    t = kp.split( ':', 1 )
    temp[t[0]] = t[1]

json = {}
for k,v in temp.items():
    if k[:7] == 'Recipes':
        temp = k[7:] + ':' + v
        json['Recipes'] = temp.split( ',' )
    elif ',' in v:
        json[k] = v.split( ',' )
    else:
        json[k] = v

        
        
#{'Recipesrcg,nagios': ':client', 'NodeName': 'chef', 'Roles': 'rcg_server,nagios_client', 'IP': '153.90.178.154', 'RunList': 'role[rcg_server],role[nagios_client]', 'FQDN': 'chef.cns.montana.edu', 'Environment': 'Production'}


print json
