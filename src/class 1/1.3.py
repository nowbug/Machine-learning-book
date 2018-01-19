# /usr/bin
# coding:utf-8


from sklearn import preprocessing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 定义一个标记编码器 label encoder
label_encoder = preprocessing.LabelEncoder()
input_classes = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']
label_encoder.fit(input_classes)
print '\nClass mapping:'
# .classes_ 是一个方法用来显示数组的形状的
for i, item in enumerate(label_encoder.classes_):
    print item, '-->', i
# 可以把再来的词转换成数字
labels = ['toyota', 'ford', 'audi']
encoded_labels = label_encoder.transform(labels)
print '\nLabels=', labels
print 'Encoded labels=', list(encoded_labels)

# 通过数字翻转成单词
encoded_labels = [2, 1, 0, 3, 1]
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print '\nEncoded labels =', encoded_labels
print 'Decoded labels=', list(decoded_labels)
