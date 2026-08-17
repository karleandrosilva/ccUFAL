import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('StudentsPerformance.csv', usecols=['gender','race/ethnicity','math score','reading score','writing score'])

# distribuições de frequência
gender = dados['gender'].unique() # classes
frequencia_gender = dados['gender'].value_counts() # frequencia
percentual_gender = dados['gender'].value_counts(normalize = True)*100 # percentual

dist_freq_qualitativas_gender = pd.DataFrame({'Frequência': frequencia_gender, 'Porcentagem(%)': percentual_gender})
print(dist_freq_qualitativas_gender)

#print(dados.describe())

print("===============\n Math score\n===============")
msmin = dados['math score'].min()
msmax = dados['math score'].max()
print("min.: {}".format(msmin))
print("mean: {}".format(dados['math score'].mean()))
print("median: {}".format(dados['math score'].median()))
print("mode: {}".format(dados['math score'].mode(dropna=False).to_string()))
print("amplitude: {}".format(msmax-msmin))
print("variance: {:.3f}".format((dados['math score'].var())))
print("standard deviation: {:.3f}".format((dados['math score'].std())))
print("max: {}".format(msmax))
print("Q1: {}".format((dados['math score'].quantile(q=0.25))))
print("Q2: {}".format((dados['math score'].quantile(q=0.5))))
print("Q3: {}".format((dados['math score'].quantile(q=0.75))))

print("===============\n Reading score\n===============")
msmin = dados['reading score'].min()
msmax = dados['reading score'].max()
print("min.: {}".format(msmin))
print("mean: {}".format(dados['reading score'].mean()))
print("median: {}".format(dados['reading score'].median()))
print("mode: {}".format(dados['reading score'].mode(dropna=False).to_string()))
print("amplitude: {}".format(msmax-msmin))
print("variance: {:.3f}".format((dados['reading score'].var())))
print("standard deviation: {:.3f}".format((dados['reading score'].std())))
print("max: {}".format(msmax))
print("Q1: {}".format((dados['reading score'].quantile(q=0.25))))
print("Q2: {}".format((dados['reading score'].quantile(q=0.5))))
print("Q3: {}".format((dados['reading score'].quantile(q=0.75))))

print("===============\n Writing score\n===============")
msmin = dados['writing score'].min()
msmax = dados['writing score'].max()
print("min.: {}".format(msmin))
print("mean: {}".format(dados['writing score'].mean()))
print("median: {}".format(dados['writing score'].median()))
print("mode: {}".format(dados['writing score'].mode(dropna=False).to_string()))
print("amplitude: {}".format(msmax-msmin))
print("variance: {:.3f}".format((dados['writing score'].var())))
print("standard deviation: {:.3f}".format((dados['writing score'].std())))
print("max: {}".format(msmax))
print("Q1: {}".format((dados['writing score'].quantile(q=0.25))))
print("Q2: {}".format((dados['writing score'].quantile(q=0.5))))
print("Q3: {}".format((dados['writing score'].quantile(q=0.75))))

print("===============\n Math score - média por Genero \n===============")
print(dados.groupby('gender')['math score'].mean().to_string())

print("===============\n Reading score - média por Genero \n===============")
print(dados.groupby('gender')['reading score'].mean().to_string())

print("===============\n Writing score - média por Genero \n===============")
print(dados.groupby('gender')['writing score'].mean().to_string())

colors=['blue', 'green', 'orange']
names=['math', 'reading', 'writing']

x1 = list(dados['math score'])
x2 = list(dados['reading score'])
x3 = list(dados['writing score'])

plt.hist([x1,x2,x3], color=colors,label=names)
plt.legend()
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Math, Reading and Writing score')
plt.show()

'''
print("Math score by Gender")
math_scores_mean = pd.crosstab(dados['gender'], dados['race/ethnicity'], aggfunc = 'mean', values = dados['math score'])
print(math_scores_mean)

race = sorted(dados['race/ethnicity'].unique()) # classes
frequencia_race = dados['race/ethnicity'].value_counts() # frequencia
percentual__race = dados['race/ethnicity'].value_counts(normalize = True)*100 # percentual

dist_freq_qualitativas_race = pd.DataFrame({'Frequência': frequencia_race, 'Porcentagem(%)': percentual__race})
print(dist_freq_qualitativas_race)
'''