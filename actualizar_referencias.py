import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catecismo.db")

def actualizar_referencias():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Agregar columna si no existe
    try:
        cursor.execute("ALTER TABLE catecismo ADD COLUMN referencias TEXT DEFAULT ''")
    except sqlite3.OperationalError:
        pass  # La columna ya existe

    # Referencias bíblicas para cada pregunta del Catecismo de Heidelberg
    # Formato: "Referencia visible|libro_api capítulo:versículo;Otra ref|libro_api cap:ver"
    referencias = {
        1: "Romanos 14:7-8|Romans 14:7-8;1 Corintios 6:19-20|1 Corinthians 6:19-20;1 Juan 3:8|1 John 3:8;Juan 10:28|John 10:28;Romanos 8:28|Romans 8:28;Romanos 8:38-39|Romans 8:38-39",
        2: "Lucas 24:46-47|Luke 24:46-47;1 Corintios 6:11|1 Corinthians 6:11;Tito 3:3-7|Titus 3:3-7;Efesios 5:8-10|Ephesians 5:8-10",
        3: "Romanos 3:20|Romans 3:20;Romanos 7:7|Romans 7:7;Gálatas 3:24|Galatians 3:24",
        4: "Mateo 22:37-40|Matthew 22:37-40;Deuteronomio 6:5|Deuteronomy 6:5;Levítico 19:18|Leviticus 19:18",
        5: "Romanos 3:10-12|Romans 3:10-12;Génesis 6:5|Genesis 6:5;Romanos 8:7|Romans 8:7;Efesios 2:3|Ephesians 2:3",
        6: "Génesis 1:26-27|Genesis 1:26-27;Efesios 4:24|Ephesians 4:24;Colosenses 3:10|Colossians 3:10",
        7: "Génesis 3:1-7|Genesis 3:1-7;Romanos 5:12|Romans 5:12;Romanos 5:18-19|Romans 5:18-19",
        8: "Génesis 8:21|Genesis 8:21;Romanos 8:7-8|Romans 8:7-8;Juan 3:5-6|John 3:5-6;Efesios 2:1-5|Ephesians 2:1-5",
        9: "Génesis 1:31|Genesis 1:31;Eclesiastés 7:29|Ecclesiastes 7:29;Deuteronomio 30:19|Deuteronomy 30:19",
        10: "Gálatas 3:10|Galatians 3:10;Deuteronomio 27:26|Deuteronomy 27:26;Nahúm 1:2|Nahum 1:2;Hebreos 10:31|Hebrews 10:31",
        11: "Éxodo 34:6-7|Exodus 34:6-7;Éxodo 20:5|Exodus 20:5;Salmo 5:4-6|Psalms 5:4-6;2 Corintios 5:10|2 Corinthians 5:10",
        12: "Génesis 2:17|Genesis 2:17;Romanos 8:3-4|Romans 8:3-4;Hebreos 2:14-15|Hebrews 2:14-15",
        13: "Mateo 6:12|Matthew 6:12;Romanos 2:4-5|Romans 2:4-5;Isaías 64:6|Isaiah 64:6",
        14: "Hebreos 2:14-17|Hebrews 2:14-17;1 Pedro 3:18|1 Peter 3:18;Isaías 53:11|Isaiah 53:11",
        15: "Jeremías 23:5-6|Jeremiah 23:5-6;1 Timoteo 2:5|1 Timothy 2:5;Lucas 2:11|Luke 2:11;Isaías 9:6|Isaiah 9:6",
        16: "Hebreos 2:17|Hebrews 2:17;Romanos 5:19|Romans 5:19;1 Pedro 3:18|1 Peter 3:18;1 Corintios 15:21|1 Corinthians 15:21",
        17: "Isaías 53:4-5|Isaiah 53:4-5;Hechos 2:24|Acts 2:24;Juan 3:16|John 3:16;1 Juan 4:9|1 John 4:9",
        18: "1 Corintios 1:30|1 Corinthians 1:30;1 Timoteo 2:5-6|1 Timothy 2:5-6;Mateo 1:21|Matthew 1:21;Isaías 7:14|Isaiah 7:14",
        19: "Génesis 3:15|Genesis 3:15;Génesis 22:18|Genesis 22:18;Romanos 1:2|Romans 1:2;Hebreos 1:1-2|Hebrews 1:1-2;Hechos 3:22-24|Acts 3:22-24",
        20: "Romanos 5:17-19|Romans 5:17-19;Juan 1:12-13|John 1:12-13;Mateo 7:14|Matthew 7:14;Isaías 53:11|Isaiah 53:11",
        21: "Santiago 2:19|James 2:19;Hebreos 11:1|Hebrews 11:1;Romanos 4:20-21|Romans 4:20-21;Efesios 2:8-9|Ephesians 2:8-9;Gálatas 2:20|Galatians 2:20",
        22: "Mateo 28:19-20|Matthew 28:19-20;Marcos 1:15|Mark 1:15;Juan 20:31|John 20:31",
        23: "Hechos 8:37|Acts 8:37;1 Corintios 15:3-4|1 Corinthians 15:3-4",
        24: "1 Pedro 1:18-21|1 Peter 1:18-21;Mateo 28:19|Matthew 28:19",
        25: "Deuteronomio 6:4|Deuteronomy 6:4;Mateo 28:19|Matthew 28:19;1 Juan 5:7|1 John 5:7;2 Corintios 13:14|2 Corinthians 13:14",
        26: "Génesis 1:1|Genesis 1:1;Salmo 33:6|Psalms 33:6;Hechos 17:28|Acts 17:28;Romanos 8:28|Romans 8:28;Mateo 10:29-30|Matthew 10:29-30",
        27: "Hechos 17:25-28|Acts 17:25-28;Hebreos 1:3|Hebrews 1:3;Jeremías 23:23-24|Jeremiah 23:23-24;Mateo 10:29|Matthew 10:29",
        28: "Romanos 5:3-5|Romans 5:3-5;Santiago 1:3|James 1:3;1 Tesalonicenses 5:18|1 Thessalonians 5:18;Romanos 8:28|Romans 8:28;Romanos 8:38-39|Romans 8:38-39",
        29: "Mateo 1:21|Matthew 1:21;Hechos 4:12|Acts 4:12;Juan 15:4-5|John 15:4-5;1 Timoteo 2:5|1 Timothy 2:5",
        30: "1 Corintios 1:30-31|1 Corinthians 1:30-31;Colosenses 2:10|Colossians 2:10;Juan 14:6|John 14:6;Hebreos 7:25|Hebrews 7:25",
        31: "Hechos 3:22|Acts 3:22;Deuteronomio 18:15|Deuteronomy 18:15;Hebreos 4:14-15|Hebrews 4:14-15;Salmo 2:6|Psalms 2:6;Lucas 1:33|Luke 1:33",
        32: "1 Juan 2:27|1 John 2:27;Hechos 11:26|Acts 11:26;Apocalipsis 1:6|Revelation 1:6;1 Pedro 2:9|1 Peter 2:9;Romanos 12:1|Romans 12:1",
        33: "Juan 1:14|John 1:14;Juan 1:18|John 1:18;Juan 3:16|John 3:16;Romanos 8:15-17|Romans 8:15-17;Gálatas 4:4-7|Galatians 4:4-7",
        34: "1 Pedro 1:18-19|1 Peter 1:18-19;1 Corintios 6:20|1 Corinthians 6:20;Colosenses 1:13-14|Colossians 1:13-14",
        35: "Juan 1:14|John 1:14;Lucas 1:35|Luke 1:35;Gálatas 4:4|Galatians 4:4;Hebreos 2:14|Hebrews 2:14;Hebreos 4:15|Hebrews 4:15",
        36: "1 Juan 1:9|1 John 1:9;Salmo 51:5|Psalms 51:5;Romanos 8:3-4|Romans 8:3-4;1 Corintios 1:30|1 Corinthians 1:30",
        37: "Isaías 53:4-5|Isaiah 53:4-5;1 Pedro 2:24|1 Peter 2:24;1 Pedro 3:18|1 Peter 3:18;1 Juan 2:2|1 John 2:2",
        38: "Isaías 53:4-5|Isaiah 53:4-5;Lucas 23:13-24|Luke 23:13-24;Hechos 4:27-28|Acts 4:27-28;Juan 19:13-16|John 19:13-16",
        39: "Gálatas 3:13|Galatians 3:13;Deuteronomio 21:23|Deuteronomy 21:23;Filipenses 2:8|Philippians 2:8",
        40: "Romanos 6:23|Romans 6:23;Hebreos 2:9|Hebrews 2:9;Hebreos 9:22|Hebrews 9:22",
        41: "1 Corintios 15:3-4|1 Corinthians 15:3-4;Hechos 13:29|Acts 13:29;Juan 19:38-42|John 19:38-42",
        42: "Filipenses 1:21-23|Philippians 1:21-23;Juan 5:24|John 5:24;Romanos 7:24-25|Romans 7:24-25",
        43: "Romanos 6:5-11|Romans 6:5-11;Gálatas 2:20|Galatians 2:20;Colosenses 3:5|Colossians 3:5;Romanos 12:1|Romans 12:1",
        44: "Mateo 27:46|Matthew 27:46;Isaías 53:10|Isaiah 53:10;Salmo 18:5-6|Psalms 18:5-6;Salmo 116:3|Psalms 116:3",
        45: "Romanos 4:25|Romans 4:25;1 Corintios 15:17-20|1 Corinthians 15:17-20;Romanos 6:4|Romans 6:4;Efesios 2:4-6|Ephesians 2:4-6;Filipenses 3:20-21|Philippians 3:20-21",
        46: "Hechos 1:9-11|Acts 1:9-11;Marcos 16:19|Mark 16:19;Hebreos 4:14|Hebrews 4:14;Hebreos 9:24|Hebrews 9:24",
        47: "Mateo 28:20|Matthew 28:20;Juan 14:16-18|John 14:16-18;Mateo 18:20|Matthew 18:20",
        48: "Hechos 1:11|Acts 1:11;Hechos 3:21|Acts 3:21;Juan 17:11|John 17:11;Colosenses 2:9|Colossians 2:9",
        49: "Romanos 8:34|Romans 8:34;1 Juan 2:1|1 John 2:1;Hebreos 9:24|Hebrews 9:24;Juan 14:2|John 14:2;Juan 16:7|John 16:7;Colosenses 3:1-2|Colossians 3:1-2",
        50: "Efesios 1:20-23|Ephesians 1:20-23;Colosenses 1:18|Colossians 1:18;Mateo 28:18|Matthew 28:18",
        51: "Hechos 2:33|Acts 2:33;Efesios 4:8-12|Ephesians 4:8-12;Salmo 2:9|Psalms 2:9;Juan 10:28|John 10:28",
        52: "Mateo 25:31-34|Matthew 25:31-34;Filipenses 3:20|Philippians 3:20;Lucas 21:28|Luke 21:28;Tito 2:13|Titus 2:13;2 Tesalonicenses 1:6-10|2 Thessalonians 1:6-10",
        53: "1 Pedro 1:2|1 Peter 1:2;1 Corintios 6:11|1 Corinthians 6:11;Gálatas 4:6|Galatians 4:6;Romanos 8:16|Romans 8:16;Juan 15:26|John 15:26",
        54: "Juan 10:27-29|John 10:27-29;Efesios 1:10-13|Ephesians 1:10-13;Hechos 2:46-47|Acts 2:46-47;Isaías 59:21|Isaiah 59:21;1 Juan 3:21|1 John 3:21",
        55: "1 Corintios 12:12-13|1 Corinthians 12:12-13;1 Corintios 12:21|1 Corinthians 12:21;Romanos 12:4-5|Romans 12:4-5;1 Juan 1:3|1 John 1:3",
        56: "1 Juan 2:2|1 John 2:2;Romanos 4:6-8|Romans 4:6-8;2 Corintios 5:19-21|2 Corinthians 5:19-21;Jeremías 31:34|Jeremiah 31:34;Miqueas 7:19|Micah 7:19",
        57: "Juan 6:39-40|John 6:39-40;1 Corintios 15:42-44|1 Corinthians 15:42-44;Filipenses 3:21|Philippians 3:21;Job 19:25-26|Job 19:25-26",
        58: "2 Corintios 5:1-5|2 Corinthians 5:1-5;Romanos 8:23|Romans 8:23;1 Corintios 2:9|1 Corinthians 2:9;Juan 17:3|John 17:3",
        59: "Romanos 1:17|Romans 1:17;Habacuc 2:4|Habakkuk 2:4;Romanos 5:1|Romans 5:1;Juan 3:36|John 3:36",
        60: "Romanos 3:21-26|Romans 3:21-26;Romanos 4:4-5|Romans 4:4-5;2 Corintios 5:21|2 Corinthians 5:21;Gálatas 2:16|Galatians 2:16;Efesios 2:8-9|Ephesians 2:8-9",
        61: "Romanos 3:28|Romans 3:28;Gálatas 3:11|Galatians 3:11;Romanos 10:10|Romans 10:10;1 Corintios 1:30|1 Corinthians 1:30",
        62: "Romanos 3:20|Romans 3:20;Isaías 64:6|Isaiah 64:6;Gálatas 3:10|Galatians 3:10;Filipenses 3:8-9|Philippians 3:8-9",
        63: "Romanos 4:4|Romans 4:4;Lucas 17:10|Luke 17:10;Mateo 5:12|Matthew 5:12;Hebreos 11:6|Hebrews 11:6",
        64: "Mateo 7:17-18|Matthew 7:17-18;Gálatas 5:22-24|Galatians 5:22-24;Juan 15:5|John 15:5;Romanos 6:1-2|Romans 6:1-2",
        65: "Efesios 2:8|Ephesians 2:8;Filipenses 1:29|Philippians 1:29;Romanos 10:17|Romans 10:17;Hechos 16:14|Acts 16:14;1 Pedro 1:23-25|1 Peter 1:23-25",
        66: "Génesis 17:7|Genesis 17:7;Romanos 4:11|Romans 4:11;Deuteronomio 30:6|Deuteronomy 30:6;Mateo 28:19|Matthew 28:19;Hechos 2:38|Acts 2:38",
        67: "Romanos 6:3|Romans 6:3;Hebreos 9:12-14|Hebrews 9:12-14;Mateo 28:19|Matthew 28:19;Hechos 2:38|Acts 2:38;Romanos 10:17|Romans 10:17",
        68: "Mateo 28:19-20|Matthew 28:19-20;1 Corintios 11:23-26|1 Corinthians 11:23-26",
        69: "Mateo 26:28|Matthew 26:28;Marcos 14:24|Mark 14:24;Hechos 2:38|Acts 2:38;Hebreos 10:10|Hebrews 10:10",
        70: "1 Juan 1:7|1 John 1:7;1 Corintios 6:11|1 Corinthians 6:11;Apocalipsis 1:5|Revelation 1:5;Romanos 6:4|Romans 6:4;Juan 3:5|John 3:5",
        71: "Mateo 28:19|Matthew 28:19;Marcos 16:16|Mark 16:16;Tito 3:5|Titus 3:5;Hechos 22:16|Acts 22:16",
        72: "1 Juan 1:7|1 John 1:7;1 Pedro 3:21|1 Peter 3:21;Efesios 5:26|Ephesians 5:26",
        73: "Romanos 6:3-4|Romans 6:3-4;Gálatas 3:27|Galatians 3:27;Marcos 16:16|Mark 16:16;Tito 3:5|Titus 3:5",
        74: "Génesis 17:7|Genesis 17:7;Mateo 19:14|Matthew 19:14;Hechos 2:38-39|Acts 2:38-39;Colosenses 2:11-12|Colossians 2:11-12;1 Corintios 7:14|1 Corinthians 7:14",
        75: "1 Corintios 11:23-26|1 Corinthians 11:23-26;Mateo 26:26-28|Matthew 26:26-28;Lucas 22:19-20|Luke 22:19-20",
        76: "Juan 6:51|John 6:51;Juan 6:55-56|John 6:55-56;1 Corintios 10:16-17|1 Corinthians 10:16-17;Efesios 5:30|Ephesians 5:30",
        77: "1 Corintios 11:23-26|1 Corinthians 11:23-26;1 Corintios 10:16-17|1 Corinthians 10:16-17",
        78: "Marcos 14:22-24|Mark 14:22-24;1 Corintios 10:1-4|1 Corinthians 10:1-4;1 Corintios 11:26|1 Corinthians 11:26",
        79: "1 Corintios 10:16-17|1 Corinthians 10:16-17;1 Corintios 11:26-28|1 Corinthians 11:26-28;Juan 6:55-58|John 6:55-58",
        80: "Hebreos 10:10-14|Hebrews 10:10-14;Hebreos 10:18|Hebrews 10:18;Hebreos 7:26-27|Hebrews 7:26-27;Hebreos 9:12|Hebrews 9:12;Juan 19:30|John 19:30",
        81: "1 Corintios 11:28-29|1 Corinthians 11:28-29;1 Corintios 10:19-22|1 Corinthians 10:19-22;Salmo 50:15-16|Psalms 50:15-16",
        82: "1 Corintios 11:20-32|1 Corinthians 11:20-32;Mateo 18:17|Matthew 18:17;Isaías 1:11-17|Isaiah 1:11-17",
        83: "Mateo 16:19|Matthew 16:19;Mateo 18:18|Matthew 18:18;Juan 20:22-23|John 20:22-23",
        84: "Mateo 16:19|Matthew 16:19;Juan 20:21-23|John 20:21-23;2 Corintios 2:15-16|2 Corinthians 2:15-16",
        85: "Mateo 18:15-18|Matthew 18:15-18;1 Corintios 5:3-5|1 Corinthians 5:3-5;2 Corintios 2:6-8|2 Corinthians 2:6-8;2 Tesalonicenses 3:14-15|2 Thessalonians 3:14-15",
        86: "Romanos 6:13|Romans 6:13;Romanos 12:1-2|Romans 12:1-2;1 Pedro 2:9-10|1 Peter 2:9-10;Mateo 5:16|Matthew 5:16;1 Pedro 2:12|1 Peter 2:12",
        87: "1 Corintios 6:9-10|1 Corinthians 6:9-10;Gálatas 5:19-21|Galatians 5:19-21;Efesios 5:5-6|Ephesians 5:5-6",
        88: "Romanos 6:1-11|Romans 6:1-11;Colosenses 3:5-10|Colossians 3:5-10;Efesios 4:22-24|Ephesians 4:22-24",
        89: "Romanos 8:13|Romans 8:13;Joel 2:13|Joel 2:13;2 Corintios 7:10|2 Corinthians 7:10",
        90: "Romanos 6:11|Romans 6:11;Romanos 14:17|Romans 14:17;Gálatas 2:20|Galatians 2:20;Colosenses 3:12-17|Colossians 3:12-17",
        91: "Romanos 12:2|Romans 12:2;1 Samuel 15:22|1 Samuel 15:22;Efesios 2:10|Ephesians 2:10;Deuteronomio 12:32|Deuteronomy 12:32",
        92: "Éxodo 20:1-17|Exodus 20:1-17;Deuteronomio 5:6-21|Deuteronomy 5:6-21",
        93: "Mateo 22:37-40|Matthew 22:37-40;Deuteronomio 6:5|Deuteronomy 6:5;Levítico 19:18|Leviticus 19:18",
        94: "1 Juan 5:21|1 John 5:21;1 Corintios 10:14|1 Corinthians 10:14;Deuteronomio 6:4-5|Deuteronomy 6:4-5;Mateo 4:10|Matthew 4:10",
        95: "Filipenses 3:19|Philippians 3:19;Efesios 5:5|Ephesians 5:5;Gálatas 4:8|Galatians 4:8;1 Crónicas 16:26|1 Chronicles 16:26",
        96: "Deuteronomio 4:15-19|Deuteronomy 4:15-19;Isaías 40:18-25|Isaiah 40:18-25;Hechos 17:29|Acts 17:29;Romanos 1:23|Romans 1:23",
        97: "Éxodo 34:13-14|Exodus 34:13-14;Deuteronomio 7:5|Deuteronomy 7:5;2 Reyes 18:4|2 Kings 18:4",
        98: "Juan 4:24|John 4:24;Romanos 10:17|Romans 10:17;2 Pedro 1:19|2 Peter 1:19;2 Timoteo 3:16-17|2 Timothy 3:16-17",
        99: "Levítico 24:15-16|Leviticus 24:15-16;Éxodo 20:7|Exodus 20:7;Mateo 5:34-37|Matthew 5:34-37;Santiago 5:12|James 5:12",
        100: "Levítico 24:15-16|Leviticus 24:15-16;Levítico 5:1|Leviticus 5:1;Proverbios 29:24|Proverbs 29:24",
        101: "Deuteronomio 6:13|Deuteronomy 6:13;Deuteronomio 10:20|Deuteronomy 10:20;Isaías 48:1|Isaiah 48:1;Hebreos 6:16|Hebrews 6:16;2 Corintios 1:23|2 Corinthians 1:23",
        102: "Mateo 5:34-37|Matthew 5:34-37;Santiago 5:12|James 5:12;Mateo 4:10|Matthew 4:10",
        103: "Deuteronomio 6:6-7|Deuteronomy 6:6-7;Salmo 40:9-10|Psalms 40:9-10;Hechos 2:42|Acts 2:42;Hebreos 10:25|Hebrews 10:25;1 Corintios 16:2|1 Corinthians 16:2",
        104: "Efesios 6:1-4|Ephesians 6:1-4;Colosenses 3:18-21|Colossians 3:18-21;Proverbios 1:8|Proverbs 1:8;Romanos 13:1-2|Romans 13:1-2;Éxodo 20:12|Exodus 20:12",
        105: "Mateo 5:21-22|Matthew 5:21-22;Génesis 9:6|Genesis 9:6;Mateo 26:52|Matthew 26:52;Romanos 13:4|Romans 13:4;Proverbios 25:21-22|Proverbs 25:21-22",
        106: "1 Juan 3:15|1 John 3:15;Romanos 12:19|Romans 12:19;Mateo 5:22|Matthew 5:22;Proverbios 14:30|Proverbs 14:30;Gálatas 5:19-21|Galatians 5:19-21",
        107: "Mateo 5:44-45|Matthew 5:44-45;Romanos 12:10|Romans 12:10;Mateo 7:12|Matthew 7:12;Gálatas 6:1-2|Galatians 6:1-2;Efesios 4:2|Ephesians 4:2",
        108: "1 Corintios 6:18-20|1 Corinthians 6:18-20;Hebreos 13:4|Hebrews 13:4;Efesios 5:3-4|Ephesians 5:3-4",
        109: "Mateo 5:27-28|Matthew 5:27-28;1 Corintios 6:18-20|1 Corinthians 6:18-20;Efesios 5:3-4|Ephesians 5:3-4;1 Tesalonicenses 4:3-5|1 Thessalonians 4:3-5",
        110: "1 Corintios 6:10|1 Corinthians 6:10;Efesios 4:28|Ephesians 4:28;Proverbios 11:1|Proverbs 11:1;Lucas 6:35|Luke 6:35;Proverbios 28:8|Proverbs 28:8",
        111: "Mateo 7:12|Matthew 7:12;Efesios 4:28|Ephesians 4:28;Filipenses 2:4|Philippians 2:4;1 Timoteo 6:17-18|1 Timothy 6:17-18",
        112: "Efesios 4:25|Ephesians 4:25;Proverbios 12:22|Proverbs 12:22;Mateo 7:1-2|Matthew 7:1-2;1 Pedro 4:8|1 Peter 4:8;Proverbios 11:13|Proverbs 11:13",
        113: "Romanos 7:7-8|Romans 7:7-8;Proverbios 4:23|Proverbs 4:23;Santiago 1:14-15|James 1:14-15;Salmo 19:14|Psalms 19:14",
        114: "1 Juan 1:8|1 John 1:8;Romanos 7:14-15|Romans 7:14-15;Eclesiastés 7:20|Ecclesiastes 7:20;Filipenses 3:12-14|Philippians 3:12-14",
        115: "Romanos 3:20|Romans 3:20;Romanos 7:24-25|Romans 7:24-25;1 Juan 1:9|1 John 1:9;Salmo 51:2-4|Psalms 51:2-4",
        116: "Salmo 50:14-15|Psalms 50:14-15;1 Tesalonicenses 5:17|1 Thessalonians 5:17;Mateo 7:7-8|Matthew 7:7-8;Lucas 11:9-13|Luke 11:9-13",
        117: "Juan 4:24|John 4:24;Romanos 8:26|Romans 8:26;1 Juan 5:14|1 John 5:14;Juan 14:13-14|John 14:13-14;Santiago 1:6|James 1:6",
        118: "Mateo 6:33|Matthew 6:33;Santiago 1:17|James 1:17;Filipenses 4:6|Philippians 4:6",
        119: "Mateo 6:9-13|Matthew 6:9-13;Lucas 11:2-4|Luke 11:2-4",
        120: "Mateo 7:9-11|Matthew 7:9-11;Lucas 11:11-13|Luke 11:11-13;Mateo 6:9|Matthew 6:9",
        121: "Salmo 115:1|Psalms 115:1;Juan 17:3|John 17:3;Mateo 5:16|Matthew 5:16;Romanos 2:24|Romans 2:24",
        122: "Salmo 2:6-9|Psalms 2:6-9;Mateo 6:33|Matthew 6:33;Romanos 10:1|Romans 10:1;Colosenses 1:9-12|Colossians 1:9-12;Apocalipsis 22:17-20|Revelation 22:17-20",
        123: "Mateo 6:10|Matthew 6:10;Mateo 16:24|Matthew 16:24;Romanos 12:2|Romans 12:2;Tito 2:11-12|Titus 2:11-12",
        124: "Mateo 6:11|Matthew 6:11;Salmo 104:27-28|Psalms 104:27-28;Salmo 145:15-16|Psalms 145:15-16;Proverbios 30:8|Proverbs 30:8;1 Timoteo 4:4-5|1 Timothy 4:4-5",
        125: "Mateo 6:12|Matthew 6:12;Salmo 51:1-4|Psalms 51:1-4;1 Juan 2:1-2|1 John 2:1-2;Mateo 6:14-15|Matthew 6:14-15;Efesios 4:32|Ephesians 4:32",
        126: "Mateo 6:13|Matthew 6:13;Mateo 26:41|Matthew 26:41;1 Pedro 5:8|1 Peter 5:8;Juan 17:15|John 17:15;Efesios 6:10-13|Ephesians 6:10-13;1 Corintios 10:13|1 Corinthians 10:13",
        127: "Romanos 10:11-12|Romans 10:11-12;2 Pedro 2:9|2 Peter 2:9;Salmo 55:22|Psalms 55:22;2 Timoteo 4:18|2 Timothy 4:18",
        128: "2 Corintios 1:20|2 Corinthians 1:20;2 Timoteo 2:13|2 Timothy 2:13;Salmo 145:18|Psalms 145:18",
        129: "Salmo 145:18-19|Psalms 145:18-19;Romanos 8:26|Romans 8:26;Apocalipsis 22:20|Revelation 22:20"
    }

    for pregunta_id, refs in referencias.items():
        cursor.execute(
            "UPDATE catecismo SET referencias = ? WHERE id = ?",
            (refs, pregunta_id)
        )

    conn.commit()
    conn.close()
    print(f"Referencias bíblicas actualizadas para {len(referencias)} preguntas")

if __name__ == "__main__":
    actualizar_referencias()
