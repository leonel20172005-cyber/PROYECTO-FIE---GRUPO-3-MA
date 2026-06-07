import numpy as np
import plotly.graph_objects as go
from calculo_lagrange import horas, velocidades, lagrange

def generar_grafica():
    # 1. Generar 200 puntos continuos para la curva suave
    horas_continuas = np.linspace(8.0, 16.0, 200)
    velocidades_curva = [lagrange(horas, velocidades, x) for x in horas_continuas]

    # 2. Configurar la figura interactiva
    fig = go.Figure()

    # Curva predictiva (Línea)
    fig.add_trace(go.Scatter(
        x=horas_continuas, 
        y=velocidades_curva, 
        mode='lines', 
        name='Curva Predictiva (Lagrange)',
        line=dict(color='#2E86C1', width=3)
    ))

    # Nodos de medición reales (Puntos)
    fig.add_trace(go.Scatter(
        x=horas, 
        y=velocidades, 
        mode='markers', 
        name='Mediciones Reales',
        marker=dict(color='#E74C3C', size=12, symbol='circle', line=dict(color='black', width=1))
    ))

    # 3. Diseño y presentación
    fig.update_layout(
        title='<b>Predicción de Ancho de Banda en la FIE</b><br>Modelo de Interpolación de Lagrange',
        xaxis_title='<b>Hora del Día (Formato 24h)</b>',
        yaxis_title='<b>Ancho de Banda (Mbps)</b>',
        hovermode='x unified',
        template='plotly_white',
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )

    return fig

if __name__ == "__main__":
    figura_final = generar_grafica()
    figura_final.show()
