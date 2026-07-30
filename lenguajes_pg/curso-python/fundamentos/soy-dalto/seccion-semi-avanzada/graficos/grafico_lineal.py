from pathlib import Path

import pandas as pd             # Analizar datos
import matplotlib.pyplot as plt # Visualizar datos de forma gráfica
import seaborn as sns           # Gráficos estadísticos

DATA_PATH = Path(__file__).parent / "resources" / "peos.csv"

# Analizar y manipular los datos
df = pd.read_csv(DATA_PATH)

# Construir un gráfico lineal con las coordenadas y datos indicados
sns.lineplot(x="Fecha", y="Peos", data=df)

# Obtener los datos del punto crítico
fecha, peos = df.loc[df['Peos'].idxmax()]

# Marcar el punto crítico
plt.plot(fecha, peos, "o")

# Mostrar el gráfico
plt.show()