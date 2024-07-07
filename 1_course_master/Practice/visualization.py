import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Данные для матрицы ошибок
confusion_matrix = np.array([
    [33, 0, 0],
    [0, 33, 0],
    [0, 1, 33]
])
cm_normalized = confusion_matrix.astype('float') / confusion_matrix.sum(axis=1)[:, np.newaxis]

# Метки классов
class_names = ['duck', 'pig', 'sheep']

# Визуализация матрицы ошибок
df_cm = pd.DataFrame(cm_normalized, index=class_names, columns=class_names)
plt.figure(figsize=(8, 6))
sns.heatmap(df_cm, annot=True, fmt='.2f', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
