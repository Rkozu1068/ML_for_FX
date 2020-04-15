u"""
    決定木系モデルを視覚化する。
    Graphviz を用いて、決定木のモデルを視覚化する。
    決定木だけでなく、ランダムフォレストなど木構造のモデルに適用できる。

"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# モデルの木構造の視覚化に必要なパッケージ
from sklearn import tree
import pydotplus as pdp

import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(df.head(5))
print(iris.target)
print(iris.target_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print(df.head(5))

# 学習データとテストデータを分ける

features = df.columns[:4]
label = df["species"]
print(features)
print(label)
print(df[features].head(5))
df_train, df_test, label_train, label_test = train_test_split(df[features], label)

clf = RandomForestClassifier(n_estimators=150)
clf.fit(df_train, label_train)
print("========================================================")
print("予測の精度")
print(clf.score(df_test, label_test))

# 試しに木の一つを視覚化する
estimators = clf.estimators_
file_name = "./tree_visualization.png"
dot_data = tree.export_graphviz(estimators[0], # 決定木オブジェクトを一つ指定する
                                out_file=None, # ファイルは介さずにGraphvizにdot言語データを渡すのでNone
                                filled=True, # Trueにすると、分岐の際にどちらのノードに多く分類されたのか色で示してくれる
                                rounded=True, # Trueにすると、ノードの角を丸く描画する。
                                feature_names=features, # これを指定しないとチャート上で特徴量の名前が表示されない
                                class_names=iris.target_names, # これを指定しないとチャート上で分類名が表示されない
                                special_characters=True # 特殊文字を扱えるようにする
                                )
graph = pdp.graph_from_dot_data(dot_data)
graph.write_png(file_name)
