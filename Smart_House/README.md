# Smart House

### Ambicion

La aspiracion del proyecto, es tanto concientizar a los individuos del excesivo/mal consumo electrico asi como lograr tener una casa inteligente. Pero es de hecho, que es posible tener una casa inteligente, si fueramos concientes de su consumo y lo que representa.

En un mundo donde la eficiencia energética se vuelve cada vez más crucial, una casa inteligente es la cúspide de la eficiencia, control y ahorro.

La energía no se desperdiciaria, cada vatio se utilizará de forma eficiente. Las luces se ajustarán automáticamente a la luz natural, los electrodomésticos funcionarán solo cuando se necesiten y la temperatura se mantendrá estable sin esfuerzo. Esto es una meta a lograr y puede parecer larga pero es algo que puede hacerse realidad gracias a la inteligencia artificial y al análisis de datos.

En el corazón de esta casa inteligente se encuentra un dataset que guarda los secretos del consumo de energía. Este conjunto de datos es un gran tesoro para el análisis energético.

El enigma a descifrar es el consumo energético y la manera de optimizar la electricidad. Al analizar los datos, podremos tomar decisiones más acertadas para optimizar el consumo de energía.

Esta gran creación no solo nos permite ahorrar dinero en la factura de la luz, sino que también contribuye a proteger el medio ambiente. Al reducir nuestro consumo de energía, reducimos las emisiones de CO2 y combatimos el cambio climático.



### Sumario

Se analizará un dataset extraído de la base de datos de UCI Machine Learning Repository.

Contiene alrededor de 4 años de datos de consumo de electricidad para un hogar ubicado en Francia, recopilados entre diciembre de 2006 y noviembre de 2010(47 meses). Los datos incluyen información sobre potencia activa global, potencia reactiva global, voltaje, intensidad global, submedición 1 (cocina), submedición 2. (lavadero), y submedición 3 (calentador de agua eléctrico y aire acondicionado). Con 2.075.259 mediciones en total y algunos valores faltantes en las mediciones (casi el 1,25% de las filas).
La información fue extraída de una casa localizada en Sceaux, Paris.

Con este dataset podemos comprender un poco mejor acerca de cómo funciona la electricidad en un hogar e intentar predecir cuáles serán los consumos de electricidad futura basándonos en datos pasados. 
Con las previsiones de demanda futura, la producción y distribución de energía se pueden optimizar para satisfacer las necesidades de la creciente población. Las aplicaciones de modelos de aprendizaje profundo al problema de pronóstico de carga eléctrica están ganando interés entre los investigadores y la industria. Sin embargo, pronosticar la demanda de los hogares individuales es una tarea desafiante debido a la diversidad de patrones de consumo de energía.
La fluctuación del consumo de energía eléctrica depende principalmente del número de aparatos eléctricos domésticos y del comportamiento de los residentes. El consumo eléctrico de los hogares se deriva de la ocupación del hogar.

El dataset:
El conjunto de datos contiene información vital sobre el consumo energético de la casa, incluyendo:

- Energía activa: La protagonista de nuestro análisis, representa la energía realmente consumida por la casa en kW.
- Energía reactiva: La energía invisible que no se convierte en trabajo útil, pero que genera pérdidas en el sistema en kW.
- Voltaje: La fuerza que impulsa la corriente eléctrica en Voltios.
- Intensidad de corriente: La cantidad de flujo de electrones por unidad de tiempo en amperios.
- Submedicion 1: Corresponde al gasto en Vatios/h de la cocina(lavavajillas, horno y microondas (los fogones no son eléctricos sino de gas)).
- Submedicion 2: Corresponde al gasto en Vatios/h de lavadero, que contiene lavadora, secadora, frigorífico y luz.
- Submedicion 3: Corresponde al gasto en Vatios/h de un termo electrico y un aire acondicionado.
- Fecha: corresponde a la fecha en formato dd/mm/aaaa
- Hora: corresponde a la hora en formato hh/mm/ss

Para enriquecer el conjunto de datos, se deben asumir las siguientes condiciones dentro del marco teórico de circuitos alternos:

- Régimen estacionario: Se asume que todas las variables (voltaje, corriente, etc.) son senoidales y de frecuencia constante. Las magnitudes y los ángulos de fase de las variables no varían con el tiempo.
- Sistema monofásico: El conjunto de datos se refiere a un solo circuito con una sola fase. Las tensiones y corrientes consideradas son valores eficaces (RMS).
- Conexión en serie: La carga se encuentra conectada en serie con la fuente de voltaje.
- Forma de onda conocida: Se debe conocer la forma de onda de las señales de voltaje y corriente (generalmente sinusoidal).
- Ausencia de armónicos: Se considera que las señales no tienen distorsión armónica significativa.
- Valores medidos correctamente: Los valores de energía global activa, reactiva, intensidad y voltaje deben ser medidos con precisión.

Con estas condiciones establecidas, se haran los calculos de:
- Potencia aparente: cantidad total de potencia o energia que consume un circuito eléctrico.
- Factor de potencia: Un indicador de la eficiencia con la que se utiliza la energía.
- Impedancia: La oposición al flujo de la corriente eléctrica.
- Ángulo de fase(φ): Es el ángulo entre la corriente y el voltaje en un circuito de corriente alterna. El coseno de este ángulo es igual al factor de potencia.

Podemos decir entonces que: 

La energía activa total (p) y la energía reactiva total (q) contribuyen a la potencia aparente (s). La potencia aparente (s) está relacionada con el voltaje (v) y la corriente (i) a través de la impedancia (z).
El factor de potencia (pf) indica la eficiencia del sistema y está relacionado con el ángulo de fase (φ), que representa la relación temporal entre voltaje y corriente en sistemas de corriente alterna.

Al fin y al cabo los objetivos que pretende lograr el ser humano atraves de la casa inteligente:
- Predecir su consumo: Saber de antemano cuanto sera el gasto de energia para poder prevenir situaciones no deseadas.
- Ajustar su consumo: Adaptar el uso de electrodomésticos a los momentos de menor demanda o mayor producción de energía renovable.
- Optimizar su tarifa eléctrica: Seleccionar la tarifa que mejor se adapte a sus nuevos hábitos de consumo.
- Reducir su huella de carbono: Disminuir el impacto ambiental de su hogar.

### Conclusion

La energia activa es la que realmente se consume y se traduce en el costo de la factura eléctrica. Es la que se utiliza para realizar trabajo útil.

La energía activa es un indicador fundamental del consumo energético real de un circuito eléctrico, al contrario de la energía reactiva que no realiza trabajo útil. Pero ambas están relacionadas mediante el factor de potencia que influye en la eficiencia del sistema eléctrico.

Ademas, junto con la energia reactiva, el voltaje y la intensidad, son indicadores claves para el análisis de la calidad del suministro.
Utilizando técnicas de aprendizaje automático, entrenamos un modelo predictivo para estimar el valor de la energía activa. El modelo aprende de las relaciones entre las variables del dataset, permitiéndonos realizar predicciones precisas del consumo energético.
Por lo tanto, nuestro análisis va a concentrarse en predecir e interpretar a la energia activa, porque es la que se consume y se traduce en el costo de la factura eléctrica, además de ser clave para la eficiencia energética, el dimensionamiento de instalaciones, el análisis de la calidad del suministro y la planificación y gestión de la red eléctrica.
Ejemplos:
- Un proveedor de energía puede utilizar la predicción de la energía activa para determinar la cantidad de energía que necesita generar y distribuir en un momento dado.
- Una empresa puede utilizar la predicción de la energia activa para identificar oportunidades para reducir su consumo de energia y ahorrar dinero en sus facturas de electricidad.
- Un operador de red electrica puede utilizar la prediccion de la energia activa para identificar posibles sobrecargas en la red y tomar medidas para evitarlas.
