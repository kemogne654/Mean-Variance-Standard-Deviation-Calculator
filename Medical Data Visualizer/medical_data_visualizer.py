import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('medical_examination.csv')

# Add an overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)) > 25
df['overweight'] = df['overweight'].astype(int)

# Normalize data: 0 = good, 1 = bad
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})
df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})

def draw_cat_plot():
    
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
  
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    
    fig = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', 
                      kind='bar', height=4, aspect=0.7)
    plt.xlabel("Features")
    plt.ylabel("Counts")
    plt.title("Categorical Plot")
    return fig

def draw_heat_map():
    
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(10, 8))

    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=.5, cmap='coolwarm')
    plt.title('Correlation Matrix Heatmap')
    plt.show()

if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
