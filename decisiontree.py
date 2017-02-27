from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,40], [179,65,37], [160,60,38], [191,84,47], [176,65,39], [156,45,35], [191,94,49],[189,102,53], [184,81,43], [183,82,42]]

Y = ['male', 'female', 'female', 'male', 'female', 'female', 'male', 'male', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

# Predict the gender by giving some values
prediction = clf.predict([189,76,44])

print prediction