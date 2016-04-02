try:
	import json
except Exception, e:
	raise e

def get_config(path):
	with open(path) as f:
		content = f.read()
		return json.loads(content)

def get_config_str(path):
	data = get_config(path)
	return data['prototype']+"://"+data['username']+":"+data['password']+"@"+data['host']+"/"+data['database']+"?charset="+data['encoding']

if __name__ == '__main__':
	print get_config_str('database.cfg')		
