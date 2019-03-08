# --*-- coding: utf-8 --*--
import os
import shutil

# Name of the problem copied from LeetCode webpage
problem = ' 111. Minimum Depth of Binary Tree  '

'''
create a new directory
'''
def mkdir(path):
	isExists = os.path.exists(path)

	if not isExists:
		os.makedirs(path)

	codefile = os.path.join(path, path+'.py')
	if not os.path.exists(codefile):
		f = open(codefile, 'w')
		f.close()

'''
analyse the string, extract some information in it.
'''
def handleStr(s):
	baseurl = 'https://leetcode.com/problems/'
	seg = s.strip().split()
	problemID = int(seg[0][:-1])
	problemName = ' '.join(seg[1:])

	problemUrl = '-'.join(seg[1:]).lower()
	problemUrl = baseurl + problemUrl

	return problemID, problemName, problemUrl

def main():
	ID, Name, Url = handleStr(problem)

	'''
	create the directory and the corresponding code file
	'''
	mkdir(str(ID))
	
	'''
	modify README.md
	'''
	firstLarger = -1

	with open('README.md', 'r', encoding='utf-8') as f:
		lines = f.readlines()
	for i, line in enumerate(lines):
		if line.startswith('|'):
			seg = line.strip().split('|')
			number = seg[1].strip()
			if number.isdigit():
				if int(number) == ID:
					exit()
				if int(number) > ID:
					firstLarger = i
					break
	thisProblem = '| {}  | [{}]({}) |'.format(str(ID), Name, Url)
	with open('README.md', 'w', encoding='utf-8') as f:
		for line in lines[:firstLarger]:
			f.write(line.strip() + '\n')
		f.write(thisProblem.strip() + '\n')
		for line in lines[firstLarger:]:
			f.write(line.strip() + '\n')

	'''
	open the file, then I modify it.
	'''
	os.system('open {}'.format(str(ID)))
	os.system('open {}/{}'.format(str(ID), str(ID)+'.py'))
	os.system('open README.md')


if __name__ == '__main__':
	main()