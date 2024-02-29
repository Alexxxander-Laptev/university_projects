def best_feature_to_split(X, y):
    ''' Выводит прирост информации при разбиении по каждому признаку'''
    number_features = X.shape[1]
    best_IG = -1
    best_feature = None

    for i in range(number_features):
        values = X[:, i]
        unique_values = np.unique(values)

        for j in unique_values:
            left_balls_ind = np.where(values <= j)[0]
            right_balls_ind = np.where(values > j)[0]

            IG = information_gain(
                y, y[left_balls_ind], y[right_balls_ind])

            if IG > best_IG:
                best_IG = IG
                best_feature = (i, j)

    return best_feature, best_IG


def build_decision_tree(X, y, depth=0, max_depth=None):
    if len(np.unique(y)) == 1 or (max_depth is not None and depth == max_depth):
        return {'class': y[0]}

    best_feature, best_IG = best_feature_to_split(X, y)

    if best_feature is None:
        return {'class': np.bincount(y).argmax()}

    feature_index, threshold = best_feature
    left_indices = np.where(X[:, feature_index] <= threshold)[0]
    right_indices = np.where(X[:, feature_index] > threshold)[0]

    left_subtree = build_decision_tree(
        X[left_indices], y[left_indices], depth + 1, max_depth)
    right_subtree = build_decision_tree(
        X[right_indices], y[right_indices], depth + 1, max_depth)

    return {'feature_index': feature_index, 'threshold': threshold,
            'left': left_subtree, 'right': right_subtree}


X = np.array(balls).reshape(-1, 1)
X_left = np.array(balls_left).reshape(-1, 1)
X_right = np.array(balls_right).reshape(-1, 1)
y = np.array([1] * 9 + [0] * 11)

# Построение дерева
decision_tree = build_decision_tree(X, y)

dot_data = StringIO()
export_graphviz(decision_tree, feature_names=[
                'yellow', 'blue'], out_file=dot_data, filled=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(value=graph.create_png())