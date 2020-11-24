## this file is for common methods that are not necessarily Pokemon related
## for now, i'll just call this common or convenience functions.
## they might be added TO dnio later, if they're useful enough
# import pokefunctions as pkf

def make_nicknames_dictionary(input_names, nickname_as_key=True, verbose=False):
	'''
	This makes nicknames that are absolute and WILL refer to one specific name. This is not a FCFS system for nicknames.
		i.e.,
		CORRECT: ["Abra","Absol"] -> ["abr","abs"]
		INCORRECT: ["Abra","Absol"] -> ["a","ab"]
	'''
	names = sorted(list(set([name.strip().title() for name in input_names])))
	## you know - let's just do the most brute-force thing. 
	## this should work fine if there are a small (<1000) number of names
	nicknames = []
	for this_name in names:
		outstring = this_name + " -> "
		other_names = [name for name in names if name!=this_name]
		name_length = len(this_name)
		attempt_length = 1
		current_nickname_attempt = ''
		## while our attempt is still SHORTER than the original, just in case we get a runaway number for some reason...
		## and (mainly) while our attempt is still not useable (i.e., it starts a different name),
		while (attempt_length<=name_length) and any([oname.startswith(current_nickname_attempt) for oname in other_names]):
			## we need to keep finding new attempts
			current_nickname_attempt = this_name[:attempt_length]
			attempt_length += 1
		## after all that, we SHOULD be left with the proper nickname
		settled_nickname = current_nickname_attempt.lower()
		nicknames.append(settled_nickname)
		outstring += settled_nickname
		if verbose:
			print(outstring)


	## now we have all the names & nicknames. time to make the dict, depending on what we want as the key
	if nickname_as_key==False:
		keys,vals = [names, nicknames]
	else:
		keys,vals = [nicknames,names]
	N_names = len(names)
	return {keys[i]:vals[i] for i in range(N_names)}

def read_pokepaste(string):
	return False

def assess(user_situation:str):
	"""
	user_situation will look something like this:
		glas, icicle, +6Atk - garch
	"""
	DEFAULT_DICT = {'multipliers':[1], 'stages':[], 'pokemon':'', 'move':''}
	offender_info, defender_info = [[info.strip() for info in side.split(',')] for side in user_situation.split('-')]
	offender = DEFAULT_DICT
	defender = DEFAULT_DICT
	for pk_info in [offender_info,defender_info]:
		N_info = len(pk_info)
		for i in range(N_info):
			this_info = pk_info[i]
			if i==0:
				# pk_info['pokemon'] = pkf.lookup_name(this_info)
				pk_info['pokemon'] = this_info
			elif this_info[0]=='+':
				pk_info['stages'].append(this_info)
			elif this_info[0]=='*':
				pk_info['multipliers'].append(float(this_info[1:]))
			else:
				# pk_info['move'] = pkf.lookup_move(this_info)
				pk_info['move'] = this_info




