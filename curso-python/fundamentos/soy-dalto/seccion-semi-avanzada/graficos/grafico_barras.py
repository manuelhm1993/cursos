from pathlib import Path

import pandas as pd             # Analizar datos
import matplotlib.pyplot as plt # Visualizar datos de forma gráfica
import seaborn as sns           # Gráficos estadísticos

DATA_PATH = Path(__file__).parent / "resources" / "cofla_ingresos.csv"

# Analizar y manipular los datos
df = pd.read_csv(DATA_PATH)

# Construir un gráfico de barras con las coordenadas y datos indicados
sns.barplot(x="Fuente", y="Ingresos", data=df)

total_ingresos = df["Ingresos"].sum()

print(f"El total de ingresos es: ${total_ingresos:,.2F}")

# Mostrar el gráfico
plt.show()