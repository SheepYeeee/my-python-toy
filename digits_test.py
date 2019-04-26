import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()#載入數字資料集

images_and_labels = list(zip(digits['images'], digits['images']))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# images_and_labels=list(zip(digits['images'],digits['target']))
# for index,(image,label) in enumerate(images_and_labels[:4]):
#     plt.subplot(2, 4, index+1)
#     plt.axis('off')
#     plt.imshow(image,cmap='gray_r',interpolation='nearest')
#     plt.title('Training: %i' % label)

n_samples=len(digits['images'])
data=digits['images'].reshape((n_samples,-1))

classifier=svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples // 2],digits.target[:n_samples // 2])
expected=digits.target[n_samples // 2:]
predicted=classifier.predict(data[n_samples // 2:])