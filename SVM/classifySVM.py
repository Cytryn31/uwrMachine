from sklearn import  svm

def train(classifier, features_train, labels_train):
    classifier.fit(features_train,labels_train)
    return classifier

def getLinearSupportVectorClassifier(penalty = 'l2',
                                     loss = 'squared_hinge',
                                     dual = True,
                                     tol = 0.0001,
                                     C = 1.0,
                                     multi_class = 'ovr',
                                     fit_intercept = True,
                                     intercept_scaling = 1,
                                     class_weight = None,
                                     verbose = 0,
                                     random_state = None,
                                     max_iter = 1000):

    classifier = svm.LinearSVC(penalty,
                            loss,
                            dual,
                            tol,
                            C,
                            multi_class,
                            fit_intercept,
                            intercept_scaling,
                            class_weight,
                            verbose,
                            random_state,
                            max_iter)

    return classifier

def getSupportVectorClassifier(C=1.0,
                               kernel='rbf',
                               degree=3,
                               gamma=0.0,
                               coef0=0.0,
                               shrinking=True,
                               probability=False,
                               tol=0.001,
                               cache_size=200,
                               class_weight=None,
                               verbose=False,
                               max_iter=-1,
                               random_state=None):

    classifier = svm.SVC(C,
                        kernel,
                        degree,
                        gamma,
                        coef0,
                        shrinking,
                        probability,
                        tol,
                        cache_size,
                        class_weight,
                        verbose,
                        max_iter,
                        random_state)

    return classifier

