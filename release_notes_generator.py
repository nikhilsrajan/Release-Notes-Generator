from tags import *
from utility import return_empty_list_of_lists
from utility import get_n_digits

class release_notes_generator:
	def __init__(self):
		self.__version_major		= 0
		self.__version_minor		= 0
		self.__version_patch		= 0
		self.__version_iteration	= 0
		self.__version_tag 			= EMPTY
		self.__version_tag_count	= -1

		self.__date_dd 				= 4
		self.__date_mm 				= 2
		self.__date_yyyy 			= 1995

		self.__type_tag 			= EMPTY
		
		self.__text_container 		= return_empty_list_of_lists(5)

		self.__export_filename		= 'release_notes_generator_export'
		self.__export_extention		= 'txt'

		self.__compiled_notes		= ''

		self.__index = {
			EMPTY 		: -1,
			NEW_FEATURE : 0,
			CHANGE		: 1,
			KNOWN_ISSUE	: 2,
			BUG_FIX		: 3,
			NOTE		: 4
		}

		self.__title = {
			EMPTY 		: '',
			NEW_FEATURE : 'NEW FEATURES:',
			CHANGE		: 'CHANGES:',
			KNOWN_ISSUE	: 'KNOWN ISSUES:',
			BUG_FIX		: 'BUG FIXES:',
			NOTE		: 'NOTES:'
		}

		self.__version_type = {
			EMPTY		: '',
			DEV 		: 'dev'
		}

		self.__release_type = {
			EMPTY 				: '',
			INTERNAL_RELEASE 	: 'Internal Release.'
		}

	def Version(self, major, minor, patch, iteration, tag = EMPTY, tagcount = 0):
		self.__version_major		= major
		self.__version_minor		= minor
		self.__version_patch		= patch
		self.__version_iteration	= iteration
		self.__version_tag 			= tag
		self.__version_tag_count	= tagcount

	def Date(self, dd, mm, yyyy):
		self.__date_dd 				= dd
		self.__date_mm 				= mm
		self.__date_yyyy 			= yyyy

	def Type(self, tag):
		self.__type_tag = tag

	def Add(self, tag, hierarchy, text):
		self.__text_container[self.__index[tag]].append([hierarchy, text])

	def Compile(self):
		self.__compiled_notes = ''

		long_line 	= '---------------------------------------------------------'
		main_bullet = '*'
		sub_bullet 	= '-'
		tab 		= '\t'
		colon 		= ':'
		endl 		= '\n'
		dash 		= '-'
		underscore	= '_'
		dot			= '.'
		space 		= ' '
		
		tct 		= tab + colon + tab
		
		version 	= str(self.__version_major) + dot + \
					  str(self.__version_minor) + dot + \
					  str(self.__version_patch) + dot + \
					  str(self.__version_iteration) + underscore + \
					  self.__version_type[self.__version_tag] + \
					  ('' if self.__version_tag_count == -1 else str(self.__version_tag_count))
		
		date 		= get_n_digits(self.__date_dd, 2) + dash + get_n_digits(self.__date_mm, 2) + dash + get_n_digits(self.__date_yyyy, 2)

		self.__compiled_notes += long_line + endl + \
								 'Version' 	+ tct + version + endl + \
								 'Date' + tct + date + endl + \
								 'Type' + tct + self.__release_type[self.__type_tag] + endl + \
								 long_line + endl + \
								 endl

		inv_index_dict = dict([[v, k] for k, v in self.__index.items()])

		for index, section in enumerate(self.__text_container):
			self.__compiled_notes += tab + self.__title[inv_index_dict[index]] + endl
			
			for line in section:
				self.__compiled_notes += tab
				if line[0] == 1:
					self.__compiled_notes += main_bullet + space + line[1] + endl
				else:
					for i in range(line[0] - 1):
						self.__compiled_notes += space + space
					self.__compiled_notes += sub_bullet + space + line[1] + endl

			self.__compiled_notes += endl

		return self.__compiled_notes

	def SetFilename(self, filename, extention = 'txt'):
		newfilename = filename
		file_already_present = 1
		tried = 0

		while file_already_present == 1:
			try:
				test_open = open(newfilename + '.' + extention, 'r')
				tried += 1
				test_open.close()
			except:
				file_already_present = 0
				break

			if tried > 0:
				newfilename = filename + ' (' + str(tried) + ')'

		self.__export_filename = newfilename + '.' + extention

	def Export(self, filename, extention):
		self.SetFilename(filename)
		with open(self.__export_filename, 'w') as file:
			file.write(self.Compile())