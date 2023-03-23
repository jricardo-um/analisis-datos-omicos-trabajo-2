# Ideas en bruto

## Propagación de virus

- Potenciales reserorios
  
  - Se trata de escoger un virus (como el covid), identificar la proteina a la se se adhiere (la que interacciona con la _spike_ del covid) y hacer varios blast (u otro parecido) para encontrar proteinas o genes similares en otras especies, que serán más probablemente susceptibles a un salto de especie del virus. Nota: ver [portal de datos del covid](https://www.covid19dataportal.org).

- Diferencias entre proteinas
  
  - Una vez tengamos la lista de especies con proteinas parecidas las separamos entre "hay literatura que describe que pueden contraer el virus" y "no hay evidencia de que esté afectada por el virus". Haremos alineamientos por grupo y entre todos para ver las diferencias si las hay.
  
  - También se podría hacer con secuencias de proteina humanas separadas segun la susceptibilidad del paciente a contagiarse o a sufrir síntomas mayores, si hubiesen datos disponibles.

Lista de virus a investigar:

| pathogen | type<br>(genoma,dirección,#cadenas,membrana) | family | host protein |
| --- | --- | --- | --- |
| MERS-CoV | ARN,-,1,+ | Coronaviridae | DDP4,CD26 |
| SARS-CoV | ?,?,?,? | Coronaviridae | ACE2 |
| SARS-CoV-2 | ARN,-,1,+ | Coronaviridae | ACE2 |
| Marburgo | ?,?,?,? | ? | ? |
| Gripe | ARN,-,1,? | ? | ? |

Info:
`A poner links aquí`

# Características de los tipos de trabajos (copiado)

1. Ensamblado de novo. Se podrá partir de un conjunto de datos FASTQ para obtener su genoma. Una vez obtenido el ensamblado, se habrá de intentar anotar el contenido.

2. Identificación de variantes. Se podrá partir de datos DNA-Seq y se aplicarán herramientas de identificación de variantes. Se deberán analizar y describir las variantes más significativas a partir del contenido de bases de datos existentes.

3. Análisis de expresión diferencial. Se deberá realizar un análisis de expresión diferencial escogiendo para ello la comparación de dos condiciones diferentes. Se procurará utilizar un mínimo de 3 muestras por condición. Se deberá realizar una caracterización funcional de los genes expresados diferencialmente.

4. Análisis metagenómico.

5. Otro tipo de trabajo que los estudiantes planteen.
   Los trabajos podrán combinar características de varios tipos de trabajos. Los estudiantes
   deberán justificar la selección de los datos a partir del objetivo específico de su trabajo.

Los trabajos deberán arrancar de los ficheros FASTQ disponibles, aunque en los repositorios de datos NGS puedan estar disponibles ficheros BAM con los alineamientos BAM ya obtenidos. No se podrán utilizar datos que posteriormente sean utilizados por los estudiantes para su TFM.

