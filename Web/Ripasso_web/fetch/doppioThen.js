fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log("Dati ricevuti:", data);
    // usa i dati qui
  });
