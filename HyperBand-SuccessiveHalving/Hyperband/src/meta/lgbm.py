'''
Example of  wrapper for xgboost estimator
supports:
    *TODO: LGBMClassifier
    *TODO: LGBMRegressor
Issues: apparently cannot boost properly model.booster_
custom objective functions and weight not supported
'''
#
from .base import SHBaseEstimator
from .callback import  early_stop,EarlyStopException
#
from lightgbm import Dataset
import numpy as np
#
class SHLGBMEstimator(SHBaseEstimator):
    def __init__(self,model):
        raise NotImplementedError
        #have not been able to work around the booster,
        # maybe try functional api instead of sklearn
#         self.model = model
#         self.env = {'best_score':-np.infty,'best_iteration':-1,'earlier_stop':False}
#     def update(self,Xtrain,ytrain,Xval,yval,scoring,n_iterations):
#         dtrain = Dataset(data=Xtrain,label=ytrain)
#
#         early_stop_callback = early_stop()
#
#         if not(self.env['earlier_stop']):
#             for i in range(n_iterations-self.model.n_estimators):
#                 # note:
#                 # this is a get, but the internal booster in XGBClassifier is also updated
#                 # add unit test for controle if future updates
#
#                 #TODO: fix this part: self.model.booster_.update -> leaves error due to train_set
#                 self.model.booster_.update(train_set=dtrain) #TODO: need to support custom objective functions fobj
#                 self.model.n_estimators += 1
#
#                 score = scoring(self,Xval,yval)
#
#                 if score >  self.env['best_score']:
#                     self.env['best_score'] = score
#                     self.env['best_iteration'] = self.model.n_estimators
#                 try:
#                     early_stop_callback(env=self.env,
#                                         score=score,
#                                         iteration=self.model.n_estimators)
#                     #TODO: ??? add rollback????
#                 except EarlyStopException:
#                     print('Update Stopped Earlier! @ {} instead of {}'.format(self.model.n_estimators,n_iterations) )
#                     self.env['earlier_stop'] = True
#                     break