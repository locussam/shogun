#!/usr/bin/env python
from tools.load import LoadMatrix
lm=LoadMatrix()

traindat = lm.load_numbers('../data/fm_train_real.dat')
testdat = lm.load_numbers('../data/fm_test_real.dat')

parameter_list = [[traindat,testdat,1.5,10],[traindat,testdat,1.5,10]]

def preprocessor_prunevarsubmean (fm_train_real=traindat,fm_test_real=testdat,width=1.4,size_cache=10):
	from shogun import Chi2Kernel
	from shogun import RealFeatures
	from shogun import PruneVarSubMean

	feats_train=RealFeatures(fm_train_real)
	feats_test=RealFeatures(fm_test_real)

	preproc=PruneVarSubMean()
	preproc.fit(feats_train)
	feats_train = preproc.transform(feats_train)
	feats_test = preproc.transform(feats_test)

	kernel=Chi2Kernel(feats_train, feats_train, width, size_cache)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

	return km_train,km_test,kernel

if __name__=='__main__':
	print('PruneVarSubMean')
	preprocessor_prunevarsubmean(*parameter_list[0])
