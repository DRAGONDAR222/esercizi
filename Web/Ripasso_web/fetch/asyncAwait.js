const getData = async (URL) => {
  try {
    const response = await fetch(URL);   // primo then
    const data = await response.json();  // secondo then

    console.log("Dati:", data);
    // qui usi i dati

  } catch (err) {
    console.error("Errore:", err);
  }
};
