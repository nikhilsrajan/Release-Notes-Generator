from tags import *
from release_notes_generator import release_notes_generator

generator = release_notes_generator()

def Version(major, minor, patch, iteration, tag = EMPTY, tagcount = -1):
	generator.Version(major, minor, patch, iteration, tag, tagcount)

def Date(dd, mm, yyyy):
	generator.Date(dd, mm, yyyy)

def Type(tag):
	generator.Type(tag)

def Add(tag, hierarchy, text):
	generator.Add(tag, hierarchy, text)

def Compile():
	return generator.Compile()

def Export(filename = 'release_notes_generator_export', extention = 'txt'):
	generator.Export(filename, extention)
