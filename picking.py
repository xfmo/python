import cPickle as p
shoplistfile='/home/shoplist.data'
shoplist=['apple','carrot']
f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist #remove shoplist
f=file(shoplistfile,'r')
kk=p.load(f)
print kk
