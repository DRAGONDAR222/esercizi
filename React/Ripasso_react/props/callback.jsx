const Figlio = ({ onClick }) => {
  return <button onClick={onClick}>Cliccami</button>;
};

//---------------

const Genitore = () => {
  const handleClick = () => {
    alert("Il figlio ha cliccato!");
  };

  return <Figlio onClick={handleClick} />;
};

export default Genitore;
