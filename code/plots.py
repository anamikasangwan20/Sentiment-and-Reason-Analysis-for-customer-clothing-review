##Plots for Baseline 3 versions:

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
x = ('Baseline' , 'Baseline with\n normalization' , 'Baseline with\n normalization \nand smoothing')
x_pos = np.arange(len(x))
bar_width = 0.1
space = 0.03
opacity = 0.9

f1_sentiment = [0.2, 0.4, 0.6] 
f1_fit = [0.2, 0.4, 0.6]
f1_fabric = [0.2, 0.4, 0.6]
f1_color = [0.2, 0.4, 0.6]
f1_style =[0.2, 0.4, 0.6]
f1_cost = [0.2, 0.4, 0.6]

plt.bar(x_pos, f1_sentiment, bar_width, alpha = opacity, color = 'peru', label = 'sentiment')
plt.bar(x_pos + bar_width + space, f1_fit, bar_width, alpha = opacity, color = 'darkolivegreen', label = 'fit')
plt.bar(x_pos + 2*bar_width + 2*space, f1_fabric, bar_width, alpha = opacity, color = 'indianred', label = 'fabric')
plt.bar(x_pos + 3*bar_width + 3*space, f1_color, bar_width, alpha = opacity, color = 'dimgrey', label = 'color')
plt.bar(x_pos + 4*bar_width + 4*space, f1_style, bar_width,  alpha = opacity, color = 'rosybrown', label = 'style')
plt.bar(x_pos + 5*bar_width + 5*space, f1_cost, bar_width,  alpha = opacity, color = 'royalblue', label = 'cost')

plt.xticks(x_pos + 3*bar_width, x)
plt.ylabel('F1 scores')
plt.title('Classifier comparison')
plt.legend()

plt.tight_layout() 
plt.show()

##Plots for 3 Classifier approaches:
x1 = ('Baseline' , 'Logreg' , 'SVM')
x1_pos = np.arange(len(x1))
bar_width = 0.1
opacity = 0.9

f1_sentiment = [0.2, 0.4, 0.6] 
f1_fit = [0.2, 0.4, 0.6]
f1_fabric = [0.2, 0.4, 0.6]
f1_color = [0.2, 0.4, 0.6]
f1_style =[0.2, 0.4, 0.6]
f1_cost = [0.2, 0.4, 0.6]

plt.bar(x1_pos, f1_sentiment, bar_width, alpha = opacity, color = 'peru', label = 'sentiment')
plt.bar(x1_pos + bar_width + space, f1_fit, bar_width, alpha = opacity, color = 'darkolivegreen', label = 'fit')
plt.bar(x1_pos + 2*bar_width + 2*space, f1_fabric, bar_width, alpha = opacity, color = 'indianred', label = 'fabric')
plt.bar(x1_pos + 3*bar_width + 3*space, f1_color, bar_width, alpha = opacity, color = 'dimgrey', label = 'color')
plt.bar(x1_pos + 4*bar_width + 4*space, f1_style, bar_width,  alpha = opacity, color = 'rosybrown', label = 'style')
plt.bar(x1_pos + 5*bar_width + 5*space, f1_cost, bar_width,  alpha = opacity, color = 'royalblue', label = 'cost')


plt.xticks(x1_pos + 3*bar_width, x1)
plt.ylabel('F1 scores')
plt.title('Classifier comparison')
plt.legend()

plt.tight_layout() 
plt.show()
