import pydicom
import pylab

ds = pydicom.read_file("F:\\study\\Group T\\Master\\Thesis\\wetransfer-886411\\test 07 AEP\\test 07 AEP0000.dcm")
##
pixel_bytes = ds.PixelData

##CT值组成了一个矩阵
pix = ds.pixel_array

##读取显示图片
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.show()
