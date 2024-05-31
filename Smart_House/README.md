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

La energía activa total (p) y la energía reactiva total (q) contribuyen a la potencia aparente (s). La potencia aparente (s) está relacionada con el voltaje (v) y la corriente (i) a través de la impedancia (z).
El factor de potencia (pf) indica la eficiencia del sistema y está relacionado con el ángulo de fase (φ), que representa la relación temporal entre voltaje y corriente en sistemas de corriente alterna.

### Conclusion

La energia activa es la que realmente se consume y se traduce en el costo de la factura eléctrica. Es la que se utiliza para realizar trabajo útil.

La energía activa es un indicador fundamental del consumo energético real de un circuito eléctrico, al contrario de la energía reactiva que no realiza trabajo útil. Pero ambas están relacionadas mediante el factor de potencia que influye en la eficiencia del sistema eléctrico.
