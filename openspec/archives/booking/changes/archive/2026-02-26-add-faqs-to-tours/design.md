# Design: Tour FAQs Integration

## Data Structure
The `faqs` field will be added as a top-level key within each tour object in the JSON array.

```json
{
  "id": "tour-id",
  ...
  "faqs": [
    {
      "question": "¿Pregunta 1?",
      "answer": "Respuesta 1."
    },
    {
      "question": "¿Pregunta 2?",
      "answer": "Respuesta 2."
    }
  ]
}
```

## Implementation Strategy
Since this is a data-only change, the primary focus is on generating high-quality, relevant content for each tour. The content should reflect the expertise of a historian (Alejandro) and address common pain points (like ticket management).

### FAQ Content Generation (Drafts)

#### 1. Alhambra Completa
- **Q:** ¿Cuánto tiempo se dedica a los Palacios Nazaríes?
- **A:** Dedicamos aproximadamente una hora a los Palacios Nazaríes para analizar en profundidad su iconografía y simbolismo, asegurando que comprendas cada detalle de esta joya arquitectónica.
- **Q:** ¿Es necesario caminar mucho?
- **A:** Sí, el recorrido por la Alhambra es extenso e incluye desniveles. Recomendamos calzado muy cómodo y preparación para una caminata de unas 3 horas.

#### 2. Alhambra sin Tickets
- **Q:** ¿Realmente vale la pena si no entro a los Palacios?
- **A:** ¡Absolutamente! El recinto de la Alhambra es una ciudad palatina enorme. Visitaremos lugares de libre acceso como el Palacio de Carlos V y los bosques, que guardan secretos históricos fascinantes que la mayoría de turistas pasan por alto.
- **Q:** ¿Puedo comprar las entradas durante el tour?
- **A:** No, las entradas suelen agotarse con semanas de antelación. Este tour está diseñado precisamente para quienes no consiguieron tickets pero quieren conocer la historia del recinto.

#### 3. Palacios Nazaríes
- **Q:** ¿Por qué hacer una visita solo de los Palacios?
- **A:** Al centrarnos exclusivamente en los Palacios Nazaríes, podemos detenernos en los detalles caligráficos y arquitectónicos que en una visita general se pasan por alto. Es una inmersión profunda para amantes del arte.
- **Q:** ¿Qué pasa si quiero ver el Generalife después?
- **A:** El guía te explicará cómo llegar al Generalife al finalizar la visita guiada en los Palacios, para que puedas explorarlo por tu cuenta si tienes la entrada correspondiente.

#### 4. Catedral de Granada
- **Q:** ¿Es la Catedral solo un edificio religioso?
- **A:** No, es un manifiesto político y artístico del triunfo cristiano tras la Reconquista. Analizaremos cómo el Renacimiento se usó para transformar la imagen de Granada.
- **Q:** ¿Cuánto dura la visita interior?
- **A:** Pasaremos aproximadamente una hora y cuarto en el interior, tiempo suficiente para admirar la Capilla Mayor y las naves sin prisas.

#### 5. Capilla Real
- **Q:** ¿Se pueden ver de cerca los sepulcros de los Reyes Católicos?
- **A:** Sí, nos situaremos frente a los mausoleos de mármol de Carrara para explicar su rica simbología y el legado dinástico que representan.
- **Q:** ¿Qué importancia tiene la colección de pintura flamenca?
- **A:** Es una de las colecciones personales más importantes de Europa. Veremos obras de gran valor que Isabel la Católica atesoró y que explican su gusto artístico personal.

#### 6. Monasterio de San Jerónimo
- **Q:** ¿Quién fue el Gran Capitán y por qué está enterrado aquí?
- **A:** Gonzalo Fernández de Córdoba fue el genio militar de los Reyes Católicos. Explicaremos su importancia histórica mientras visitamos su impresionante mausoleo.
- **Q:** ¿Qué veremos en los claustros?
- **A:** Visitaremos sus dos claustros renacentistas, espacios de gran paz que nos permiten entender cómo era la vida contemplativa de los monjes jerónimos.

#### 7. Monasterio de La Cartuja
- **Q:** ¿Por qué se dice que su sacristía es la más bella del mundo?
- **A:** Debido a su asombrosa decoración barroca en estuco, mármol y maderas preciosas. Es una explosión visual que busca representar la gloria divina de forma abrumadora.
- **Q:** ¿Cómo era la vida de un monje cartujo?
- **A:** Durante el tour explicaremos la regla del silencio y la soledad absoluta que seguían, lo cual contrasta fuertemente con la riqueza ornamental del edificio.

#### 8. Ruta Fray Leopoldo
- **Q:** ¿Es una ruta apta para personas con movilidad reducida?
- **A:** Sí, el recorrido por los lugares vinculados a Fray Leopoldo es mayoritariamente llano y accesible por las calles del centro de Granada.
- **Q:** ¿Se visita la cripta donde reposan sus restos?
- **A:** Sí, la visita incluye el paso por la cripta en la Iglesia de los Capuchinos, donde podrás ser testigo de la profunda devoción popular que aún hoy despierta.

#### 9. Ruta del Gran Capitán
- **Q:** ¿Este tour es muy técnico sobre historia militar?
- **A:** No, aunque hablamos de sus hazañas, nos centramos en su figura humana y su impacto en la transformación de la Granada musulmana a la cristiana.
- **Q:** ¿Qué relación tiene con el Monasterio de San Jerónimo?
- **A:** El monasterio fue elegido por él y su esposa como lugar de descanso eterno, y es el eje central para entender su legado en la ciudad.

#### 10. Ruta de San Juan de Dios
- **Q:** ¿Visitaremos el hospital que él fundó?
- **A:** Sí, conoceremos la historia del antiguo hospital y cómo Juan de Dios revolucionó el concepto de cuidado a los enfermos en el siglo XVI.
- **Q:** ¿Es una ruta muy larga?
- **A:** Tiene una duración de unas 2 horas a un ritmo pausado, recorriendo los lugares clave de su vida en el centro histórico.

#### 11. Basílica de San Juan de Dios
- **Q:** ¿Por qué hay tantos espejos en el interior?
- **A:** Los espejos, junto con el oro, se usaban en el barroco para multiplicar la luz y crear una atmósfera que recordara al cielo, buscando impresionar al fiel.
- **Q:** ¿Podemos subir al camarín del Santo?
- **A:** Dependiendo de la disponibilidad del monumento el día de la visita, intentaremos acceder a este espacio sagrado para ver de cerca las reliquias.

#### 12. Misterios y Leyendas del Albaicín
- **Q:** ¿Se cuentan historias de fantasmas?
- **A:** Más que fantasmas, nos centramos en enigmas históricos y leyendas populares que han pasado de generación en generación en el barrio más antiguo de Granada.
- **Q:** ¿El tour termina en el Mirador de San Nicolás?
- **A:** Sí, finalizamos allí para que puedas disfrutar de la puesta de sol sobre la Alhambra, una de las vistas más famosas del mundo.

#### 13. Abadía del Sacromonte
- **Q:** ¿Entraremos en las cuevas originales?
- **A:** Visitaremos las Santas Cuevas de la Abadía, donde se originó la leyenda de los Libros Plúmbeos y el origen del cristianismo en Granada.
- **Q:** ¿Hay que subir muchas cuestas?
- **A:** El barrio del Sacromonte tiene pendientes pronunciadas. El tour requiere cierta forma física o el uso del autobús urbano para algunos tramos si se prefiere.

#### 14. Centro Ciudad
- **Q:** ¿Veremos la Alcaicería (el antiguo mercado de seda)?
- **A:** Sí, pasearemos por sus estrechas calles para entender cómo funcionaba el comercio en la época nazarí y cómo ha evolucionado hasta hoy.
- **Q:** ¿Es una buena opción para un primer día en Granada?
- **A:** Es la opción ideal, ya que ofrece una visión general de la historia de la ciudad, desde sus raíces árabes hasta su esplendor renacentista.


## Risks & Mitigations
- **Data Consistency:** Ensure every tour has the same structure.
- **Language Accuracy:** Use professional Spanish terminology suitable for a historian guide.
