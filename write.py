stream = open('output.txt','wt')

print('\nCan i write to this file? \n' + str(stream.writable()))

stream.write('H')
stream.writelines(['ello',' ''world'])
stream.write('\n')
names = ['Nathaniel','Arthurjoe']
stream.writelines(names)