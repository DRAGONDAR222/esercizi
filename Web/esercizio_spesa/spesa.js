// Funzione per aggiungere un elemento alla lista
function addItem() {
    const itemInput = document.getElementById('itemInput');
    const newItem = itemInput.value;

    if (newItem) {
        const li = document.createElement('li');
        li.textContent = newItem;

        const list = document.getElementById('dynamicList');
        list.appendChild(li);

        itemInput.value = ''; // Svuota il campo di input
    } else {
        alert('Inserisci un elemento per aggiungerlo alla lista!');
    }
}

// Funzione per resettare la lista
function resetList() {
    const list = document.getElementById('dynamicList');
    while (list.firstChild) {
        list.removeChild(list.firstChild); // Svuota la lista
    }
}