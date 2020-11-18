def damage(level,power,absAtk,absDef,modifier_dictionary=dict()):
	'''Assuming all are ints, and modifier_dictionary is a dict of {modifier_name}:{modifier_multiplier} key-value pairs.'''
	output = ((((2*level/5)+2)*power*absAtk/absDef)/50) + 2
	for modkey in modifier_dictionary.keys():
		modval = modifier_dictionary[modkey]
		output *= modval
	return output

