from time import time

start = time()
end = time()
sleep(10)

print('Inserted another batch ... %.3f second' % (end - start)) 
print('Inserted another batch ... {:.3f} second'.format(end - start)) 

