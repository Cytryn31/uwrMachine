from bottle import request, run, route
import Connection.GET as wtf
import classifier
import numpy as np
import Connection.POST as post
import pickle
import Connection.PUT as put

@route('/hello', method = 'GET')
def hello():
    return "Hello World!"

@route('/train', method = 'POST')
def train():
    classfier_name = request.forms.get('classfier_name')
    classfier_type = request.forms.get('classfier_type')
    classfier_params = request.forms.get('classfier_params')
    cross_validation_type = request.forms.get('cross_validation_type')
    learning_curve_params = request.forms.get('learning_curve_params')
    train_size = request.forms.get('train_size')
    clf = classifier.configure_classifier(classfier_type,classfier_params)
    cv = classifier.configure_cross_validation(cross_validation_type,classfier_params)
    features_train, labels_train = wtf.getArrays()

    clf, train_sizes, train_scores, test_scores = classifier.train(clf,
                        train_sizes = np.linspace(.1, 1.0,train_size),
                        cv = cv,
                        params = " ",
                        features = features_train,
                        labels = labels_train )
    data = classfier_to_send(classfier_name, clf, train_sizes, train_scores, test_scores)
    post.send("http://naos-software.com/dataprocessing/rest-api","/classifiers","",data)

    return data

def test():
    classfier_name = request.forms.get('classfier_name')
    classfier_dump = request.forms.get('classfier')
    features_train, labels_train = wtf.getArrays()
    clf = pickle.loads(classfier_dump)
    preditions, accuracy, recall, precision = classifier.test(clf = clf, features = features_train, labels = labels_train)



    return data1+data2

run(host='localhost', port=8080)
