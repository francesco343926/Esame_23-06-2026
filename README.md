# Esame - 23/06/2026

---
> **❗ ATTENZIONE:** 
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale** 
> (https://github.com/my-github-username/Esame_23-06-2026) e non quello principale.

---
**DURATA DELLA PROVA**: 2 h

---
Si consideri il database `yelp_reduced.sql`, contenente informazioni su attività commerciali (business), recensioni 
(review) ed utenti, strutturato secondo il seguente diagramma ER.
![database.png](img/database.png)

-----
## LINK ACCESSIBILI DURANTE L'ESAME
- `Python`: https://docs.python.org/
- `PyCharm`: https://www.jetbrains.com/help/pycharm/getting-started.html
- `DBeaver`: https://dbeaver.com/docs/dbeaver/
- `Flet`: https://docs.flet.dev/api-reference/
- `mysql-connector-python`: https://pypi.org/project/mysql-connector-python/ & https://dev.mysql.com/doc/connector-python/en/
- `NetworkX`: https://networkx.org/documentation/stable/reference/index.html
-----

## Materiale Fornito
Il repository Esame_23-06-2026 è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario 
per svolgere l'esame:

```code
Esame_23-06-2026/
├── database/
│   ├── __init__.py
|   ├── connector.cnf 
|   ├── DB_connect.py 
│   └── dao.py (DA MODIFICARE) 
│
├── model/ (AGGIUNGERE ULTERIORI CLASSI SE NECESSARIE) 
│   ├── __init__.py
│   ├── user.py
│   └── model.py (DA MODIFICARE) 
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py (DA MODIFICARE)
│   └── view.py (DA MODIFICARE)
│
├── requirements.txt
├── Guida esame in laboratorio v02.pdf
├── plot_35.png 
├── README.md
├── yelp_reduced.sql (DA IMPORTARE)
└── main.py (DA ESEGUIRE)
 ```
