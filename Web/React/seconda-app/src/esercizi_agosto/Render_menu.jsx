const Render_menu = ({ onSetEsercizio }) => {
  const array_esercizi = [
    "Saluto",
    "CardUtente",
    "MenuRistorante",
    "Termostato",
    "CampoRicerca",
    "MessaggioSegreto",
    "AggiornaTitolo",
    "GalleriaFoto",
    "ModuloContatti",
    "BlogApp",
  ];

  return (
   <nav className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div className="container-fluid">
        <ul className="navbar-nav me-auto mb-2 mb-lg-0 d-flex flex-row">
          {array_esercizi.map((item) => (
            <li key={item} className="nav-item">
              <button
                className="nav-link btn btn-link text-white px-3"
                onClick={() => onSetEsercizio(item)}
              >
                {item}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
};

export default Render_menu;
