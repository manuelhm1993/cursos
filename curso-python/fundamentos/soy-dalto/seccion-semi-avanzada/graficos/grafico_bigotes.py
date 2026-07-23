from pathlib import Path

import pandas as pd             # Analizar datos
import matplotlib.pyplot as plt # Visualizar datos de forma gráfica
import seaborn as sns           # Gráficos estadísticos

DATA_PATH = Path(__file__).parent / "resources" / "bigotes.csv"

# Analizar y manipular los datos
df = pd.read_csv(DATA_PATH)

# Construir un gráfico de bigotes con las coordenadas y datos indicados
sns.boxplot(x="Categoria", y="Valor", data=df)

# Mostrar el gráfico
plt.show()