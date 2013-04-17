try:
    import numpy
    print 'Trying numpy'
except ImportError:
    print "numpy is not installed"

try:
    import matplotlib
    print 'Trying matplotlib'
except ImportError:
    print "matplotlib is not installed"

try:
	from matplotlib.mlab import PCA
	print 'Trying matplotlib.mlab'
except ImportError:
	print 'matplotlib.mlab is not installed'