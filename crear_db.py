import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "catecismo.db")

def crear_base_de_datos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS catecismo (
            id INTEGER PRIMARY KEY,
            domingo INTEGER NOT NULL,
            pregunta TEXT NOT NULL,
            respuesta TEXT NOT NULL,
            meditacion TEXT NOT NULL
        )
    """)

    # Las 129 preguntas del Catecismo de Heidelberg
    preguntas = [
        # === PARTE I: LA MISERIA DEL HOMBRE (Domingos 2-4) ===
        (1, 1,
         "¿Cuál es tu único consuelo tanto en la vida como en la muerte?",
         "Que yo, con cuerpo y alma, tanto en la vida como en la muerte, no me pertenezco a mí mismo, sino a mi fiel Salvador Jesucristo, que me libró del poder del diablo, satisfaciendo enteramente con su preciosa sangre por todos mis pecados, y me guarda de tal manera que sin la voluntad de mi Padre celestial ni un solo cabello de mi cabeza puede caer; antes es necesario que todas las cosas sirvan para mi salvación. Por eso también me asegura, por su Espíritu Santo, la vida eterna y me hace pronto y aparejado para vivir en adelante según su santa voluntad.",
         "El Catecismo de Heidelberg comienza con la pregunta más fundamental de la vida cristiana: ¿dónde encontramos verdadero consuelo? La respuesta nos revela que nuestro consuelo no depende de nuestras circunstancias, sino de a quién pertenecemos. Pertenecemos a Cristo, no a nosotros mismos. Esto transforma todo. Si somos de Cristo, entonces Él es responsable de nosotros. Él pagó por nuestros pecados con su sangre, nos libró del dominio del diablo, y nos guarda cada día. Ni un cabello cae sin el permiso de nuestro Padre celestial. Medita hoy en esta verdad gloriosa: no estás solo, no estás abandonado. Perteneces al Salvador que dio su vida por ti. Que esta certeza te dé paz en medio de cualquier tormenta."),

        (2, 1,
         "¿Cuántas cosas debes saber para que, gozando de este consuelo, puedas vivir y morir dichosamente?",
         "Tres: La primera, cuán grandes son mis pecados y miserias. La segunda, de qué manera soy librado de todos mis pecados y miserias. La tercera, cómo he de ser agradecido a Dios por tal liberación.",
         "El catecismo nos presenta un esquema triple que organiza toda la vida cristiana: miseria, liberación y gratitud. No podemos apreciar la gracia si primero no entendemos la profundidad de nuestro pecado. Y una vez que comprendemos cuán grande es nuestra liberación, la respuesta natural es una vida de gratitud. Este esquema no es solo teológico, es profundamente práctico. Cada día necesitamos recordar de dónde nos sacó Dios, lo que Cristo hizo por nosotros, y cómo debemos vivir en respuesta a tan grande amor. Reflexiona: ¿vives con esta triple conciencia diariamente?"),

        (3, 2,
         "¿De dónde conoces tu miseria?",
         "De la Ley de Dios.",
         "La ley de Dios funciona como un espejo que nos muestra quiénes somos realmente. Sin la ley, viviríamos en una falsa seguridad, pensando que somos buenos por naturaleza. Pero cuando nos miramos en el espejo de los mandamientos divinos, descubrimos cuán lejos estamos de la perfección que Dios requiere. Este conocimiento no es para destruirnos, sino para llevarnos a Cristo. La ley es nuestro ayo que nos conduce al Salvador (Gálatas 3:24). Hoy, en lugar de huir de la ley de Dios, permítele que haga su obra en tu corazón, mostrándote tu necesidad de gracia."),

        (4, 2,
         "¿Qué requiere la Ley de Dios de nosotros?",
         "Cristo nos lo enseña en Mateo 22:37-40: Amarás al Señor tu Dios con todo tu corazón, con toda tu alma y con toda tu mente. Este es el primero y grande mandamiento. Y el segundo es semejante: Amarás a tu prójimo como a ti mismo. De estos dos mandamientos depende toda la ley y los profetas.",
         "Toda la ley de Dios se resume en una sola palabra: amor. Amor total a Dios y amor genuino al prójimo. Pero aquí está el problema: ninguno de nosotros puede cumplir este mandamiento perfectamente. No amamos a Dios con todo nuestro corazón; a menudo lo relegamos a un segundo plano. No amamos a nuestro prójimo como a nosotros mismos; frecuentemente somos egoístas. Esta es precisamente la miseria que el catecismo quiere que reconozcamos. Solo cuando admitimos que no podemos amar como Dios manda, estamos listos para buscar ayuda en Cristo, quien cumplió la ley perfectamente por nosotros."),

        (5, 2,
         "¿Puedes guardar todo esto perfectamente?",
         "No, porque por naturaleza estoy inclinado a aborrecer a Dios y a mi prójimo.",
         "Esta respuesta es dura pero honesta. Por naturaleza, no solo fallamos en amar a Dios y al prójimo, sino que estamos inclinados a lo opuesto: al aborrecimiento. Nuestra naturaleza caída no es neutral; está activamente inclinada al mal. Esto no significa que no podamos hacer nada bueno externamente, pero significa que incluso nuestras mejores obras están manchadas por motivos egoístas. Reconocer esto no es pesimismo, es realismo bíblico. Y este realismo nos prepara para recibir con brazos abiertos la gracia de Dios en Cristo. Solo quien sabe que está enfermo busca al médico."),

        (6, 3,
         "¿Creó Dios al hombre tan malo y perverso?",
         "No. Dios creó al hombre bueno y a su imagen, es decir, en verdadera justicia y santidad, para que rectamente conociera a Dios su Creador, lo amara de todo corazón y viviera con Él en eterna bienaventuranza para alabarle y glorificarle.",
         "Dios no es el autor del mal. Él creó al hombre bueno, a su propia imagen. Fuimos diseñados para conocer a Dios, amarlo y disfrutarlo eternamente. Esta es una verdad crucial: el mal no es parte del diseño original. El sufrimiento, la maldad y la muerte son intrusos en la buena creación de Dios. Esto nos da esperanza, porque si el mal no es original sino que entró después, entonces puede ser vencido. Y en Cristo, precisamente eso es lo que sucede: Dios está restaurando todas las cosas a su diseño original. Medita hoy en el propósito para el cual fuiste creado: conocer y amar a Dios."),

        (7, 3,
         "¿De dónde procede esta corrupción de la naturaleza humana?",
         "De la caída y desobediencia de nuestros primeros padres Adán y Eva en el paraíso, donde nuestra naturaleza quedó de tal manera corrompida, que todos somos concebidos y nacidos en pecado.",
         "La doctrina del pecado original nos enseña que la corrupción humana no es un problema individual sino universal. No nos volvemos pecadores cuando pecamos por primera vez; nacemos pecadores. Adán, como cabeza federal de la humanidad, nos representó a todos cuando desobedeció. Su caída fue nuestra caída. Esto puede parecer injusto hasta que consideramos al segundo Adán: Cristo. Así como en Adán todos caímos, en Cristo todos los que creen son levantados (Romanos 5:19). La representación federal que nos condenó en Adán es la misma que nos salva en Cristo."),

        (8, 3,
         "¿Estamos tan corrompidos que somos totalmente incapaces de hacer el bien e inclinados a todo mal?",
         "Sí, a menos que seamos regenerados por el Espíritu de Dios.",
         "La doctrina de la depravación total no significa que hagamos todo el mal posible, sino que cada parte de nuestro ser está afectada por el pecado. Nuestra mente, voluntad, emociones y cuerpo están corrompidos. No podemos salvarnos a nosotros mismos ni siquiera dar el primer paso hacia Dios por nuestra propia fuerza. Pero hay esperanza: el Espíritu de Dios puede regenerarnos. La regeneración es el acto sobrenatural por el cual Dios nos da un nuevo corazón, nuevos deseos y nueva vida. Lo que es imposible para el hombre es posible para Dios. ¡Qué consuelo saber que nuestra salvación depende de Él y no de nosotros!"),

        (9, 4,
         "¿No es Dios injusto al requerir en su Ley lo que el hombre no puede cumplir?",
         "No, porque Dios hizo al hombre capaz de cumplirla; pero el hombre, por instigación del diablo, se privó a sí mismo y a toda su descendencia, por desobediencia voluntaria, de estos dones divinos.",
         "Esta pregunta aborda una objeción natural: si no podemos cumplir la ley, ¿es justo que Dios la exija? La respuesta es clara: Dios nos creó con la capacidad de obedecerle perfectamente. Fuimos nosotros quienes perdimos esa capacidad por nuestra propia desobediencia. Sería como si alguien destruyera voluntariamente sus herramientas de trabajo y luego se quejara de que no puede trabajar. Dios no redujo sus estándares porque nosotros nos degradamos. Su justicia permanece intacta. Pero en su misericordia, proveyó a Cristo para cumplir la ley en nuestro lugar."),

        (10, 4,
         "¿Dejará Dios sin castigo tal desobediencia y apostasía?",
         "De ninguna manera; antes bien, su ira se enciende terriblemente, tanto contra el pecado original como contra los actuales de los hombres, y los castigará en justo juicio temporal y eternamente, como Él ha dicho: Maldito todo aquel que no permanece en todas las cosas escritas en el libro de la Ley, para hacerlas.",
         "Dios no puede ignorar el pecado. Su santidad y justicia demandan que toda transgresión sea castigada. Esto puede sonar aterrador, y debería. El pecado tiene consecuencias reales y eternas. Pero esta verdad, lejos de dejarnos sin esperanza, nos prepara para apreciar la magnitud de lo que Cristo hizo en la cruz. Él recibió el castigo que merecíamos. La ira de Dios contra nuestro pecado fue derramada sobre su Hijo. La justicia fue satisfecha y la misericordia fue extendida. Sin la cruz, estaríamos perdidos. Con la cruz, somos libres."),

        (11, 4,
         "¿No es Dios también misericordioso?",
         "Dios es ciertamente misericordioso, pero también es justo; por tanto, su justicia requiere que el pecado cometido contra la altísima majestad de Dios sea castigado con el sumo castigo, es decir, con el castigo eterno en cuerpo y alma.",
         "Esta pregunta equilibra dos atributos divinos que a menudo se malinterpretan. Dios es misericordioso, sí, pero su misericordia no anula su justicia. Algunos piensan que un Dios amoroso nunca castigaría, pero eso sería un dios hecho a nuestra imagen. El Dios verdadero es tanto perfectamente justo como perfectamente misericordioso. El milagro del evangelio es que en la cruz, ambos atributos se encuentran: la justicia es satisfecha y la misericordia es derramada. Cristo llevó nuestro castigo (justicia) para que nosotros recibiéramos perdón (misericordia). En la cruz, Dios es justo y justificador."),

        # === PARTE II: LA LIBERACIÓN DEL HOMBRE (Domingos 5-31) ===
        (12, 5,
         "Puesto que por el justo juicio de Dios merecemos el castigo temporal y eterno, ¿cómo podremos escapar de este castigo y volver a ser recibidos en gracia?",
         "Dios quiere que su justicia sea satisfecha; por eso es preciso que le hagamos cumplida satisfacción, o por nosotros mismos o por otro.",
         "Aquí comienza la segunda parte del catecismo: la liberación. La pregunta es directa: ¿cómo escapamos del castigo que merecemos? La respuesta establece un principio fundamental: la justicia de Dios debe ser satisfecha. No hay atajos, no hay excepciones. Alguien tiene que pagar. O pagamos nosotros eternamente, o alguien paga por nosotros. Esta es la base de la doctrina de la sustitución. Cristo se puso en nuestro lugar. Él satisfizo la justicia divina que nosotros jamás podríamos satisfacer. Cada vez que sientas el peso de tu pecado, recuerda: la deuda ya fue pagada."),

        (13, 5,
         "¿Podemos por nosotros mismos hacer esta satisfacción?",
         "De ninguna manera; antes bien, aumentamos cada día nuestra deuda.",
         "No solo no podemos pagar nuestra deuda con Dios, sino que cada día la aumentamos. Cada pecado añade más a una cuenta que ya era impagable. Es como intentar salir de un hoyo cavando más profundo. Nuestros mejores esfuerzos religiosos, nuestras obras más nobles, no pueden borrar ni un solo pecado. Esta verdad nos lleva a la desesperación de nosotros mismos, y eso es exactamente lo que Dios quiere. Porque solo cuando dejamos de confiar en nuestras propias fuerzas estamos listos para confiar completamente en Cristo. La bancarrota espiritual es el primer paso hacia la riqueza de la gracia."),

        (14, 5,
         "¿Puede alguna criatura pagar por nosotros?",
         "Ninguna; porque, en primer lugar, Dios no quiere castigar en otra criatura lo que el hombre ha cometido; y además, ninguna pura criatura puede soportar el peso de la ira eterna de Dios contra el pecado y librar de ella a otros.",
         "Ni un ángel, ni un santo, ni ninguna criatura puede pagar nuestra deuda. Primero, porque la justicia demanda que sea un humano quien pague por pecados humanos. Segundo, porque ninguna criatura finita puede soportar un castigo infinito. Solo alguien que sea verdaderamente humano y verdaderamente divino puede satisfacer estas condiciones. Este razonamiento nos lleva inevitablemente a Cristo: Dios encarnado, plenamente hombre y plenamente Dios. Él es el único mediador posible. No hay otro camino, no hay otro nombre bajo el cielo en que podamos ser salvos."),

        (15, 6,
         "¿Qué clase de Mediador y Libertador debemos buscar?",
         "Uno que sea verdadero hombre y perfectamente justo, y sin embargo más poderoso que todas las criaturas, es decir, que sea al mismo tiempo verdadero Dios.",
         "El catecismo nos presenta el perfil del Salvador que necesitamos. Debe ser verdadero hombre para representarnos. Debe ser perfectamente justo para no tener pecado propio. Y debe ser verdadero Dios para poder soportar el peso infinito de la ira divina. Solo una persona en toda la historia cumple estos requisitos: Jesucristo. Él es el Dios-hombre, el mediador perfecto entre Dios y los hombres. No fue un accidente que el Hijo de Dios se hiciera hombre; fue el plan eterno de Dios para rescatar a su pueblo. Maravíllate hoy ante la sabiduría infinita de Dios en la salvación."),

        (16, 6,
         "¿Por qué debe ser verdadero hombre y perfectamente justo?",
         "Porque la justicia de Dios requiere que la misma naturaleza humana que ha pecado, pague por el pecado; y un hombre que fuera él mismo pecador no podría pagar por otros.",
         "La encarnación no es opcional en el plan de salvación. Dios requiere que la naturaleza humana que pecó sea la misma que pague. Por eso el Hijo de Dios tomó carne humana. Pero además debía ser sin pecado, porque un pecador no puede pagar por otros pecadores. Cristo vivió la vida perfecta que nosotros debíamos haber vivido. Su obediencia activa, cumpliendo toda la ley, se nos acredita por la fe. Y su obediencia pasiva, sufriendo en la cruz, paga nuestro castigo. En Cristo tenemos tanto la justicia positiva que necesitamos como el perdón de nuestros pecados."),

        (17, 6,
         "¿Por qué debe ser al mismo tiempo verdadero Dios?",
         "Para que por el poder de su divinidad, pudiera llevar en su naturaleza humana el peso de la ira de Dios contra el pecado y nos obtuviera y restituyera la justicia y la vida.",
         "Si Cristo fuera solo hombre, no podría haber soportado la ira infinita de Dios. La divinidad de Cristo sostuvo su humanidad mientras sufría en la cruz. El peso del pecado del mundo requería hombros divinos. Además, solo Dios puede otorgar justicia y vida eterna. Un mero hombre podría morir, pero no podría dar vida a otros. Cristo, siendo Dios, tiene el poder de dar vida eterna a todos los que creen en Él. La divinidad de Cristo no es un detalle teológico menor; es la garantía de que su sacrificio fue suficiente y de que nuestra salvación es segura."),

        (18, 6,
         "¿Quién es este Mediador, que es al mismo tiempo verdadero Dios y verdadero hombre justo?",
         "Nuestro Señor Jesucristo, que nos ha sido hecho por Dios sabiduría, justificación, santificación y redención.",
         "Después de describir al mediador que necesitamos, el catecismo revela su nombre: Jesucristo. Él es la respuesta a todas nuestras necesidades. ¿Necesitamos sabiduría? Cristo es nuestra sabiduría. ¿Necesitamos ser declarados justos? Cristo es nuestra justificación. ¿Necesitamos ser transformados? Cristo es nuestra santificación. ¿Necesitamos ser rescatados? Cristo es nuestra redención. Todo lo que necesitamos se encuentra en una sola persona. No necesitamos buscar en múltiples lugares; todo está en Jesús. Hoy, descansa en la suficiencia de Cristo para cada área de tu vida."),

        (19, 6,
         "¿De dónde sabes esto?",
         "Del santo Evangelio, el cual Dios mismo reveló primeramente en el paraíso; después lo proclamó por los santos patriarcas y profetas, lo representó por los sacrificios y otras ceremonias de la Ley, y por último lo cumplió por medio de su Hijo unigénito.",
         "El evangelio no es una invención tardía. Desde el mismo jardín del Edén, Dios prometió un Salvador (Génesis 3:15). A lo largo del Antiguo Testamento, esta promesa fue desarrollada: a través de Abraham, Moisés, David y los profetas. Los sacrificios del templo apuntaban hacia el sacrificio perfecto de Cristo. Toda la Biblia cuenta una sola historia: la historia de la redención en Cristo. Cuando lees el Antiguo Testamento, busca a Cristo en cada página. Él es el cordero prometido, el rey esperado, el profeta anunciado. La Biblia entera es un testimonio de Jesús."),

        (20, 7,
         "¿Son salvos por Cristo todos los hombres, así como fueron condenados por Adán?",
         "No, solamente aquellos que por verdadera fe son injertados en Él y reciben todos sus beneficios.",
         "La salvación no es automática ni universal. Aunque Cristo es suficiente para salvar a todos, su salvación es eficaz solo para aquellos que creen. La fe es el instrumento por el cual nos unimos a Cristo y recibimos sus beneficios. Sin fe, permanecemos en nuestra condenación en Adán. Con fe, somos trasladados al reino de Cristo. Esto no significa que la fe sea una obra que hacemos; la fe misma es un don de Dios. Pero es el medio que Dios ha establecido para que recibamos la salvación. Examina tu corazón: ¿tienes verdadera fe en Cristo?"),

        (21, 7,
         "¿Qué es la verdadera fe?",
         "No es solo un conocimiento cierto por el cual tengo por verdadero todo lo que Dios nos ha revelado en su Palabra, sino también una confianza plena que el Espíritu Santo infunde en mi corazón por el Evangelio, asegurándome que no solo a otros, sino también a mí, Dios ha dado la remisión de pecados, la justicia y la vida eterna, y todo por pura gracia y solamente por los méritos de Jesucristo.",
         "La fe tiene dos dimensiones: conocimiento y confianza. No basta con saber datos sobre Cristo; hay que confiar personalmente en Él. El demonio sabe que Cristo murió y resucitó, pero no confía en Él. La verdadera fe va más allá del conocimiento intelectual: es una confianza personal que dice 'Cristo murió por mí'. Esta fe no la producimos nosotros; es obra del Espíritu Santo en nuestro corazón. Hoy, pregúntate: ¿mi fe es solo conocimiento o es también confianza viva? ¿Puedo decir con certeza que Cristo es MI Salvador?"),

        (22, 7,
         "¿Qué es lo que ha de creer un cristiano?",
         "Todo lo que nos es prometido en el Evangelio, que en resumen nos enseñan los artículos de la fe cristiana universal e indudable.",
         "La fe cristiana no es vaga ni indefinida. Tiene contenido específico resumido en el Credo Apostólico. No creemos en cualquier cosa; creemos en verdades reveladas por Dios. El credo nos da un resumen confiable de las doctrinas esenciales: Dios como Creador, Cristo como Salvador, el Espíritu Santo como Santificador. Estos no son inventos humanos, son verdades divinas. Conocer el contenido de la fe nos protege del error y nos da fundamento sólido. Estudia el credo, medita en sus verdades, y haz de ellas el fundamento de tu vida diaria."),

        (23, 7,
         "¿Cuáles son estos artículos?",
         "Creo en Dios Padre Todopoderoso, Creador del cielo y de la tierra. Creo en Jesucristo, su único Hijo, Señor nuestro; que fue concebido por obra del Espíritu Santo, nació de la Virgen María; padeció bajo el poder de Poncio Pilato, fue crucificado, muerto y sepultado; descendió a los infiernos; al tercer día resucitó de entre los muertos; subió a los cielos y está sentado a la diestra de Dios Padre Todopoderoso; y desde allí ha de venir a juzgar a los vivos y a los muertos. Creo en el Espíritu Santo; la santa Iglesia universal; la comunión de los santos; el perdón de los pecados; la resurrección de la carne y la vida perdurable. Amén.",
         "El Credo Apostólico es el resumen más antiguo y venerado de la fe cristiana. En pocas palabras abarca toda la historia de la salvación: creación, caída, redención y consumación. Cada frase está cargada de significado teológico profundo. Cuando recitamos el credo, nos unimos a millones de creyentes a lo largo de los siglos que han confesado la misma fe. No es una fórmula vacía, sino una declaración viva de lo que creemos. Tómate tiempo para meditar en cada línea del credo. Cada palabra es un tesoro de verdad que merece ser explorado y atesorado."),

        (24, 8,
         "¿Cómo se dividen estos artículos?",
         "En tres partes: La primera trata de Dios Padre y de nuestra creación. La segunda, de Dios Hijo y de nuestra redención. La tercera, de Dios Espíritu Santo y de nuestra santificación.",
         "El credo se estructura de forma trinitaria: Padre, Hijo y Espíritu Santo. Cada persona de la Trinidad tiene una obra especial en nuestra salvación. El Padre nos creó, el Hijo nos redimió, y el Espíritu nos santifica. Pero esto no significa que actúen por separado; las tres personas obran juntas en todo. La estructura trinitaria del credo nos recuerda que servimos a un Dios trino: un solo Dios en tres personas. Este misterio está en el corazón de nuestra fe y es la base de nuestra salvación."),

        (25, 8,
         "Puesto que no hay más que una sola esencia divina, ¿por qué nombras tres: Padre, Hijo y Espíritu Santo?",
         "Porque Dios se ha revelado así en su Palabra, que estas tres personas distintas son el único, verdadero y eterno Dios.",
         "La doctrina de la Trinidad no es una invención filosófica sino una revelación bíblica. Dios se ha revelado como uno en esencia y tres en personas. No tres dioses, sino un solo Dios en tres personas distintas. Esto supera nuestra comprensión, pero no contradice la razón. Es un misterio que adoramos, no un problema que resolvemos. El Padre no es el Hijo, el Hijo no es el Espíritu, pero los tres son el mismo Dios. Que la Trinidad te inspire a la adoración humilde de un Dios que es infinitamente más grande que nuestra capacidad de comprenderlo."),

        (26, 9,
         "¿Qué crees cuando dices: Creo en Dios Padre Todopoderoso, Creador del cielo y de la tierra?",
         "Que el eterno Padre de nuestro Señor Jesucristo, que de la nada creó el cielo y la tierra con todo lo que en ellos hay, y que los sustenta y gobierna por su eterno consejo y providencia, es mi Dios y mi Padre por causa de Cristo su Hijo; en quien de tal manera confío que no dudo que Él me proveerá de todo lo necesario para el cuerpo y para el alma; y además, que convertirá en mi beneficio cualquier mal que me envíe en este valle de lágrimas, puesto que Él puede hacerlo como Dios omnipotente, y quiere hacerlo como Padre fiel.",
         "Esta respuesta es profundamente personal. No dice simplemente que Dios es Creador, sino que es MI Dios y MI Padre. El Todopoderoso que hizo el universo de la nada es el mismo que cuida de ti personalmente. Él proveerá todo lo necesario para tu cuerpo y tu alma. Y aún más asombroso: convertirá en tu beneficio cualquier mal que te llegue. Puede hacerlo porque es omnipotente. Quiere hacerlo porque es tu Padre fiel. Romanos 8:28 cobra vida aquí. Hoy, confía en que tu Padre celestial tiene el poder y la voluntad de cuidarte."),

        (27, 10,
         "¿Qué entiendes por providencia de Dios?",
         "Es la omnipotente y omnipresente fuerza de Dios, por la cual sustenta y gobierna el cielo y la tierra con todas las criaturas, de tal manera que las hierbas y la lluvia, la sequía y el fruto, la comida y la bebida, la salud y la enfermedad, las riquezas y la pobreza, y todas las cosas, no acontecen por casualidad, sino por su consejo y voluntad paternal.",
         "Nada sucede por casualidad. Desde la lluvia que cae hasta la enfermedad que llega, todo está bajo el gobierno soberano de Dios. Esto no significa que Dios cause el mal, pero sí que nada escapa a su control. La providencia es el gobierno continuo de Dios sobre su creación. Cada detalle de tu vida, grande o pequeño, está en sus manos. Esto no es fatalismo; es confianza en un Padre amoroso que dirige todas las cosas para bien de sus hijos. Cuando las circunstancias parezcan caóticas, recuerda: hay un Dios soberano que no ha perdido el control."),

        (28, 10,
         "¿De qué nos sirve saber que Dios ha creado todas las cosas y que aún las sustenta por su providencia?",
         "Que debemos ser pacientes en la adversidad, agradecidos en la prosperidad, y que para el porvenir debemos tener gran confianza en nuestro fiel Dios y Padre, de que ninguna criatura nos separará de su amor, ya que todas las criaturas están de tal manera en su mano, que sin su voluntad no pueden moverse ni actuar.",
         "La doctrina de la providencia tiene consecuencias prácticas enormes. En la adversidad: paciencia, porque Dios está en control. En la prosperidad: gratitud, porque todo viene de su mano. Para el futuro: confianza, porque nada nos puede separar de su amor. Esta triple respuesta transforma nuestra actitud ante la vida. Ya no somos víctimas de las circunstancias sino hijos de un Padre soberano. Las criaturas no pueden hacernos daño sin su permiso. Vive hoy con la paz que viene de saber que el Todopoderoso es tu Padre."),

        # Domingos sobre el Hijo
        (29, 11,
         "¿Por qué es llamado Hijo de Dios: Jesús, esto es, Salvador?",
         "Porque Él nos salva y nos libra de todos nuestros pecados, y porque en ningún otro se debe buscar ni se puede hallar salvación alguna.",
         "El nombre Jesús significa 'Jehová salva'. No es un nombre casual sino un programa de vida. Jesús vino específicamente a salvar a su pueblo de sus pecados. Y esta salvación es exclusiva: no hay otro salvador, no hay otro camino, no hay otro nombre. En un mundo que ofrece múltiples opciones de salvación, el catecismo es claro: solo en Jesús hay esperanza. No en nuestras obras, no en otros líderes religiosos, no en filosofías humanas. Solo Jesús salva. Aférrate a Él como tu única esperanza."),

        (30, 11,
         "¿Creen entonces en el único Salvador Jesús los que buscan su bienaventuranza y salvación en los santos, en sí mismos, o en alguna otra parte?",
         "No; antes niegan con los hechos al único Salvador Jesús, aunque se gloríen de ser de Él; porque una de dos: o Jesús no es un Salvador perfecto, o los que por verdadera fe reciben a este Salvador, tienen que encontrar en Él todo lo necesario para su salvación.",
         "Este es un principio radical: o Cristo es suficiente o no lo es. No podemos dividir nuestra confianza entre Cristo y algo más. Si añadimos nuestras obras, santos, o cualquier otra cosa a Cristo como base de salvación, estamos diciendo que Cristo solo no basta. Pero la Escritura es clara: Cristo es un Salvador completo y perfecto. En Él encontramos todo lo necesario. No hay suplementos que añadir al evangelio. Examina tu corazón: ¿descansas solo en Cristo o estás añadiendo algo a tu confianza en Él?"),

        (31, 12,
         "¿Por qué es llamado Cristo, es decir, Ungido?",
         "Porque ha sido ordenado por Dios Padre y ungido con el Espíritu Santo para ser nuestro supremo Profeta y Doctor, que nos ha revelado enteramente el secreto consejo y la voluntad de Dios acerca de nuestra redención; y para ser nuestro único Sumo Sacerdote, que por el único sacrificio de su cuerpo nos ha redimido, e intercede continuamente por nosotros ante el Padre; y para ser nuestro eterno Rey, que nos gobierna por su Palabra y Espíritu, y nos guarda y conserva en la redención obtenida para nosotros.",
         "Cristo significa 'Ungido'. Jesús fue ungido para tres oficios: Profeta, Sacerdote y Rey. Como Profeta, nos revela la voluntad de Dios. Como Sacerdote, se ofrece a sí mismo por nosotros e intercede constantemente. Como Rey, nos gobierna y protege. En el Antiguo Testamento, profetas, sacerdotes y reyes eran personas diferentes. En Cristo, los tres oficios se unen perfectamente. Él es todo lo que necesitamos: nos enseña, nos salva y nos gobierna. Hoy, recibe a Cristo en sus tres oficios y permite que sea tu Profeta, Sacerdote y Rey."),

        (32, 12,
         "¿Por qué eres llamado cristiano?",
         "Porque por la fe soy miembro de Cristo y participo de su unción, para que confiese su nombre, me ofrezca a mí mismo como un sacrificio vivo de gratitud, y con libre conciencia combata contra el pecado y el diablo en esta vida, y después reine con Él eternamente sobre todas las criaturas.",
         "Ser cristiano no es solo una etiqueta; es participar de los oficios de Cristo. Somos profetas al confesar su nombre. Somos sacerdotes al ofrecernos como sacrificios vivos. Somos reyes al combatir contra el pecado y al anticipar nuestro reinado eterno con Cristo. Nuestra identidad como cristianos no es pasiva sino activa. Tenemos una misión: confesar, ofrecernos y luchar. Y tenemos una esperanza: reinar eternamente con Cristo. Hoy, vive como lo que eres: un profeta, sacerdote y rey ungido por el Espíritu de Cristo."),

        (33, 13,
         "¿Por qué es llamado Hijo unigénito de Dios, ya que nosotros también somos hijos de Dios?",
         "Porque solo Cristo es el Hijo eterno y natural de Dios; mas nosotros somos hijos de Dios adoptados por gracia, por causa de Él.",
         "Hay una diferencia fundamental entre la filiación de Cristo y la nuestra. Cristo es Hijo de Dios por naturaleza, desde la eternidad. Nosotros somos hijos por adopción, por gracia. Él es el Hijo unigénito; nosotros somos hijos adoptados. Pero qué maravillosa es nuestra adopción: el Dios del universo nos ha recibido en su familia. No por nuestros méritos, sino por causa de Cristo. Somos coherederos con Él de todas las promesas de Dios. La adopción es uno de los privilegios más dulces del evangelio. Hoy, vive como hijo amado del Padre."),

        (34, 13,
         "¿Por qué le llamas Señor nuestro?",
         "Porque nos ha comprado y rescatado del pecado y del poder del diablo, no con oro ni con plata, sino con su preciosa sangre, y nos ha libertado de todo el poder del diablo, para hacernos suyos.",
         "Jesús es nuestro Señor porque nos compró con su propia sangre. No somos nuestros; fuimos comprados por precio (1 Corintios 6:20). El señorío de Cristo no es una tiranía sino una liberación. Nos rescató de la esclavitud del pecado y del diablo para hacernos suyos. Bajo su señorío encontramos verdadera libertad. El mundo busca autonomía, pero la verdadera libertad se encuentra en la sumisión a Cristo. Cuando Él es Señor de tu vida, ya nada te esclaviza. Rinde hoy todo aspecto de tu vida a su autoridad amorosa."),

        (35, 14,
         "¿Qué quiere decir: que fue concebido por obra del Espíritu Santo, nació de la Virgen María?",
         "Que el eterno Hijo de Dios, el cual es y permanece verdadero y eterno Dios, tomó la verdadera naturaleza humana de la carne y sangre de la Virgen María, por obra del Espíritu Santo, para ser también verdadera simiente de David, semejante a sus hermanos en todo, excepto en el pecado.",
         "La concepción virginal es esencial para nuestra salvación. Cristo tomó verdadera naturaleza humana, pero sin pecado. El Espíritu Santo obró sobrenaturalmente para que el Hijo de Dios naciera como verdadero hombre sin heredar la corrupción del pecado original. Es verdadero Dios y verdadero hombre en una sola persona. Este misterio de la encarnación es el fundamento de nuestra redención. Si Cristo no fuera verdadero hombre, no podría representarnos. Si no fuera sin pecado, no podría salvarnos. Maravíllate ante el milagro de la encarnación."),

        (36, 14,
         "¿Qué beneficio recibes de la santa concepción y nacimiento de Cristo?",
         "Que Él es nuestro Mediador y con su inocencia y perfecta santidad cubre, delante de Dios, mi pecado, en el cual fui concebido.",
         "La concepción santa de Cristo beneficia directamente a cada creyente. Donde nosotros fuimos concebidos en pecado, Cristo fue concebido en santidad. Su pureza cubre nuestra impureza. Su inocencia cubre nuestra culpa. Como nuestro Mediador, se presenta ante Dios con una naturaleza humana perfecta y nos viste con su justicia. Este es el maravilloso intercambio del evangelio: Él tomó nuestro pecado y nos dio su justicia. Hoy, presenta te ante Dios con confianza, no por tu propia bondad, sino cubierto por la perfecta santidad de Cristo."),

        (37, 15,
         "¿Qué entiendes por la palabra padeció?",
         "Que todo el tiempo que vivió en la tierra, pero especialmente al fin de su vida, sufrió en cuerpo y alma la ira de Dios contra el pecado de todo el género humano, a fin de que con su pasión, como único sacrificio propiciatorio, nos librara en cuerpo y alma de la condenación eterna, y nos obtuviera la gracia de Dios, la justicia y la vida eterna.",
         "El sufrimiento de Cristo no fue solo físico. Durante toda su vida, y especialmente en la cruz, soportó la ira de Dios contra el pecado. Esto es lo que significa la propiciación: Cristo absorbió la ira divina en nuestro lugar. Su sufrimiento tuvo un propósito redentor: librarnos de la condenación y obtener para nosotros gracia, justicia y vida eterna. Cuando meditas en la pasión de Cristo, no pienses solo en los clavos y la corona de espinas. Piensa en el peso infinito de la ira divina que cayó sobre Él por amor a ti."),

        (38, 15,
         "¿Por qué padeció bajo el poder de Poncio Pilato como juez?",
         "Para que, siendo inocente, fuera condenado por juez temporal, y con esto nos librara del severo juicio de Dios que a nosotros nos amenazaba.",
         "El detalle histórico de Poncio Pilato no es casual. Cristo fue condenado por un juez terrenal para librarnos de la condenación del Juez celestial. El inocente fue tratado como culpable para que los culpables fuéramos tratados como inocentes. Este intercambio es la esencia del evangelio. Pilato sabía que Jesús era inocente, pero lo condenó de todos modos. En la providencia de Dios, este acto de injusticia humana sirvió para la mayor justicia: nuestra salvación. Dios obra incluso a través de la maldad humana para cumplir sus propósitos redentores."),

        (39, 15,
         "¿Tiene algún significado especial el que Cristo fuera crucificado y no muriera de otra manera?",
         "Sí, porque por eso estoy cierto de que Él tomó sobre sí la maldición que pesaba sobre mí; pues la muerte en cruz era maldita de Dios.",
         "La crucifixión no fue un accidente sino un cumplimiento profético. Deuteronomio 21:23 declara: 'Maldito todo el que es colgado en un madero'. Cristo eligió esta muerte específica para tomar sobre sí nuestra maldición. Gálatas 3:13 lo confirma: 'Cristo nos redimió de la maldición de la ley, hecho por nosotros maldición'. La cruz no fue solo un instrumento de tortura; fue el lugar donde la maldición fue transferida de nosotros a Cristo. Cada vez que veas una cruz, recuerda: la maldición que era tuya fue llevada por Él."),

        (40, 16,
         "¿Por qué fue necesario que Cristo se humillara hasta la muerte?",
         "Porque la justicia y la verdad de Dios exigían que solamente la muerte del Hijo de Dios pagase nuestros pecados.",
         "La muerte de Cristo fue una necesidad teológica, no un accidente histórico. La justicia de Dios exigía muerte como pago por el pecado. Y no cualquier muerte, sino la muerte del Hijo de Dios. Ningún otro pago era suficiente. Esto nos muestra la gravedad del pecado: costó la vida del Hijo de Dios. Y nos muestra la profundidad del amor divino: Dios estuvo dispuesto a pagar ese precio por nosotros. La cruz revela simultáneamente lo terrible del pecado y lo maravilloso del amor de Dios."),

        (41, 16,
         "¿Por qué fue también sepultado?",
         "Para testificar con esto que de veras había muerto.",
         "La sepultura de Cristo confirma la realidad de su muerte. No se desmayó, no fingió: murió verdaderamente. Esto es importante porque si no murió realmente, tampoco resucitó realmente, y nuestra fe sería vana. La tumba de Cristo es el testigo silencioso de que el precio fue pagado completamente. Pero la tumba vacía es el testigo glorioso de que la muerte no tuvo la última palabra. Cristo entró en la tumba como nuestro representante y salió victorioso. Su sepultura fue real, pero fue temporal. La muerte no pudo retenerlo."),

        (42, 16,
         "Puesto que Cristo ha muerto por nosotros, ¿por qué hemos de morir también nosotros?",
         "Nuestra muerte no es una satisfacción por nuestros pecados, sino solamente una abolición del pecado y un tránsito a la vida eterna.",
         "La muerte física del creyente ya no es un castigo sino una transición. Cristo pagó completamente por nuestros pecados, así que nuestra muerte ya no es pago por ellos. Es más bien la puerta de entrada a la vida eterna, el momento en que somos liberados completamente del pecado. Para el creyente, morir es ganancia (Filipenses 1:21). La muerte ha perdido su aguijón. Ya no debemos temerla como castigo, sino verla como el último paso hacia la gloria. Cristo transformó nuestra peor enemiga en una sirvienta que nos conduce a casa."),

        (43, 16,
         "¿Qué otro beneficio recibimos del sacrificio y muerte de Cristo en la cruz?",
         "Que por virtud de ella nuestra vieja naturaleza es crucificada, muerta y sepultada con Él, para que las malas concupiscencias de la carne no reinen más en nosotros, sino que nos ofrezcamos a Él en sacrificio de gratitud.",
         "La muerte de Cristo no solo nos libra de la culpa del pecado sino también de su poder. Nuestra vieja naturaleza fue crucificada con Cristo (Romanos 6:6). Esto significa que el pecado ya no tiene dominio sobre nosotros. No somos esclavos del pecado; somos libres para vivir en gratitud. La santificación fluye de la cruz. Porque hemos muerto con Cristo, podemos vivir para Cristo. La lucha contra el pecado no la peleamos solos ni con nuestras fuerzas; la peleamos desde la victoria que Cristo ya ganó en la cruz."),

        (44, 17,
         "¿Por qué se añade: descendió a los infiernos?",
         "Para que en mis mayores tentaciones yo tenga la certeza y el consuelo de que mi Señor Jesucristo, por medio de sus inefables angustias, dolores, terrores y agonías infernales, en los cuales se sumió durante toda su pasión, pero especialmente en la cruz, me ha librado de las angustias y tormentos del infierno.",
         "El descenso a los infiernos se refiere a los sufrimientos infernales que Cristo experimentó, especialmente en la cruz. Cuando clamó '¡Dios mío, por qué me has desamparado?', estaba experimentando el infierno en nuestro lugar: la separación de Dios. Esto nos da consuelo inmenso: Cristo sufrió el infierno para que nosotros nunca tengamos que sufrirlo. En nuestras mayores angustias y tentaciones, podemos recordar que Cristo ya pasó por lo peor imaginable por nosotros. No hay profundidad a la que puedas caer donde Cristo no haya estado primero."),

        (45, 17,
         "¿De qué nos sirve la resurrección de Cristo?",
         "Primero, por su resurrección ha vencido a la muerte, para hacernos partícipes de la justicia que Él nos ganó con su muerte. Segundo, por su poder somos ahora resucitados a una nueva vida. Tercero, la resurrección de Cristo es una garantía segura de nuestra gloriosa resurrección.",
         "La resurrección de Cristo tiene tres beneficios gloriosos. Primero, confirma que su sacrificio fue aceptado: la deuda fue pagada y la muerte fue vencida. Segundo, nos da poder para vivir una vida nueva ahora mismo. No tenemos que esperar al cielo para experimentar el poder de la resurrección; obra en nosotros hoy. Tercero, garantiza nuestra propia resurrección futura. Porque Él vive, nosotros viviremos también. La resurrección no es solo un evento pasado; es una realidad presente y una promesa futura. ¡Cristo ha resucitado! ¡Y nosotros resucitaremos con Él!"),

        (46, 18,
         "¿Qué entiendes por: subió a los cielos?",
         "Que Cristo, a la vista de sus discípulos, fue levantado de la tierra al cielo, y que está allí para nuestro bien hasta que vuelva otra vez a juzgar a los vivos y a los muertos.",
         "La ascensión de Cristo no fue una partida sino una entronización. Subió al cielo para sentarse en el trono como Rey del universo. Y está allí para nuestro bien, no para alejarse de nosotros. Desde el cielo, intercede por nosotros, gobierna sobre todas las cosas, y prepara lugar para nosotros. Además, envió al Espíritu Santo en su lugar. La ascensión es una victoria: nuestro representante humano está en el trono del universo. Donde Él está, allí estaremos nosotros también. La ascensión es la garantía de nuestro futuro glorioso."),

        (47, 18,
         "¿No está Cristo con nosotros hasta el fin del mundo, como nos lo ha prometido?",
         "Cristo es verdadero hombre y verdadero Dios; según su naturaleza humana no está ahora en la tierra; mas según su divinidad, majestad, gracia y Espíritu, en ningún momento se ausenta de nosotros.",
         "Esta pregunta aborda una aparente contradicción: si Cristo subió al cielo, ¿cómo puede estar con nosotros? La respuesta distingue entre sus dos naturalezas. Según su humanidad, está en el cielo. Según su divinidad, está omnipresente. Por su Espíritu, habita en cada creyente. Nunca estamos solos. Cristo está tan cerca de ti ahora como lo estuvo de sus discípulos en Galilea. Su presencia espiritual es real, poderosa y constante. No la vemos con los ojos, pero la experimentamos por la fe. Él prometió: 'Estaré con vosotros todos los días'."),

        (48, 18,
         "Pero si la naturaleza humana no está presente dondequiera que está la divina, ¿no se separan así las dos naturalezas de Cristo?",
         "De ninguna manera; porque la divinidad es incomprensible y omnipresente, y por tanto es necesario que esté fuera de los límites de la naturaleza humana que asumió, y sin embargo, no deja por eso de estar en ella; puesto que la divinidad no puede ser limitada por nada.",
         "Esta pregunta teológica profunda trata sobre la unión de las dos naturalezas de Cristo. Aunque su humanidad está localizada en el cielo, su divinidad es omnipresente. Esto no significa que las naturalezas estén separadas; están unidas en una persona. La divinidad de Cristo no está limitada por su humanidad. Este misterio supera nuestra comprensión pero nos da confianza: el Cristo que está a la diestra del Padre es el mismo que habita en nuestros corazones por su Espíritu. No hay contradicción, solo misterio glorioso."),

        (49, 19,
         "¿De qué nos sirve la ascensión de Cristo al cielo?",
         "Primero, que es nuestro Abogado ante la presencia de su Padre en los cielos. Segundo, que tenemos nuestra carne en el cielo como una prenda segura de que Él, como Cabeza nuestra, también nos llevará a sí, como miembros suyos. Tercero, que nos envía su Espíritu como prenda de garantía, por cuyo poder buscamos las cosas de arriba donde está Cristo sentado a la diestra de Dios, y no las de la tierra.",
         "La ascensión nos beneficia de tres maneras maravillosas. Primero, Cristo intercede por nosotros ante el Padre. Tenemos un Abogado en la corte celestial. Segundo, nuestra naturaleza humana ya está en el cielo en Cristo, como garantía de que nosotros también llegaremos allí. Tercero, desde el cielo envió al Espíritu Santo para que nuestros corazones busquen las cosas celestiales. La ascensión no es una pérdida sino una ganancia. Cristo en el cielo es mejor para nosotros que Cristo en la tierra, porque desde allí derrama sus beneficios sobre toda la iglesia."),

        (50, 19,
         "¿Por qué se añade: y está sentado a la diestra de Dios?",
         "Porque Cristo subió al cielo para manifestarse allí como Cabeza de su Iglesia cristiana, por medio de quien el Padre gobierna todas las cosas.",
         "Estar sentado a la diestra de Dios significa ocupar el lugar de máximo poder y autoridad. Cristo no está pasivo en el cielo; está gobernando activamente como Cabeza de la Iglesia. Todas las cosas están bajo sus pies. Él dirige la historia, protege a su iglesia y gobierna sobre todo el universo. Cuando el mundo parece fuera de control, recuerda: Cristo está sentado en el trono. Nada escapa a su gobierno. Los reyes de la tierra son sus siervos, los eventos de la historia cumplen sus propósitos. Tu Rey reina, y reinará hasta que todos sus enemigos sean puestos por estrado de sus pies."),

        (51, 19,
         "¿De qué nos sirve esta gloria de Cristo, nuestra Cabeza?",
         "Primero, que por su Espíritu Santo derrama dones celestiales en nosotros, sus miembros. Segundo, que por su poder nos defiende y guarda contra todos los enemigos.",
         "Cristo glorificado es Cristo activo a nuestro favor. Desde su trono celestial, derrama dones espirituales sobre su iglesia: dones de enseñanza, servicio, liderazgo, misericordia y muchos más. Y con su poder infinito nos defiende contra todo enemigo: Satanás, el mundo y nuestra propia carne. No estamos indefensos en la batalla espiritual; tenemos un Rey todopoderoso que pelea por nosotros. Cada don que tienes viene de Cristo glorificado. Cada victoria que experimentas es por su poder. Vive hoy con la confianza de que tu Cabeza celestial cuida de ti."),

        (52, 19,
         "¿Qué consuelo te da la venida de Cristo para juzgar a los vivos y a los muertos?",
         "Que en todas mis tribulaciones y persecuciones espero, con la cabeza erguida, a Aquel mismo que antes se puso ante el tribunal de Dios por mí y quitó de mí toda maldición, como Juez del cielo; el cual echará a todos sus enemigos y los míos en la condenación eterna, y a mí, con todos los escogidos, me llevará consigo a los gozos y la gloria celestial.",
         "El juicio final no es motivo de temor para el creyente, sino de consuelo. El Juez que viene es el mismo Salvador que murió por nosotros. No nos condenará; nos vindicará. Toda injusticia será corregida, todo mal será juzgado, y nosotros seremos llevados a la gloria eterna. En medio de las tribulaciones, levanta la cabeza: tu redención se acerca. El mundo que ahora parece dominado por el mal será transformado cuando Cristo vuelva. Esperamos con gozo al Juez que es nuestro Abogado, al Rey que es nuestro Salvador."),

        # Domingos sobre el Espíritu Santo
        (53, 20,
         "¿Qué crees del Espíritu Santo?",
         "Primero, que es, juntamente con el Padre y el Hijo, verdadero y eterno Dios. Segundo, que me ha sido dado a mí, para hacerme partícipe de Cristo y de todos sus beneficios por la verdadera fe, para consolarme, y para permanecer conmigo eternamente.",
         "El Espíritu Santo no es una fuerza impersonal sino la tercera persona de la Trinidad, verdadero Dios junto con el Padre y el Hijo. Y este Dios habita en cada creyente. Su obra es unirnos a Cristo, aplicar en nosotros los beneficios de la redención, consolarnos en las aflicciones, y permanecer con nosotros para siempre. El Espíritu Santo es el regalo de Dios que hace real en nuestra experiencia todo lo que Cristo ganó para nosotros. Sin Él, la obra de Cristo quedaría fuera de nosotros. Por Él, la obra de Cristo vive en nosotros."),

        (54, 21,
         "¿Qué crees de la santa Iglesia universal de Cristo?",
         "Que el Hijo de Dios, desde el principio hasta el fin del mundo, congrega, defiende y conserva para sí, por su Espíritu y su Palabra, en la unidad de la verdadera fe, una comunidad escogida para la vida eterna; y que yo soy un miembro vivo de ella y lo seré eternamente.",
         "La Iglesia no es una institución humana sino la obra del Hijo de Dios. Cristo mismo congrega, defiende y conserva a su pueblo. La Iglesia es eterna, universal y está unida por la verdadera fe. Y lo más personal: yo soy miembro vivo de ella. Pertenecer a la Iglesia no es opcional para el creyente; es parte de lo que significa ser cristiano. Fuimos salvados para una comunidad, no para el aislamiento. Valora tu iglesia local, participa activamente, y recuerda que eres parte de algo mucho más grande que tú mismo: el cuerpo de Cristo."),

        (55, 22,
         "¿Qué entiendes por la comunión de los santos?",
         "Primero, que todos y cada uno de los creyentes, como miembros de Cristo, participan de Él y de todos sus tesoros y dones. Segundo, que cada uno debe sentirse obligado a emplear sus dones, con buena voluntad y gozo, en beneficio y salvación de los demás miembros.",
         "La comunión de los santos tiene dos dimensiones: vertical y horizontal. Verticalmente, compartimos en Cristo y todos sus beneficios. Horizontalmente, compartimos nuestros dones unos con otros. No somos individuos aislados sino un cuerpo interconectado. Tus dones son para servir a otros, y los dones de otros son para tu beneficio. Esta mutualidad es la belleza de la iglesia. Hoy, piensa en cómo puedes usar tus talentos, recursos y tiempo para bendecir a otros creyentes. La vida cristiana no se vive en solitario sino en comunidad."),

        (56, 22,
         "¿Qué crees del perdón de los pecados?",
         "Que Dios, por la satisfacción de Cristo, no quiere acordarse jamás de mis pecados ni de mi naturaleza pecaminosa, contra la cual tengo que luchar toda mi vida; sino que por gracia me imputa la justicia de Cristo, para que yo nunca sea condenado.",
         "El perdón de Dios es completo y permanente. No solo olvida nuestros pecados individuales sino también nuestra naturaleza pecaminosa. Y en lugar de nuestro pecado, nos imputa la justicia perfecta de Cristo. Esto significa que ante Dios, somos tan justos como Cristo mismo. No por nuestros méritos sino por los de Él. Este perdón nos libra de toda condenación, pasada, presente y futura. Cuando el diablo te acuse, recuerda: Dios no quiere acordarse de tus pecados. Estás vestido con la justicia de Cristo. Eres perdonado, aceptado y amado."),

        (57, 22,
         "¿Qué consuelo te da la resurrección de la carne?",
         "Que no solamente mi alma será llevada después de esta vida, sin dilación, a Cristo, su Cabeza; sino que también esta mi carne, resucitada por el poder de Cristo, será de nuevo unida a mi alma y hecha conforme al cuerpo glorioso de Cristo.",
         "La esperanza cristiana no es una existencia incorpórea en las nubes. Es una resurrección física, corporal. Nuestros cuerpos serán transformados y glorificados, hechos semejantes al cuerpo resucitado de Cristo. Esto significa que la materia importa, que nuestros cuerpos importan. Dios no nos salvó para descartarnos sino para renovarnos completamente: alma y cuerpo. La resurrección de la carne es la esperanza final que le da sentido a todo nuestro sufrimiento presente. Este cuerpo que ahora sufre será glorificado. ¡Qué esperanza tan gloriosa!"),

        (58, 22,
         "¿Qué consuelo te da el artículo de la vida eterna?",
         "Que puesto que yo siento ya en mi corazón el principio del gozo eterno, después de esta vida poseeré una bienaventuranza perfecta, cual ojo no vio, ni oído oyó, ni ha subido en corazón de hombre para alabar en ella a Dios eternamente.",
         "La vida eterna no comienza cuando morimos; ya ha comenzado. En nuestro corazón ya sentimos el principio del gozo eterno. Cada momento de adoración, cada experiencia de la gracia, cada destello de la gloria de Dios es un anticipo del cielo. Pero lo que viene será inmensamente mejor: una bienaventuranza que no podemos ni imaginar. Ojo no vio, oído no oyó lo que Dios tiene preparado. Esta esperanza nos sostiene en las dificultades presentes y nos motiva a vivir para la gloria de Dios. Lo mejor está por venir. Siempre."),

        # Sobre la justificación por la fe
        (59, 23,
         "¿De qué te sirve creer todo esto?",
         "De que soy justo en Cristo, delante de Dios, y heredero de la vida eterna.",
         "Creer las verdades del evangelio no es un ejercicio intelectual vacío. Tiene consecuencias eternas. Por la fe somos declarados justos ante Dios y nos convertimos en herederos de la vida eterna. La fe nos une a Cristo y todo lo que es de Él se vuelve nuestro. Su justicia se convierte en nuestra justicia. Su herencia se convierte en nuestra herencia. La fe es el instrumento que recibe todas las riquezas de Cristo. No es la fe misma lo que nos salva, sino Cristo a quien la fe se aferra. Hoy, regocíjate: por la fe, eres justo ante Dios y heredero de la vida eterna."),

        (60, 23,
         "¿Cómo eres justo delante de Dios?",
         "Solo por la verdadera fe en Jesucristo; de tal manera que, aunque mi conciencia me acuse de haber pecado gravemente contra todos los mandamientos de Dios, y de no haber guardado ninguno de ellos, y de estar aún inclinado a todo mal, sin embargo, Dios, sin ningún mérito mío, por pura gracia, me concede y atribuye la perfecta satisfacción, justicia y santidad de Cristo, como si nunca hubiera cometido ni tenido pecado alguno, y como si yo mismo hubiera cumplido toda la obediencia que Cristo cumplió por mí; con tal de que yo acepte esta gracia con corazón creyente.",
         "Esta es quizás la respuesta más gloriosa de todo el catecismo. Resume la doctrina de la justificación por la fe sola. A pesar de todos nuestros pecados, Dios nos declara justos basándose únicamente en la obra de Cristo. Su satisfacción se nos atribuye como si fuera nuestra. Su obediencia se nos acredita como si nosotros la hubiéramos cumplido. Esto es pura gracia, inmerecida e incondicional. Cuando tu conciencia te acuse, recuerda estas palabras. No eres justo por lo que haces sino por lo que Cristo hizo por ti. Descansa en esta verdad."),

        (61, 23,
         "¿Por qué dices que eres justo solo por la fe?",
         "No porque yo agrade a Dios en virtud de la dignidad de mi fe, sino porque solo la satisfacción, justicia y santidad de Cristo es mi justicia delante de Dios; y porque yo no puedo recibirla ni aplicármela de otro modo que por la sola fe.",
         "La fe no tiene mérito en sí misma. No somos salvos por la calidad de nuestra fe sino por la calidad de nuestro Salvador. La fe es simplemente la mano vacía que recibe el regalo de Cristo. Un mendigo que recibe una moneda de oro no se enriquece por la habilidad de su mano sino por el valor de la moneda. Así, no somos justos por la dignidad de nuestra fe sino por la dignidad de Cristo. La fe es solo el instrumento, Cristo es el fundamento. Esto nos libra de la ansiedad de preguntarnos si tenemos suficiente fe. Mira a Cristo, no a tu fe."),

        # Sobre los sacramentos
        (62, 24,
         "¿Por qué nuestras buenas obras no pueden ser nuestra justicia delante de Dios, ni una parte de ella?",
         "Porque la justicia que puede subsistir ante el juicio de Dios ha de ser absolutamente perfecta y del todo conforme a la Ley de Dios; y aun nuestras mejores obras en esta vida son todas imperfectas y manchadas de pecado.",
         "Nuestras mejores obras están manchadas de pecado. Incluso nuestros actos más nobles llevan mezcla de motivos impuros, orgullo y egoísmo. Por eso no pueden ser la base de nuestra justificación. La justicia que Dios requiere es absoluta perfección, y eso solo se encuentra en Cristo. Esto no significa que las buenas obras no importan; son fruto de la gratitud y evidencia de la fe genuina. Pero nunca son la base de nuestra aceptación ante Dios. Somos aceptados por Cristo y solo por Cristo. Las obras fluyen de la salvación, no la producen."),

        (63, 24,
         "¿No merecen nuestras buenas obras nada, aunque es la voluntad de Dios recompensarlas en esta vida y en la futura?",
         "Esta recompensa no se da por mérito, sino por gracia.",
         "Dios promete recompensar las buenas obras de sus hijos, pero esta recompensa es de gracia, no de mérito. Incluso cuando Dios corona nuestras obras, está coronando sus propios dones en nosotros. Las buenas obras que hacemos son posibles solo porque el Espíritu Santo obra en nosotros. Así que toda la gloria regresa a Dios. La gracia es el principio, el medio y el fin de nuestra salvación. No hay espacio para el orgullo humano en el plan de Dios. Todo es gracia: desde la fe que recibimos hasta las recompensas que disfrutaremos."),

        (64, 24,
         "¿No hace esta doctrina a los hombres impíos y negligentes?",
         "No, porque es imposible que los que son injertados en Cristo por la verdadera fe no produzcan frutos de gratitud.",
         "Esta es la objeción clásica contra la justificación por la fe sola: si somos salvos solo por fe, ¿para qué ser buenos? La respuesta es contundente: la verdadera fe siempre produce frutos. Un árbol vivo no puede dejar de dar fruto. Si alguien dice tener fe pero no produce obras, su fe no es genuina. La fe y las obras son inseparables, aunque tienen funciones diferentes. La fe justifica, las obras evidencian. La fe nos salva, las obras demuestran que hemos sido salvados. La gracia no produce pereza sino gratitud activa."),

        (65, 25,
         "Si solo la fe nos hace participantes de Cristo y de todos sus beneficios, ¿de dónde procede esta fe?",
         "Del Espíritu Santo, el cual la produce en nuestros corazones por la predicación del santo Evangelio, y la confirma por el uso de los santos sacramentos.",
         "La fe no es algo que producimos por nuestro propio esfuerzo. Es un don del Espíritu Santo. Él usa dos medios principales para crear y fortalecer nuestra fe: la predicación del evangelio y los sacramentos. Por eso la asistencia a la iglesia, la escucha de la Palabra predicada y la participación en los sacramentos son tan importantes. Son los medios que Dios ha establecido para alimentar nuestra fe. No los descuides. La fe viene por el oír, y el oír por la Palabra de Dios. Acude fielmente a los medios de gracia que Dios ha provisto."),

        (66, 25,
         "¿Qué son los sacramentos?",
         "Son señales y sellos sagrados visibles, instituidos por Dios para que, por medio de ellos, nos haga entender más claramente y nos confirme la promesa del Evangelio, a saber: que Él nos concede gratuitamente la remisión de los pecados y la vida eterna por causa del único sacrificio de Cristo cumplido en la cruz.",
         "Los sacramentos son ayudas visuales que Dios nos dio para fortalecer nuestra fe. Así como la predicación llega a nuestros oídos, los sacramentos llegan a nuestros ojos y a nuestro cuerpo. Son señales que representan las promesas del evangelio y sellos que las confirman. No añaden nada a la obra de Cristo, pero nos ayudan a comprenderla y apropiárnosla. El agua del bautismo y el pan y vino de la Cena nos recuerdan tangiblemente que Cristo murió por nosotros. Dios conoce nuestra debilidad y nos da estos medios para fortalecer nuestra fe vacilante."),

        (67, 25,
         "¿Están, pues, instituidos la Palabra y los sacramentos para dirigir nuestra fe al sacrificio de Jesucristo en la cruz como el único fundamento de nuestra salvación?",
         "Sí, ciertamente; pues el Espíritu Santo enseña en el Evangelio y nos confirma por los santos sacramentos que toda nuestra salvación se funda en el único sacrificio de Cristo ofrecido por nosotros en la cruz.",
         "Todo en la vida cristiana apunta a una sola dirección: Cristo crucificado. La predicación, los sacramentos, toda la liturgia de la iglesia tiene un solo objetivo: dirigir nuestra fe a la cruz. No hay otro fundamento, no hay otra fuente de salvación. Los sacramentos no son fines en sí mismos sino medios que nos señalan a Cristo. Cuando participas del bautismo o la Santa Cena, no mires el agua, el pan o el vino como si tuvieran poder en sí mismos. Mira a través de ellos hacia Cristo y su sacrificio. Él es el verdadero fundamento."),

        # Sobre el Bautismo
        (68, 26,
         "¿Cuántos sacramentos ha instituido Cristo en el Nuevo Testamento?",
         "Dos: el santo Bautismo y la santa Cena.",
         "Cristo instituyó solo dos sacramentos. No tres, no siete, sino dos. El bautismo marca nuestra entrada en la comunidad del pacto, y la Santa Cena nos alimenta continuamente en la fe. Ambos fueron instituidos directamente por Cristo y están claramente registrados en las Escrituras. La sencillez de los sacramentos refleja la sencillez del evangelio: agua, pan y vino, elementos comunes que se convierten en medios extraordinarios de gracia. No necesitamos rituales complicados; necesitamos fe sencilla en las promesas de Cristo."),

        (69, 26,
         "¿Cómo te recuerda y asegura el santo Bautismo que el único sacrificio de Cristo en la cruz te aprovecha?",
         "De esta manera: que Cristo ha instituido el lavamiento exterior con agua, y ha prometido que yo soy lavado con su sangre y Espíritu de la suciedad de mi alma, es decir, de todos mis pecados, tan ciertamente como soy lavado exteriormente con el agua, que suele usarse para quitar la suciedad del cuerpo.",
         "El bautismo es una imagen visible de una realidad invisible. Así como el agua limpia el cuerpo, la sangre de Cristo limpia el alma. La conexión es directa y personal: tan ciertamente como el agua toca tu cuerpo, la sangre de Cristo toca tu alma. El bautismo no salva en sí mismo, pero es la promesa visible de Dios de que en Cristo somos completamente limpios. Cada vez que recuerdes tu bautismo, recuerda la promesa: tus pecados han sido lavados por la sangre de Cristo. Eres limpio ante Dios."),

        (70, 26,
         "¿Qué significa ser lavado con la sangre y el Espíritu de Cristo?",
         "Significa recibir de Dios la remisión de los pecados por gracia, por causa de la sangre de Cristo, que Él derramó por nosotros en su sacrificio de la cruz; y también ser renovados por el Espíritu Santo y santificados como miembros de Cristo, para que más y más muramos al pecado y vivamos santa e irreprensiblemente.",
         "El lavamiento espiritual tiene dos aspectos: perdón y renovación. La sangre de Cristo nos perdona; el Espíritu Santo nos renueva. No solo somos declarados inocentes sino que somos transformados internamente. El perdón trata con la culpa del pecado; la santificación trata con el poder del pecado. Ambos son necesarios y ambos son dones de Dios. Día a día, el Espíritu nos capacita para morir más al pecado y vivir más para Dios. La vida cristiana es un proceso continuo de renovación. No te desanimes por la lentitud del progreso; confía en que Dios completará la obra que comenzó en ti."),

        (71, 27,
         "¿Dónde nos ha prometido Cristo que nos lavará con su sangre y su Espíritu tan ciertamente como somos lavados con el agua del Bautismo?",
         "En la institución del Bautismo, donde dice: Id, pues, y haced discípulos a todas las naciones, bautizándolos en el nombre del Padre, y del Hijo, y del Espíritu Santo. El que creyere y fuere bautizado, será salvo; mas el que no creyere, será condenado. Esta promesa se repite donde la Escritura llama al Bautismo el lavamiento de la regeneración y la limpieza de los pecados.",
         "Las promesas del bautismo están firmemente arraigadas en las palabras de Cristo mismo y en las Escrituras. No son invenciones humanas sino mandatos y promesas divinas. La fórmula trinitaria del bautismo nos recuerda que las tres personas de la Divinidad están involucradas en nuestra salvación. El bautismo es la señal visible de pertenecer a este Dios trino. Cuando dudas de tu salvación, recuerda las promesas conectadas a tu bautismo: eres lavado, renovado y adoptado en la familia de Dios."),

        # Sobre la Santa Cena
        (72, 27,
         "¿Es entonces el lavamiento exterior con agua el lavamiento mismo de los pecados?",
         "No; pues solo la sangre de Jesucristo y el Espíritu Santo nos limpian de todo pecado.",
         "El agua del bautismo no tiene poder mágico para perdonar pecados. Solo la sangre de Cristo limpia y solo el Espíritu Santo regenera. El bautismo es la señal, no la realidad misma. Confundir la señal con lo señalado es un error grave. El agua apunta a Cristo; no es un sustituto de Cristo. Esta distinción nos protege tanto de la superstición (creer que el agua salva) como del desprecio (creer que el bautismo no importa). Los sacramentos son importantes precisamente porque señalan a Cristo, pero nunca reemplazan la fe personal en Él."),

        (73, 27,
         "¿Por qué llama el Espíritu Santo al Bautismo el lavamiento de la regeneración y la limpieza de los pecados?",
         "Dios no nos habla así sin causa importante; porque no solo quiere enseñarnos con esto que así como la suciedad del cuerpo se limpia con el agua, así nuestros pecados son limpiados por la sangre y el Espíritu de Cristo; sino que con mayor razón quiere asegurarnos, por esta señal y prenda divinas, que somos tan verdaderamente lavados de nuestros pecados espiritualmente, como lo somos corporalmente con el agua.",
         "Dios usa un lenguaje fuerte sobre el bautismo porque quiere que tomemos en serio sus promesas. Cuando la Escritura llama al bautismo lavamiento de regeneración, está usando la señal para referirse a la realidad que representa. Es un lenguaje sacramental que conecta firmemente la señal visible con la gracia invisible. Dios quiere que estemos tan seguros de nuestro lavamiento espiritual como estamos seguros de que el agua moja. Su intención es fortalecer nuestra fe débil con promesas tangibles y visibles."),

        (74, 27,
         "¿Se ha de bautizar también a los niños pequeños?",
         "Sí, porque están comprendidos, así como los adultos, en el pacto y en la Iglesia de Dios, y tanto a ellos como a los adultos se les promete, por la sangre de Cristo, la remisión de los pecados y el Espíritu Santo, que obra la fe. Por eso, por medio del Bautismo, como señal del pacto, deben ser incorporados en la Iglesia cristiana y diferenciados de los hijos de los incrédulos, como se hacía en el Antiguo Testamento por la circuncisión, en cuyo lugar ha sido instituido el Bautismo en el Nuevo Testamento.",
         "El bautismo infantil se basa en la continuidad del pacto de gracia. Los hijos de creyentes pertenecen a la comunidad del pacto y deben recibir su señal. Así como los niños israelitas eran circuncidados, los hijos de la iglesia son bautizados. Esto no significa que el bautismo salve automáticamente a los niños, sino que los marca como miembros de la comunidad del pacto y les aplica las promesas de Dios. Los padres creyentes tienen la responsabilidad de criar a sus hijos bautizados en la fe, enseñándoles a apropiarse personalmente de las promesas de su bautismo."),

        (75, 28,
         "¿Cómo te recuerda y asegura la santa Cena que participas de aquel único sacrificio de Cristo en la cruz y de todos sus beneficios?",
         "De esta manera: que Cristo me ha mandado, a mí y a todos los creyentes, comer de este pan partido y beber de esta copa en memoria suya, y le ha unido estas promesas: primera, que su cuerpo fue ofrecido y partido en la cruz por mí y su sangre derramada por mí, tan ciertamente como veo con mis ojos que el pan del Señor es partido para mí y la copa me es comunicada; segunda, que Él mismo alimenta y sustenta mi alma para la vida eterna con su cuerpo crucificado y su sangre derramada, tan ciertamente como recibo de mano del ministro y gusto con mi boca el pan y la copa del Señor, que me son dados como señales seguras del cuerpo y de la sangre de Cristo.",
         "La Santa Cena es una experiencia multisensorial del evangelio. Vemos el pan partido, simbolizando el cuerpo de Cristo quebrantado. Bebemos el vino, simbolizando su sangre derramada. Y la promesa es personal: así como el pan alimenta tu cuerpo, Cristo alimenta tu alma. La Cena no es un mero recuerdo intelectual; es una participación real en los beneficios de Cristo por medio de la fe. Cada vez que participas, estás siendo espiritualmente alimentado y fortalecido. No tomes la Cena mecánicamente; tómala con fe, meditando en lo que Cristo hizo por ti."),

        (76, 28,
         "¿Qué significa comer el cuerpo crucificado de Cristo y beber su sangre derramada?",
         "No solo es abrazar con el corazón creyente todo el sufrimiento y muerte de Cristo y alcanzar así el perdón de los pecados y la vida eterna; sino también ir uniéndose más y más a su sagrado cuerpo por el Espíritu Santo, que habita en Cristo y en nosotros al mismo tiempo; de tal manera que, aunque Cristo está en el cielo y nosotros en la tierra, somos, sin embargo, carne de su carne y hueso de sus huesos, y vivimos y somos gobernados eternamente por un solo Espíritu, como los miembros de un cuerpo lo son por una misma alma.",
         "Comer y beber espiritualmente a Cristo significa dos cosas: recibir perdón y crecer en unión con Él. Por la fe, nos apropiamos de todo lo que Cristo sufrió por nosotros. Y por el Espíritu Santo, nuestra unión con Cristo se profundiza continuamente. Aunque Él está en el cielo y nosotros en la tierra, estamos unidos a Él de manera real y viva. Somos carne de su carne. Esta unión mística con Cristo es la realidad más profunda de la vida cristiana. En la Santa Cena, esta unión se celebra, se experimenta y se fortalece."),

        (77, 28,
         "¿Dónde ha prometido Cristo que quiere alimentar y sustentar a los creyentes con su cuerpo y sangre, tan ciertamente como ellos comen de este pan partido y beben de esta copa?",
         "En la institución de la Cena, donde dice: El Señor Jesús, la noche que fue entregado, tomó pan; y habiendo dado gracias, lo partió, y dijo: Tomad, comed; esto es mi cuerpo que por vosotros es partido; haced esto en memoria de mí. Asimismo tomó también la copa, después de haber cenado, diciendo: Esta copa es el nuevo pacto en mi sangre; haced esto todas las veces que la bebiereis, en memoria de mí. Porque todas las veces que comiereis este pan, y bebiereis esta copa, la muerte del Señor anunciáis hasta que Él venga. Esta promesa se repite por el apóstol Pablo donde dice: La copa de bendición que bendecimos, ¿no es la comunión de la sangre de Cristo? El pan que partimos, ¿no es la comunión del cuerpo de Cristo? Siendo uno solo el pan, nosotros, con ser muchos, somos un cuerpo; pues todos participamos de aquel mismo pan.",
         "Las palabras de institución de la Santa Cena vienen directamente de Cristo. No son tradición humana sino mandato divino. Cristo mismo estableció esta ceremonia y le dio su significado. Las palabras 'haced esto en memoria de mí' son un mandato perpetuo para la iglesia. Y Pablo añade que la Cena es verdadera comunión con Cristo y entre los creyentes. Cuando tomamos el pan, participamos del cuerpo de Cristo. Cuando bebemos la copa, participamos de su sangre. Y al hacerlo juntos, declaramos que somos un solo cuerpo en Él."),

        (78, 28,
         "¿Se convierten el pan y el vino en el verdadero cuerpo y sangre de Cristo?",
         "No; así como el agua del Bautismo no se convierte en la sangre de Cristo ni es el lavamiento mismo de los pecados, sino que es solamente una señal y garantía divinas de estas cosas, así también el pan sagrado de la Cena no se convierte en el cuerpo de Cristo, aunque es llamado el cuerpo de Cristo conforme a la naturaleza y uso de los sacramentos.",
         "La posición reformada rechaza la transubstanciación. El pan sigue siendo pan y el vino sigue siendo vino. Pero no son pan y vino comunes; son señales sagradas que nos conectan espiritualmente con Cristo. Cuando Cristo dijo 'esto es mi cuerpo', usó lenguaje figurativo, como cuando dijo 'yo soy la puerta' o 'yo soy la vid'. El poder de la Cena no está en una transformación mágica de los elementos sino en la promesa de Cristo de alimentarnos espiritualmente mientras comemos y bebemos por fe. La verdadera presencia de Cristo es espiritual, no física."),

        (79, 29,
         "¿Por qué, pues, llama Cristo al pan su cuerpo y a la copa su sangre, o el nuevo pacto en su sangre; y por qué dice San Pablo: la participación del cuerpo y de la sangre de Cristo?",
         "Cristo no habla así sin una razón importante: porque no solo quiere enseñarnos con ello que así como el pan y el vino sustentan esta vida temporal, así también su cuerpo crucificado y su sangre derramada son verdadera comida y bebida de nuestras almas para la vida eterna; sino que, mucho más, por estas señales visibles y prendas, nos quiere asegurar que somos verdaderamente participantes de su verdadero cuerpo y sangre por la operación del Espíritu Santo, como recibimos estas sagradas señales con la boca corporal en memoria suya; y que todo su sufrimiento y obediencia son tan ciertamente nuestros como si nosotros mismos en nuestras propias personas hubiéramos sufrido y dado satisfacción por nuestros pecados.",
         "El lenguaje sacramental es fuerte porque las realidades que señala son gloriosas. Cristo usa palabras tan directas porque quiere que estemos absolutamente seguros de que participamos verdaderamente de Él. No es un mero ejercicio de memoria sino una verdadera comunión espiritual. Por la obra del Espíritu Santo, mientras comemos el pan y bebemos el vino, somos alimentados con Cristo mismo. Su sufrimiento se vuelve nuestro, su obediencia se nos acredita. La Cena es un banquete de gracia donde nos alimentamos del Salvador. Acércate con hambre espiritual y serás saciado."),

        (80, 30,
         "¿Qué diferencia hay entre la Cena del Señor y la misa papal?",
         "La Cena del Señor nos testifica que tenemos perdón perfecto de todos nuestros pecados por el único sacrificio de Jesucristo, que Él mismo cumplió una sola vez en la cruz; y que por el Espíritu Santo somos injertados en Cristo, quien según su naturaleza humana no está ahora en la tierra sino en el cielo, a la diestra del Padre, y allí quiere ser adorado por nosotros. Pero la misa enseña que los vivos y los muertos no tienen el perdón de los pecados por el sufrimiento de Cristo, a menos que Cristo sea todavía ofrecido diariamente por ellos por los sacerdotes; y que Cristo está corporalmente presente bajo las formas de pan y vino, y que por tanto debe ser adorado en ellos. De modo que la misa no es en el fondo otra cosa que una negación del único sacrificio y sufrimiento de Jesucristo, y una idolatría condenable.",
         "Esta pregunta histórica marca una diferencia teológica fundamental entre la fe reformada y el catolicismo romano. El punto central es la suficiencia del sacrificio de Cristo. La fe reformada enseña que Cristo fue ofrecido una sola vez y para siempre (Hebreos 10:10). No necesita ser sacrificado de nuevo. La misa, al pretender repetir el sacrificio, implica que la cruz no fue suficiente. Además, adorar el pan y el vino como si fueran Cristo contradice el hecho de que su cuerpo humano está en el cielo. Estas diferencias no son menores; tocan el corazón del evangelio."),

        (81, 30,
         "¿Quiénes deben venir a la mesa del Señor?",
         "Los que están verdaderamente descontentos de sí mismos por sus pecados, y sin embargo confían en que estos les son perdonados y que sus restantes debilidades están cubiertas por el sufrimiento y muerte de Cristo; y que desean también cada vez más fortalecer su fe y enmendar su vida. Pero los hipócritas y los que no se arrepienten, comen y beben condenación para sí.",
         "La Santa Cena no es para perfectos sino para pecadores arrepentidos. Las tres marcas de quien debe acercarse a la mesa son: descontento con su pecado, confianza en el perdón de Cristo, y deseo de crecer en fe y santidad. No necesitas ser perfecto para participar; necesitas ser honesto ante Dios. Si te duele tu pecado, si confías en Cristo, y si deseas ser mejor, la mesa es para ti. Pero si te acercas sin arrepentimiento, comes y bebes juicio para ti mismo. Examínate antes de participar, pero no te quedes fuera si tu corazón busca a Cristo."),

        (82, 30,
         "¿Deben admitirse también a esta Cena los que con su confesión y su vida se muestran incrédulos e impíos?",
         "No; porque con eso se profana el pacto de Dios y se provoca su ira contra toda la congregación; por lo cual la Iglesia cristiana está obligada, según la ordenanza de Cristo y sus Apóstoles, a excluir a los tales por las llaves del reino de los cielos, hasta que enmienden sus vidas.",
         "La disciplina eclesiástica protege la santidad de los sacramentos y la integridad de la iglesia. Quienes viven en pecado abierto sin arrepentimiento no deben participar de la Cena, no porque la iglesia sea elitista, sino porque el amor genuino a veces requiere confrontación. La disciplina busca la restauración del pecador, no su destrucción. Y protege a la congregación de la falsa seguridad. Las llaves del reino que Cristo dio a la iglesia incluyen el poder de admitir y excluir de los sacramentos. Esto es una responsabilidad solemne que debe ejercerse con amor y sabiduría."),

        (83, 31,
         "¿Qué son las llaves del reino de los cielos?",
         "La predicación del santo Evangelio y la disciplina cristiana. Por ambas se abre el reino de los cielos a los creyentes y se cierra a los incrédulos.",
         "Las llaves del reino son la predicación y la disciplina. La predicación abre el cielo cuando anuncia el perdón a los que creen, y lo cierra cuando anuncia condenación a los que rechazan el evangelio. La disciplina abre cuando admite a los arrepentidos en la comunión de la iglesia, y cierra cuando excluye a los impenitentes. Estas llaves fueron dadas por Cristo a su iglesia. Son un poder solemne y una responsabilidad sagrada. La iglesia no inventa las condiciones de entrada al reino; simplemente anuncia las que Cristo estableció."),

        (84, 31,
         "¿Cómo se abre y se cierra el reino de los cielos por la predicación del santo Evangelio?",
         "Cuando, según el mandato de Cristo, se anuncia y se testifica públicamente a todos y cada uno de los creyentes que, cuantas veces acepten con verdadera fe la promesa del Evangelio, todos sus pecados les son verdaderamente perdonados por Dios, por los méritos de Cristo; y por el contrario, a todos los incrédulos y a los que no se arrepienten de corazón, se les anuncia y testifica que la ira de Dios y la condenación eterna pesan sobre ellos, mientras no se conviertan; según este testimonio del Evangelio quiere Dios juzgar, tanto en esta vida como en la venidera.",
         "La predicación del evangelio tiene poder de vida y muerte. Para los que creen, es aroma de vida para vida. Para los que rechazan, es aroma de muerte para muerte. El predicador no inventa este poder; lo recibe de Cristo. Cuando el evangelio es fielmente predicado, Dios mismo está abriendo y cerrando las puertas del reino. Esto le da una solemnidad tremenda a la predicación. No es entretenimiento ni mera educación; es el medio por el cual Dios salva y condena. Escucha la predicación con reverencia, porque a través de ella Dios te habla directamente."),

        (85, 31,
         "¿Cómo se abre y se cierra el reino de los cielos por la disciplina cristiana?",
         "Cuando, según el mandato de Cristo, los que bajo el nombre de cristianos mantienen doctrinas o conductas que no son cristianas, y no quieren abandonar sus errores y maldades después de haber sido amonestados repetidas veces, son acusados ante la Iglesia o ante quienes han sido nombrados por la Iglesia para ello; y si no hacen caso de la amonestación, son excluidos por estos de los sacramentos, y por Dios mismo del reino de Cristo; y si prometen y muestran verdadero arrepentimiento, son recibidos de nuevo como miembros de Cristo y de la Iglesia.",
         "La disciplina eclesiástica sigue el proceso que Cristo estableció en Mateo 18: primero amonestación privada, luego ante testigos, y finalmente ante la iglesia. El objetivo siempre es la restauración, no la venganza. Cuando alguien es excluido, es con la esperanza de que se arrepienta y vuelva. Y cuando se arrepiente, debe ser recibido con gozo y amor. Una iglesia sin disciplina es una iglesia sin amor verdadero, porque el amor confronta el pecado que destruye. La disciplina protege al pecador, a la iglesia y la honra de Cristo."),

        # === PARTE III: LA GRATITUD (Domingos 32-52) ===
        (86, 32,
         "Ya que hemos sido librados de nuestra miseria, por pura gracia, por medio de Cristo, sin mérito alguno de nuestra parte, ¿por qué debemos hacer buenas obras?",
         "Porque Cristo, después de habernos comprado y rescatado con su sangre, nos renueva también por su Espíritu Santo a su imagen, para que con toda nuestra vida nos mostremos agradecidos a Dios por sus beneficios, y Él sea glorificado por nosotros; además, para que cada uno pueda estar seguro de su fe por los frutos de ella, y para que por nuestra conducta piadosa ganemos a nuestros prójimos para Cristo.",
         "Aquí comienza la tercera parte del catecismo: la gratitud. Las buenas obras no son la causa de nuestra salvación sino la consecuencia. Hacemos el bien por tres razones: gratitud a Dios que nos salvó, evidencia de que nuestra fe es genuina, y testimonio para ganar a otros para Cristo. La motivación correcta para las buenas obras no es el miedo al castigo ni el deseo de ganar la salvación, sino el amor y la gratitud hacia quien nos salvó. Cuando entiendes cuánto te ha sido perdonado, la obediencia deja de ser una carga y se convierte en un gozo."),

        (87, 32,
         "¿No pueden, pues, salvarse los que, continuando en su vida perversa e ingrata, no se convierten a Dios?",
         "De ninguna manera; porque la Escritura dice que ni los deshonestos, ni los idólatras, ni los adúlteros, ni los ladrones, ni los avaros, ni los borrachos, ni los maldicientes, ni los rapaces, poseerán el reino de Dios.",
         "Esta advertencia es seria y necesaria. La gracia que salva también transforma. Si no hay transformación, debemos cuestionar si hubo verdadera salvación. Esto no significa que los creyentes sean perfectos, sino que hay un cambio de dirección en sus vidas. Quien continúa viviendo en pecado deliberado sin arrepentimiento no tiene evidencia de ser salvo. La fe genuina siempre produce frutos de santidad. Si tu vida no muestra ningún cambio desde que profesaste fe en Cristo, examínate seriamente. La gracia barata no salva; la gracia verdadera transforma."),

        # Los Diez Mandamientos
        (88, 33,
         "¿En cuántas partes consiste la verdadera conversión del hombre?",
         "En dos partes: la mortificación del viejo hombre y la vivificación del nuevo.",
         "La vida cristiana tiene un ritmo doble: morir y vivir. Morir al pecado y vivir para Dios. Mortificar los deseos carnales y avivar los espirituales. Este proceso es continuo; no termina hasta que Cristo vuelva. Cada día debemos crucificar nuestra vieja naturaleza y alimentar la nueva. No es un proceso pasivo sino activo. Requiere disciplina, oración, estudio bíblico y dependencia del Espíritu Santo. Pero no es un esfuerzo solitario; el Espíritu obra en nosotros lo que agrada a Dios. Cooperamos con la gracia que nos transforma."),

        (89, 33,
         "¿Qué es la mortificación del viejo hombre?",
         "Es un sincero dolor de corazón de haber ofendido a Dios con nuestros pecados, y un aborrecimiento y huida cada vez mayor de ellos.",
         "La mortificación no es simplemente dejar de pecar externamente. Es un dolor profundo por haber ofendido a Dios y un creciente aborrecimiento del pecado. No solo dejamos de hacer lo malo; aprendemos a odiarlo. Este cambio de actitud hacia el pecado es obra del Espíritu Santo en nosotros. Cuanto más conocemos a Dios, más aborrecemos lo que le ofende. La mortificación es una batalla diaria que no ganamos por fuerza de voluntad sino por el poder del Espíritu. Pídele a Dios que te dé un odio santo hacia el pecado."),

        (90, 33,
         "¿Qué es la vivificación del nuevo hombre?",
         "Es un sincero gozo de corazón en Dios por medio de Cristo y un amor y delicia en vivir según la voluntad de Dios y en la práctica de toda buena obra.",
         "La vida cristiana no es solo dejar el mal sino gozarse en el bien. La vivificación es gozo en Dios, amor a su voluntad y deleite en las buenas obras. No obedecemos a regañadientes sino con alegría. No vemos los mandamientos como cadenas sino como la guía del Padre amoroso. Cuando el Espíritu Santo obra en nosotros, la obediencia se convierte en placer. El Salmo 1 describe al hombre bienaventurado como aquel cuyo deleite está en la ley del Señor. Pídele a Dios que haga de su voluntad tu mayor gozo."),

        (91, 33,
         "¿Cuáles son las buenas obras?",
         "Solamente aquellas que se hacen por verdadera fe, conforme a la Ley de Dios y para su gloria; y no las que se fundan en nuestra propia opinión o en preceptos de los hombres.",
         "No toda obra aparentemente buena es verdaderamente buena ante Dios. Las buenas obras genuinas cumplen tres criterios: nacen de la fe verdadera, se conforman a la ley de Dios, y buscan su gloria. Una obra hecha sin fe, aunque parezca noble, no agrada a Dios. Una obra que contradice su ley, aunque tenga buenas intenciones, no es buena. Y una obra hecha para nuestra propia gloria, aunque sea impresionante, pierde su valor ante Dios. La verdadera bondad nace de la fe, sigue la Palabra y busca la gloria de Dios."),

        (92, 34,
         "¿Cuál es la Ley de Dios?",
         "Dios habló todas estas palabras diciendo: Yo soy el Señor tu Dios, que te saqué de la tierra de Egipto, de casa de servidumbre. I. No tendrás dioses ajenos delante de mí. II. No te harás imagen ni ninguna semejanza. III. No tomarás el nombre del Señor tu Dios en vano. IV. Acuérdate del día de reposo para santificarlo. V. Honra a tu padre y a tu madre. VI. No matarás. VII. No cometerás adulterio. VIII. No hurtarás. IX. No hablarás contra tu prójimo falso testimonio. X. No codiciarás.",
         "Los Diez Mandamientos son el resumen de la voluntad moral de Dios para la humanidad. No son sugerencias sino mandatos del Dios soberano. Pero nota el preámbulo: antes de dar la ley, Dios recuerda su gracia redentora. Los mandamientos no son la condición para ser salvos sino la guía para vivir como salvados. El orden es importante: primero la gracia, luego la obediencia. Primero el éxodo, luego la ley. Primero la salvación, luego la santificación. Los mandamientos son el camino de la gratitud para quienes ya han sido liberados por gracia."),

        (93, 34,
         "¿Cómo se dividen estos mandamientos?",
         "En dos tablas: la primera nos enseña cómo debemos comportarnos con Dios; la segunda, lo que debemos a nuestro prójimo.",
         "Los mandamientos se dividen en dos relaciones: con Dios y con el prójimo. Los primeros cuatro mandamientos regulan nuestra relación vertical con Dios. Los últimos seis regulan nuestras relaciones horizontales con los demás. Jesús resumió ambas tablas en dos mandamientos: amar a Dios y amar al prójimo. No podemos separar estas dos dimensiones. Quien dice amar a Dios pero maltrata a su prójimo es mentiroso. Y quien sirve al prójimo sin amar a Dios está incompleto. La vida cristiana integra ambas tablas en una vida de amor total."),

        (94, 34,
         "¿Qué ordena Dios en el primer mandamiento?",
         "Que yo, si no quiero poner en peligro la salvación de mi alma, huya y evite toda idolatría, hechicería, encantamientos, superstición, invocación de santos o de otras criaturas; y que reconozca bien al único y verdadero Dios, confíe solo en Él, me someta a Él con toda humildad y paciencia, espere todo bien solo de Él, y le ame, tema y honre con todo mi corazón. En resumen, que antes renuncie a todas las criaturas que hacer lo más mínimo contra su voluntad.",
         "El primer mandamiento es el fundamento de todos los demás. Exige lealtad exclusiva a Dios. Toda forma de idolatría, desde la adoración de imágenes hasta la superstición moderna, viola este mandamiento. Pero la idolatría no siempre es obvia; puede ser sutil. Todo lo que ponemos en el lugar de Dios, sea dinero, éxito, relaciones o placer, se convierte en un ídolo. El mandamiento exige que Dios sea primero en todo: en nuestro amor, confianza, temor y esperanza. Examina tu corazón: ¿hay algo que ocupe el lugar que solo Dios merece?"),

        (95, 34,
         "¿Qué es idolatría?",
         "Es poner nuestra confianza en cualquiera otra cosa en lugar del único Dios verdadero que se ha revelado en su Palabra, o además de Él; o inventar o tener alguna otra cosa en la cual poner nuestra confianza.",
         "La idolatría es más amplia de lo que pensamos. No se limita a adorar estatuas; incluye confiar en cualquier cosa más que en Dios. Tu carrera, tu cuenta bancaria, tus relaciones, tu salud, cualquiera de estas cosas puede convertirse en un ídolo si depositas en ella tu confianza suprema. Calvino dijo que el corazón humano es una fábrica de ídolos. Constantemente estamos tentados a reemplazar a Dios con sustitutos más visibles y tangibles. La lucha contra la idolatría es una batalla diaria que requiere vigilancia constante y dependencia del Espíritu Santo."),

        (96, 35,
         "¿Qué requiere Dios en el segundo mandamiento?",
         "Que no representemos a Dios con imagen alguna, ni le rindamos culto de ninguna otra manera que la que Él ha ordenado en su Palabra.",
         "El segundo mandamiento prohíbe representar a Dios mediante imágenes y adorarle de maneras que Él no ha establecido. Dios determina cómo quiere ser adorado; nosotros no. Este principio, conocido como el principio regulador del culto, protege la adoración de la invención humana. No podemos añadir al culto lo que Dios no ha mandado. Esto nos llama a una adoración sencilla, bíblica y centrada en la Palabra. La creatividad humana tiene su lugar, pero no puede reemplazar ni contradecir lo que Dios ha revelado sobre cómo quiere ser adorado."),

        (97, 35,
         "¿No se ha de hacer, pues, imagen alguna?",
         "Dios no puede ni debe ser representado de ninguna manera. Las criaturas, aunque pueden ser representadas, Dios prohíbe hacer y tener imagen de ellas para darles culto o servirse de ellas para honrarle a Él.",
         "Las imágenes de Dios están prohibidas porque cualquier representación visual de Él distorsiona su naturaleza infinita. Dios es espíritu, invisible e incomprensible. Cualquier imagen lo reduce y lo limita. Las criaturas pueden ser representadas artísticamente, pero no para adorarlas ni para usarlas como mediadores ante Dios. Este mandamiento nos invita a conocer a Dios a través de su Palabra, no a través de representaciones visuales. La fe viene por el oír, no por el ver. Busca conocer a Dios en las Escrituras, donde Él se ha revelado verdaderamente."),

        (98, 35,
         "¿No se pueden tolerar las imágenes en los templos como libros para los laicos?",
         "No; porque no debemos pretender ser más sabios que Dios, el cual quiere que sus cristianos sean instruidos no por ídolos mudos, sino por la predicación viva de su Palabra.",
         "Este argumento histórico de que las imágenes son 'libros para los iletrados' es rechazado por el catecismo. Dios no nos instruyó mediante imágenes sino mediante su Palabra predicada. No debemos sustituir lo que Dios estableció con lo que nos parece más conveniente. La predicación es el medio designado por Dios para enseñar a su pueblo. Puede parecer menos atractiva que las imágenes, pero es el método que Dios escogió y bendice. Confiemos en la sabiduría de Dios por encima de la nuestra."),

        (99, 36,
         "¿Qué ordena Dios en el tercer mandamiento?",
         "Que no solo no blasfememos o abusemos del nombre de Dios, jurando, maldiciendo o usando juramentos innecesarios, sino que tampoco seamos partícipes de tan horribles pecados con nuestro silencio y consentimiento; y que no usemos el santo nombre de Dios sino con temor y reverencia, a fin de que sea bien confesado e invocado por nosotros, y glorificado en todas nuestras palabras y obras.",
         "El nombre de Dios representa todo lo que Él es. Tomarlo en vano no se limita a la blasfemia obvia; incluye usar su nombre casualmente, jurar falsamente en su nombre, o permanecer en silencio cuando otros lo deshonran. Positivamente, debemos usar el nombre de Dios con reverencia, invocarlo en oración, confesarlo ante los demás, y glorificarlo en todo lo que hacemos y decimos. Cada vez que mencionas a Dios, debería ser con temor santo y gratitud profunda. Su nombre es santo; trátalo como tal."),

        (100, 36,
         "¿Es un pecado tan grave el blasfemar el nombre de Dios con juramento y maldiciones, que Dios se enoja también contra los que no hacen todo lo posible por impedirlo y prohibirlo?",
         "Sí, ciertamente; porque no hay pecado mayor ni que más provoque la ira de Dios que la blasfemia de su nombre; por eso mandó Dios que fuera castigado con la muerte.",
         "La gravedad de la blasfemia refleja la santidad de Dios. Deshonrar su nombre es atacar su misma esencia. Y no solo los blasfemos son culpables; también quienes lo toleran sin decir nada. Tenemos la responsabilidad de defender la honra del nombre de Dios. En una cultura donde la blasfemia es común y aceptada, los creyentes debemos ser diferentes. No solo evitamos blasfemar, sino que nos duele cuando otros lo hacen. Y cuando es apropiado, con gracia y valor, debemos hablar en defensa de la santidad del nombre de nuestro Dios."),

        (101, 37,
         "¿Podemos jurar piadosamente por el nombre de Dios?",
         "Sí, cuando el magistrado lo exija de sus súbditos, o cuando la necesidad lo requiera para mantener y promover la fidelidad y la verdad, para la gloria de Dios y el bienestar del prójimo; porque tal juramento está fundado en la Palabra de Dios y fue usado rectamente por los santos del Antiguo y Nuevo Testamento.",
         "El catecismo distingue entre el juramento vano y el juramento legítimo. Jurar por el nombre de Dios es apropiado cuando la autoridad civil lo requiere o cuando es necesario para establecer la verdad. En estos casos, invocar el nombre de Dios como testigo es un acto de adoración, reconociendo que Él es el Dios de toda verdad. Los santos bíblicos juraron legítimamente en varias ocasiones. Lo que se prohíbe es el juramento casual, falso o innecesario, no el juramento solemne hecho con reverencia en circunstancias apropiadas."),

        (102, 37,
         "¿Se puede también jurar por los santos o por alguna otra criatura?",
         "No; porque el juramento legítimo es una invocación de Dios, en la cual le pedimos que, como el único que conoce los corazones, sea testigo de la verdad y nos castigue si juramos en falso; honor que no se debe dar a ninguna criatura.",
         "Jurar por los santos, por los ángeles, o por cualquier criatura es inapropiado porque el juramento reconoce al testigo como omnisciente, y solo Dios lo es. Cuando juramos por Dios, estamos invocando al único que conoce nuestros corazones y puede juzgar nuestra sinceridad. Ninguna criatura tiene esa capacidad. Dar ese honor a una criatura es una forma de idolatría. Esto nos recuerda que toda nuestra vida debe estar orientada hacia Dios y solo hacia Él. Solo Él merece nuestra adoración, invocación y confianza absoluta."),

        (103, 38,
         "¿Qué ordena Dios en el cuarto mandamiento?",
         "En primer lugar, que se mantenga el ministerio de la Palabra de Dios y la educación religiosa, y que yo acuda con regularidad a la congregación de Dios, especialmente en el día de reposo, para oír la Palabra de Dios, para participar de los santos sacramentos, para invocar públicamente al Señor y para dar limosna cristiana. En segundo lugar, que todos los días de mi vida descanse de mis obras pecaminosas, deje obrar al Señor en mí por su Espíritu, y comience así en esta vida el reposo eterno.",
         "El día de reposo tiene un significado espiritual profundo que va más allá de simplemente no trabajar. Se trata de dedicar tiempo a la adoración comunitaria, la escucha de la Palabra, la participación en los sacramentos y la oración. Pero también tiene una dimensión diaria: cada día debemos descansar de nuestras obras pecaminosas y dejar que el Espíritu obre en nosotros. El verdadero reposo sabático se cumple en Cristo, quien nos da descanso del peso del pecado y de la salvación por obras. Vive cada día en ese reposo espiritual."),

        (104, 39,
         "¿Qué ordena Dios en el quinto mandamiento?",
         "Que tribute a mi padre, a mi madre y a todos mis superiores, honor, amor y fidelidad, y que me someta con la debida obediencia a su buena enseñanza y corrección, y que también tenga paciencia con sus debilidades, puesto que Dios quiere gobernarnos por medio de ellos.",
         "El quinto mandamiento establece el principio de autoridad. Dios gobierna el mundo a través de estructuras de autoridad: padres, gobernantes, maestros, pastores. Honrar a nuestros padres es el modelo para respetar toda autoridad legítima. Esto incluye amor, obediencia y paciencia con sus debilidades. No obedecemos porque las autoridades sean perfectas, sino porque Dios las ha establecido. Este mandamiento tiene una promesa: vida larga y bendecida. La sociedad que honra la autoridad prospera; la que la desprecia se destruye."),

        (105, 39,
         "¿Qué requiere Dios en el sexto mandamiento?",
         "Que no ultraje, odie, injurie ni mate a mi prójimo, ni por mí mismo, ni por medio de otro, ni en pensamiento, ni en palabra, ni en gesto y mucho menos en hecho; sino más bien que deponga todo deseo de venganza; además, que no me haga daño a mí mismo ni me exponga voluntariamente a ningún peligro. Por lo cual también el magistrado va armado de la espada para prevenir los homicidios.",
         "El sexto mandamiento prohíbe mucho más que el asesinato físico. Jesús enseñó que incluso la ira y el insulto violan este mandamiento (Mateo 5:21-22). No solo no debemos matar, sino que no debemos odiar, insultar, desear venganza, ni siquiera dañarnos a nosotros mismos. Positivamente, debemos proteger y preservar la vida. El mandamiento cubre pensamientos, palabras, gestos y acciones. Dios mira el corazón, no solo las manos. Examina tu corazón: ¿albergas resentimiento, odio o deseos de venganza? La gracia de Cristo puede liberar tu corazón de estos venenos."),

        (106, 40,
         "¿Se refiere este mandamiento solo al homicidio?",
         "Al prohibir el homicidio, Dios nos enseña que Él aborrece la raíz del homicidio, a saber: la envidia, el odio, la cólera y el deseo de venganza; y que todo esto delante de Él es un homicidio encubierto.",
         "Dios no se conforma con una obediencia superficial. Va a la raíz del problema: el corazón. La envidia, el odio, la cólera y el deseo de venganza son asesinatos embrionarios. Si no los detenemos, pueden crecer hasta convertirse en violencia abierta. Pero incluso si nunca llegan a la acción, ya son pecado ante Dios. Juan lo dice claramente: 'Todo aquel que aborrece a su hermano es homicida' (1 Juan 3:15). Dios quiere pureza de corazón, no solo de manos. Pídele al Espíritu que limpie tu corazón de todo resentimiento y odio."),

        (107, 40,
         "¿Basta entonces con que no matemos a nuestro prójimo de la manera descrita?",
         "No; porque al condenar Dios la envidia, el odio y la ira, nos manda amar a nuestro prójimo como a nosotros mismos, tener para con él paciencia, paz, dulzura, misericordia y amistad; protegerlo en cuanto nos sea posible contra todo lo que pueda perjudicarle, y hacer bien aun a nuestros enemigos.",
         "Los mandamientos no son solo negativos; tienen un lado positivo. No basta con no matar; debemos amar activamente. Debemos ser pacientes, pacíficos, dulces, misericordiosos y amistosos. Debemos proteger a nuestro prójimo y hacer bien incluso a nuestros enemigos. Esta es la enseñanza de Jesús: 'Amad a vuestros enemigos'. El estándar es altísimo y nos recuerda cuánto necesitamos la gracia de Dios. Solo el Espíritu puede capacitarnos para amar como Cristo amó. Hoy, busca una oportunidad concreta de bendecir a alguien, especialmente a alguien difícil de amar."),

        (108, 41,
         "¿Qué nos enseña el séptimo mandamiento?",
         "Que toda deshonestidad es maldita de Dios, y que por tanto debemos aborrecerla de todo corazón, y vivir casta y moderadamente, tanto dentro del santo matrimonio como fuera de él.",
         "El séptimo mandamiento protege la santidad del matrimonio y la pureza sexual. Toda forma de inmoralidad sexual es aborrecida por Dios. Pero no basta con evitar el adulterio; debemos vivir castamente en toda circunstancia. Los casados deben ser fieles a su cónyuge. Los solteros deben vivir en pureza. En una cultura sexualizada, este mandamiento es contracultural y desafiante. Pero la pureza sexual no es represión sino protección. Dios nos diseñó para la sexualidad dentro del matrimonio, y allí encuentra su mayor plenitud y gozo."),

        (109, 41,
         "¿Prohíbe Dios en este mandamiento solamente el adulterio y pecados semejantes?",
         "Puesto que nuestro cuerpo y nuestra alma son templo del Espíritu Santo, Dios quiere que los guardemos puros y santos; por eso prohíbe toda acción, gesto, palabra, pensamiento, deseo impuro y cualquier cosa que pueda incitar a ello.",
         "Como en los demás mandamientos, Dios va más allá de la acción externa. No solo prohíbe el adulterio sino todo pensamiento, deseo y situación que pueda conducir a la impureza. Jesús enseñó que mirar con lujuria ya es adulterio del corazón (Mateo 5:28). Nuestros cuerpos son templos del Espíritu Santo y debemos tratarlos con reverencia. Esto incluye cuidar lo que miramos, leemos, escuchamos y pensamos. La pureza es una batalla del corazón que se gana con vigilancia diaria y dependencia del Espíritu. Guarda tu corazón, porque de él mana la vida."),

        (110, 42,
         "¿Qué prohíbe Dios en el octavo mandamiento?",
         "No solo los robos y rapiñas que castiga el magistrado, sino que también llama robo todas las malas artes y medios, o cualquier pretensión con que intentemos apropiarnos de los bienes de nuestro prójimo; como son: pesas falsas, medidas cortas, mercancías adulteradas, moneda falsa, usura, o cualquier otro medio prohibido por Dios; y también toda avaricia y abuso y desperdicio de sus dones.",
         "El octavo mandamiento va mucho más allá del hurto común. Incluye toda forma de deshonestidad económica: fraude, engaño comercial, usura abusiva, avaricia y desperdicio. Dios está interesado en cómo manejamos nuestro dinero y nuestros negocios. La integridad económica es parte de la vida cristiana. También se incluye el desperdicio de los dones de Dios como una forma de robo, pues malgastamos lo que Él nos confió. Que nuestra vida financiera refleje la integridad del Dios a quien servimos."),

        (111, 42,
         "¿Qué manda Dios en este mandamiento?",
         "Que procure el bien de mi prójimo en cuanto pueda y obre con él como quisiera que obrasen conmigo; y que trabaje fielmente para poder socorrer a los pobres en sus necesidades.",
         "El lado positivo del octavo mandamiento nos llama a la generosidad activa. No solo no robamos; trabajamos para poder dar a los necesitados. La regla de oro se aplica aquí directamente: trata a otros como quisieras ser tratado. El trabajo honesto no es solo para nuestro beneficio sino para poder ser generosos. Efesios 4:28 lo resume perfectamente: 'El que hurtaba, no hurte más, sino trabaje... para que tenga qué compartir con el que padece necesidad'. La generosidad cristiana es el antídoto contra la avaricia."),

        (112, 43,
         "¿Qué requiere el noveno mandamiento?",
         "Que no levante falso testimonio contra nadie, que no tergiverse las palabras de ninguno, que no sea murmurador ni calumniador, que no condene ni ayude a condenar a nadie temerariamente y sin ser oído; sino que evite toda especie de mentira y engaño como obras propias del diablo, si no quiero provocar contra mí la terrible ira de Dios; y que en juicios y en todas las demás circunstancias ame la verdad, la diga y la confiese sinceramente, y que defienda y promueva el honor y la buena fama de mi prójimo en cuanto pueda.",
         "El noveno mandamiento protege la verdad y la reputación del prójimo. Prohíbe toda forma de mentira: falso testimonio, tergiversación, murmuración, calumnia y juicio temerario. Positivamente, nos llama a amar la verdad, hablar con sinceridad y defender la buena fama de nuestro prójimo. En la era de las redes sociales, este mandamiento es tremendamente relevante. Qué fácil es compartir rumores, juzgar sin escuchar y destruir reputaciones con un clic. El cristiano debe ser un guardián de la verdad y un defensor de la honra de su prójimo."),

        (113, 44,
         "¿Qué requiere el décimo mandamiento?",
         "Que ni aun el menor deseo o pensamiento contrario a cualquiera de los mandamientos de Dios entre jamás en nuestro corazón, sino que siempre y con toda el alma aborrezcamos el pecado y nos deleitemos en toda justicia.",
         "El décimo mandamiento llega a lo más profundo del corazón: los deseos. No solo prohíbe acciones y palabras pecaminosas sino los deseos mismos. La codicia es el pecado del corazón que alimenta todos los demás pecados. Adán y Eva codiciaron antes de desobedecer. David codició antes de adulterar. La codicia es la raíz de donde brotan los demás males. Este mandamiento nos muestra que la obediencia que Dios requiere es total: no solo externa sino interna, no solo de las manos sino del corazón. Solo Cristo cumplió este mandamiento perfectamente."),

        (114, 44,
         "¿Pueden los que se han convertido a Dios guardar estos mandamientos perfectamente?",
         "No; sino que aun los más santos, mientras vivan en este mundo, no tienen sino un pequeño principio de esta obediencia; pero de tal manera que, con firme resolución, comienzan a vivir no solo según algunos, sino según todos los mandamientos de Dios.",
         "La honestidad del catecismo es refrescante. Ni siquiera los más santos pueden guardar perfectamente los mandamientos en esta vida. Solo tenemos un pequeño principio de obediencia. Pero ese principio es real: tiene una dirección clara hacia todos los mandamientos, no solo algunos selectos. La perfección vendrá en la gloria; en esta vida luchamos, caemos y nos levantamos. Pero la dirección de nuestra vida es hacia la santidad. No te desanimes por tu imperfección; regocíjate por el progreso que la gracia produce. Y sigue luchando con la esperanza de la perfección futura."),

        (115, 44,
         "Si en esta vida ninguno puede guardar perfectamente los Diez Mandamientos, ¿por qué quiere Dios que se nos prediquen tan estrictamente?",
         "Primero, para que durante toda nuestra vida conozcamos más y más nuestra naturaleza pecaminosa, y busquemos con mayor empeño la remisión de los pecados y la justicia en Cristo. Segundo, para que nos ejercitemos sin cesar, y pidamos a Dios la gracia del Espíritu Santo, a fin de ser renovados más y más según la imagen de Dios, hasta que después de esta vida alcancemos la perfección.",
         "La ley tiene un triple uso en la vida cristiana. Primero, nos muestra nuestro pecado y nos lleva a Cristo (uso pedagógico). Segundo, refrena el mal en la sociedad (uso civil). Tercero, guía al creyente en santidad (uso normativo). Aquí el catecismo enfatiza los usos primero y tercero. La predicación estricta de la ley nos mantiene humildes y dependientes de Cristo, y nos motiva a buscar la santificación por el Espíritu. La ley no es enemiga del evangelio; es su compañera. Nos muestra nuestra necesidad y nos guía en gratitud."),

        # Sobre la Oración
        (116, 45,
         "¿Por qué es necesaria la oración para los cristianos?",
         "Porque es la parte principal de la gratitud que Dios requiere de nosotros, y porque Dios solo quiere dar su gracia y Espíritu Santo a los que se lo piden con gemidos sinceros e incesantes y le dan gracias por ello.",
         "La oración no es opcional para el cristiano; es esencial. Es la parte principal de la gratitud que debemos a Dios. Además, Dios ha decidido obrar a través de las oraciones de su pueblo. No porque Él necesite que le informemos, sino porque la oración es el medio por el cual nos conectamos con Él y recibimos su gracia. Orar es respirar espiritualmente. Así como el cuerpo necesita aire, el alma necesita oración. Si tu vida de oración es débil, toda tu vida espiritual se debilita. Hoy, toma tiempo para hablar con tu Padre celestial. Él espera escucharte."),

        (117, 45,
         "¿Qué se requiere en la oración para que agrade a Dios y sea oída por Él?",
         "Primero, que solo al verdadero Dios, que se nos ha revelado en su Palabra, pidamos de corazón todo lo que nos ha mandado pedir. Segundo, que conozcamos bien nuestra necesidad y nuestra miseria, para humillarnos ante su divina Majestad. Tercero, que tengamos este firme fundamento: que, aunque no lo merecemos, Dios ciertamente oirá nuestra oración por causa de Cristo nuestro Señor, como nos lo ha prometido en su Palabra.",
         "La oración eficaz tiene tres requisitos: dirigirse solo al Dios verdadero, nacer de una conciencia genuina de necesidad, y descansar en la mediación de Cristo. No oramos a santos ni a ángeles, sino solo a Dios. No oramos con orgullo sino con humildad. Y no oramos basados en nuestro mérito sino en los méritos de Cristo. Cuando oras, recuerda que te diriges al Creador del universo, que reconoces tu dependencia total de Él, y que tienes acceso a su trono solo por la sangre de Jesús. Ora con humildad y confianza."),

        (118, 45,
         "¿Qué nos ha mandado Dios pedir?",
         "Todo lo necesario para el alma y para el cuerpo, todo lo cual comprendió Cristo nuestro Señor en la oración que Él mismo nos enseñó.",
         "Dios nos invita a traerle todas nuestras necesidades, tanto espirituales como materiales. No hay petición demasiado grande ni demasiado pequeña para Él. El Padre Nuestro, que Cristo nos enseñó, es el modelo perfecto de oración que cubre todas las áreas de la vida. Desde la gloria de Dios hasta el pan de cada día, desde el perdón de pecados hasta la protección contra el mal. Que esta oración sea tu guía diaria y tu escuela de oración. En ella encontrarás todo lo que necesitas para hablar con tu Padre celestial."),

        (119, 46,
         "¿Cuál es esta oración?",
         "Padre nuestro que estás en los cielos, santificado sea tu nombre. Venga tu reino. Hágase tu voluntad, como en el cielo, así también en la tierra. El pan nuestro de cada día, dánoslo hoy. Y perdónanos nuestras deudas, como también nosotros perdonamos a nuestros deudores. Y no nos metas en tentación, mas líbranos del mal. Porque tuyo es el reino, y el poder, y la gloria, por todos los siglos. Amén.",
         "El Padre Nuestro es la oración perfecta porque fue enseñada por el Hijo perfecto. En pocas palabras abarca todo lo que necesitamos pedir. Comienza con Dios (su nombre, su reino, su voluntad) antes de llegar a nuestras necesidades. Este orden es significativo: primero la gloria de Dios, luego nuestras necesidades. Y termina con una doxología que reconoce que todo el poder y la gloria pertenecen a Dios. Esta oración debería ser memorizada, meditada y usada diariamente. No como una fórmula vacía sino como un modelo vivo para toda nuestra vida de oración."),

        (120, 46,
         "¿Por qué nos ha mandado Cristo que nos dirijamos a Dios diciendo: Padre nuestro?",
         "Para despertar en nosotros, al comienzo mismo de nuestra oración, el temor filial y la confianza en Dios, que son el fundamento de nuestra oración, a saber: que Dios, por medio de Cristo, es nuestro Padre, y que mucho menos nos negará lo que le pedimos con fe que nuestros padres nos negarían las cosas terrenales.",
         "Llamar a Dios 'Padre' no es un detalle menor; es el fundamento de toda oración cristiana. Esta palabra despierta dos actitudes esenciales: temor reverencial y confianza filial. Tememos a Dios porque es santo y majestuoso. Confiamos en Él porque es nuestro Padre amoroso. Si un padre terrenal, siendo imperfecto, da buenas cosas a sus hijos, cuánto más nuestro Padre celestial, siendo perfecto, nos dará lo que necesitamos. Cuando ores, no te acerques como un esclavo temeroso sino como un hijo amado. Tu Padre te espera con brazos abiertos."),

        (121, 47,
         "¿Qué quiere decir la primera petición: Santificado sea tu nombre?",
         "Concédenos primero que te conozcamos rectamente y que santifiquemos, glorifiquemos y alabemos toda tu omnipotencia, sabiduría, bondad, justicia, misericordia y verdad, que resplandecen en todas tus obras; y después, que ordenemos toda nuestra vida, pensamientos, palabras y obras de tal manera que tu nombre no sea blasfemado sino honrado y alabado por causa nuestra.",
         "La primera petición pone a Dios en primer lugar. Antes de pedir cualquier cosa para nosotros, pedimos que el nombre de Dios sea santificado, es decir, reconocido como santo. Esto implica conocer a Dios correctamente, glorificarlo en todas sus perfecciones, y vivir de tal manera que otros vean a Dios en nosotros. Nuestras vidas deben ser una carta abierta que honre el nombre de Dios. Cuando vivimos en pecado, deshonramos su nombre. Cuando vivimos en santidad, lo glorificamos. Que tu vida hoy sea una alabanza viviente al nombre santo de Dios."),

        (122, 48,
         "¿Qué quiere decir la segunda petición: Venga tu reino?",
         "Gobiérnanos de tal manera por tu Palabra y Espíritu, que nos sometamos a ti cada día más; conserva y aumenta tu Iglesia; destruye las obras del diablo y todo poder que se levante contra ti, y todos los malos propósitos que se fragüen contra tu santa Palabra, hasta que llegue la perfección de tu reino, en la cual tú serás todo en todos.",
         "Pedir que venga el reino de Dios es pedir que su gobierno se extienda en tres dimensiones. Primero, en nosotros: que nos sometamos más a Él cada día. Segundo, en la iglesia: que crezca y se fortalezca. Tercero, en el mundo: que todo mal sea destruido. Esta petición mira hacia el futuro glorioso cuando Cristo vuelva y Dios sea todo en todos. Pero también tiene aplicación presente: cada vez que obedecemos, el reino avanza. Cada vez que la iglesia crece, el reino se extiende. Cada vez que el mal retrocede, el reino se manifiesta. Ora y trabaja para que el reino de Dios avance."),

        (123, 49,
         "¿Qué quiere decir la tercera petición: Hágase tu voluntad, como en el cielo, así también en la tierra?",
         "Concédenos que nosotros y todos los hombres renunciemos a nuestra propia voluntad y obedezcamos tu voluntad, que es la única buena, sin murmuración alguna, para que cada uno cumpla con su deber y vocación, con tanta voluntad y fidelidad como los ángeles en el cielo.",
         "La tercera petición es quizás la más difícil de orar sinceramente, porque implica renunciar a nuestra propia voluntad. Nuestra naturaleza quiere imponer su agenda; Dios quiere que nos sometamos a la suya. El modelo es celestial: así como los ángeles obedecen instantánea y gozosamente, así debemos obedecer nosotros. Esto incluye cumplir fielmente nuestro deber y vocación, sin murmuración. La voluntad de Dios no es una carga sino un privilegio. Él sabe lo que es mejor. Cuando oramos 'hágase tu voluntad', estamos confiando en la sabiduría infinita de nuestro Padre."),

        (124, 50,
         "¿Qué quiere decir la cuarta petición: El pan nuestro de cada día, dánoslo hoy?",
         "Provee para todas las necesidades de nuestro cuerpo, para que de este modo reconozcamos que Tú eres la fuente única de todo bien, y que sin tu bendición ni nuestro cuidado ni nuestro trabajo, ni aun tus propios dones, podrían aprovecharnos; y así apartemos nuestra confianza de todas las criaturas para ponerla solo en Ti.",
         "Con esta petición reconocemos que dependemos totalmente de Dios para nuestras necesidades materiales. El pan de cada día incluye alimento, vestido, salud, trabajo y todo lo necesario para la vida. Al pedirlo diariamente, confesamos que Dios es la fuente de todo bien. Nuestro trabajo es importante, pero sin la bendición de Dios es inútil. Esta petición nos libera de la ansiedad materialista. No necesitamos acumular obsesivamente porque nuestro Padre proveerá mañana como proveyó hoy. Confía en Él para tus necesidades diarias y vive con la libertad de un hijo bien cuidado."),

        (125, 51,
         "¿Qué quiere decir la quinta petición: Perdónanos nuestras deudas, como también nosotros perdonamos a nuestros deudores?",
         "Ten a bien, por causa de la sangre de Cristo, no imputarnos a nosotros, pobres pecadores, ninguna de nuestras transgresiones, ni la maldad que siempre se encuentra en nosotros; así como nosotros encontramos este testimonio de tu gracia en nosotros, de que nuestro firme propósito es perdonar de corazón a nuestro prójimo.",
         "Esta petición reconoce dos verdades incómodas: que seguimos pecando y que debemos perdonar a otros. Pedimos perdón basados en la sangre de Cristo, no en nuestro mérito. Y el fruto de haber sido perdonados es que perdonamos a otros. No es que nuestro perdón a otros gane el perdón de Dios, sino que es evidencia de que hemos recibido su gracia. Quien no puede perdonar a otros demuestra que no ha comprendido cuánto le ha sido perdonado. El perdón recibido genera perdón otorgado. Hoy, si albergas resentimiento contra alguien, pide a Dios la gracia de perdonar como Él te ha perdonado."),

        (126, 52,
         "¿Qué quiere decir la sexta petición: Y no nos metas en tentación, mas líbranos del mal?",
         "Puesto que somos tan débiles que no podemos subsistir un momento, y además nuestros enemigos mortales, el diablo, el mundo y nuestra propia carne, no cesan de combatirnos, dígnate sustentarnos y fortalecernos por el poder de tu Espíritu Santo, para que no sucumbamos en esta lucha espiritual, sino que siempre resistamos firmemente, hasta que al fin obtengamos una completa victoria.",
         "La última petición reconoce nuestra debilidad y la fuerza de nuestros enemigos. Somos frágiles; el diablo, el mundo y la carne son poderosos. Sin la ayuda de Dios, caeríamos en un instante. Por eso pedimos que Dios nos sostenga y fortalezca por su Espíritu. La vida cristiana es una batalla espiritual real contra enemigos reales. Pero la victoria está asegurada para los que perseveran en Cristo. No luches solo; pide diariamente la protección y el poder del Espíritu. Y ten la esperanza de que un día la batalla terminará y la victoria será completa y eterna."),

        (127, 52,
         "¿Qué quiere decir la conclusión: Porque tuyo es el reino, y el poder, y la gloria, por todos los siglos?",
         "Que te pedimos todo esto, porque Tú, siendo nuestro Rey y Todopoderoso, nos puedes y quieres dar todo bien; y todo esto para que no nosotros, sino tu santo nombre sea eternamente glorificado.",
         "La doxología final del Padre Nuestro nos recuerda por qué podemos orar con confianza: porque Dios tiene el reino (la autoridad para conceder nuestras peticiones), el poder (la capacidad para hacerlo) y la gloria (el propósito último de todo). Oramos a un Dios que puede y quiere responder. Y el fin de todo es su gloria, no la nuestra. Esta conclusión transforma nuestra actitud en la oración: no somos mendigos desesperados sino hijos confiados de un Rey todopoderoso que busca glorificar a su Padre en todo."),

        (128, 52,
         "¿Qué quiere decir la palabra: Amén?",
         "Que esto es verdadero y cierto; porque mi oración es mucho más ciertamente oída por Dios, que lo que yo siento en mi corazón de que lo deseo de Él.",
         "El Amén no es una formalidad vacía sino una declaración de fe. Significa: 'Esto es verdadero y cierto'. Al decir Amén, afirmamos que creemos que Dios escucha nuestras oraciones. Y aquí viene algo hermoso: Dios escucha nuestras oraciones con más certeza de lo que nosotros mismos sentimos al orar. Nuestros sentimientos fluctúan, pero la fidelidad de Dios es constante. A veces oramos con poca fe, con dudas, con distracción. Pero Dios escucha incluso nuestras oraciones débiles porque responde basándose en su fidelidad, no en nuestra fervor. Amén. Así sea. Es verdad."),

        (129, 52,
         "¿Cómo concluye el Catecismo de Heidelberg?",
         "Con la certeza de que nuestra oración es oída por Dios y la esperanza de la vida eterna. Todo el catecismo nos ha llevado desde nuestra miseria, a través de la liberación en Cristo, hasta la gratitud expresada en obediencia y oración.",
         "El Catecismo de Heidelberg nos ha guiado en un viaje completo: desde el conocimiento de nuestra miseria, pasando por la gloriosa liberación en Cristo, hasta la vida de gratitud. Este esquema triple de miseria, liberación y gratitud resume toda la vida cristiana. Nunca dejamos de necesitar estas tres verdades. Cada día reconocemos nuestro pecado, nos aferramos a Cristo, y vivimos en agradecimiento. Que este catecismo no sea solo un documento histórico sino una guía viva para tu caminar diario con Dios. Soli Deo Gloria: solo a Dios sea la gloria.")
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO catecismo (id, domingo, pregunta, respuesta, meditacion)
        VALUES (?, ?, ?, ?, ?)
    """, preguntas)

    conn.commit()
    conn.close()
    print(f"Base de datos creada exitosamente con {len(preguntas)} preguntas en: {DB_PATH}")

if __name__ == "__main__":
    crear_base_de_datos()
