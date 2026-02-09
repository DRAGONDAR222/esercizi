# per vedere tutti i contatiner

    docker ps

---

# postgres

    docker exec -it its_postgresql psql -U postgres

---

# python

    docker exec -it its_dev python3

---

# per eseguire un esercizio python

    docker exec -it its_dev python3 /home/nomeCartella/main.py

dove home equivale (già impostato) al path di vscode
e il resto alla sottocartella ed il resto del path...


---

## in docker 
    /home/its/vscode_projects/programmi_esercizi/
### corrisponde a 
    /home

## per Esempio:
    /home/its/vscode_projects/programmi_esercizi/Python/Basics/esercizio_match/3C-1.py
### diventa
    /home/Python/Basics/esercizio_match/3C-1.py


---

# comando per risalire all'imagine di un conatiner

    docker ps -a --filter "name=its_dev" --format "table {{.Names}}\t{{.Image}}\t{{.Status}}"

---

# per liberare una porta occupata da un container questo può essere messo in: status exited
### liberando di fatto la sua porta localhost (nel caso)

    docker stop <nome_container_o_id>
### es:
    docker stop its_dev


poi per riavviarlo eseguiamo

    docker start -ai <nome_container_o_id>
### es:
    docker start -ai its_dev

---

# per risalire al volume usato in un container

    docker inspect NOME_CONTAINER --format '{{json .Mounts}}' | jq
### es:
    docker inspect its_dev --format '{{json .Mounts}}' | jq

### jq sarebbe un programma che legge json da terminale (va installato)
#### ma si puo fare anche senza togliendo: | jq

---

# comando per vedere i volumi disponibili

    docker volume ls

---

# comando per impostare un volume indipendente a partire da un path locale 

    docker volume create --name nome_volume --opt type=none --opt device=/percorso/locale --opt o=bind

1. `--name nome_volume` → scegli un nome per il volume.
2. `--opt type=none` → tipo generico (bind mount).
3. `--opt device=/percorso/locale` → path sul tuo filesystem locale.
4. `--opt o=bind` → dice a Docker di “collegare” la cartella locale al volume.

---

# comando per creare un docker compose
    Creare un Docker Compose è semplice: si scrive un file YAML chiamato di solito **docker-compose.yml** nella cartella del progetto. Non serve “comandare” la creazione, basta creare il file con dentro la configurazione dei container.

1. Crea il file

    touch docker-compose.yml

2. Definisci i servizi nel file

```yaml
version: "3.9"  # versione del formato Compose

services:
    nome_servizio1:
        image: nome_immagine1  # oppure build: ./path_dockerfile
        ports:
        - "porta_locale:porta_container"
        volumes:
        - volume_locale:/path/container
        environment:
        VAR1: valore
        VAR2: valore

    nome_servizio2:
        image: nome_immagine2
        depends_on:
        - nome_servizio1
        ports:
        - "porta_locale2:porta_container2"
        volumes:
        - volume_locale2:/path/container2
        environment:
        VAR3: valore

volumes:
    volume_locale:
    volume_locale2:
```

### in pratica:
- ``services``: definisce ogni container come servizio.
- ``image/build``: indica quale immagine usare o dove trovare il Dockerfile.
- ``ports``: mappatura tra host e container.
- ``volumes``: montaggio di directory o volumi persistenti.
- ``depends_on``: definisce l’ordine di avvio tra servizi.
- ``volumes`` (a fine file): definisce volumi persistenti condivisibili tra container.


3. Avvia i container contemporaneamente
    docker-compose up 
    (li mette nello status: up)
    docker-compose stop
    (li mette nello status: exited)


