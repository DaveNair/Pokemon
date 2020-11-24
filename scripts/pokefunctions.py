## Author: Dave Nair
## this is a file for generic FUNCTIONS that are commonly run in Pokemon. 
## the idea is to have this be a module for other files to import
import numpy as np

def damage(power,attac,absDef,modifier_dictionary=dict(),level=50):
	'''Assuming all are ints, and modifier_dictionary is a dict of {modifier_name}:{modifier_multiplier} key-value pairs.'''
	output = ((((2*level/5)+2)*power*absAtk/absDef)/50) + 2
	for modkey in modifier_dictionary.keys():
		modval = modifier_dictionary[modkey]
		output *= modval
	return output

def stage_multiplier(stage_value):
	if stage_value[-3:].isalpha():
		stage_value = stage_value[:-3]
	stage_value = int(stage_value)
	lower,upper = [0,0]
	if stage_value>0:
		upper += stage_value
	elif stage_value<0:
		lower -= stage_value
	return float((2+upper)/(2+lower))

def stat_value(base,iv,ev,nature,lv=50,hp=False):
	if hp==True:
		return np.floor((((2*base) + iv + np.floor(ev/4))*lv)/100) + lv + 10
	else:
		np.floor((np.floor((((2*base) + iv + np.floor(ev/4))*lv)/100)+5) * nature)
	return False

def current_spread(base_stats:dict,IVs=dict(),EVs=dict(),natures=dict(),level=50):
	currstats = dict()
	for statkey in list(base_stats.keys()):
		baseval = base_stats[statkey]
		ivval = IVs.get(statkey, default=31)
		evval = EVs.get(statkey, default=0)
		natureval = natures.get(statkey, default=1)
		hpbool = statkey=='hp'
		statval = stat_value(baseval, iv=ivval, ev=evval, nature=natureval, lv=level, hp=hpbool)
		currstats[statkey] = statval
	return currstats
