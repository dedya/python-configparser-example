import configparser

config=configparser.ConfigParser()
folderPath = "<path-to-your-config-file>"

config.read(folderPath+'/config.ini')

mysqlHost = config['mysql']['host']
mysqlUser = config['mysql']['user']
mysqlPassword = config['mysql']['password']
postgreHost = config['postgresql']['host']
postgreUser = config['postgresql']['user']
postgrePassword = config['postgresql']['password']

print(mysqlhost)
print(postgrehost)
