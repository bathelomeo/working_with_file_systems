stream = open('manage.txt','wt')

stream.write('demo!')

stream.seek(0)

stream.write('cool')

stream.flush()

stream.close()
