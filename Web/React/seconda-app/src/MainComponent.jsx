import React, { useState } from "react";

const data = [
  { id: 1, name: "omar" },
  { id: 2, name: "tazio" },
  { id: 3, name: "gianluca" },
  { id: 4, name: "anna" },
];

const MainComponent = () => {
  const [people, setPeople] = useState(data);

  const removePeople = (id) => setPeople(people.filter((el) => el.id !== id));
  return (
    <div>
      <h3>Passaggio di Proprietà a cascata </h3>
      <Elenco people={people} removePeople={removePeople} />
    </div>
  );
};

const Elenco = ({ people, removePeople }) => {
  return (
    <div>
      {people.map((el, index) => {
        return <Persona key={index} {...el} removePeople={removePeople} />;
      })}
    </div>
  );
};

const Persona = ({ id, name, removePeople }) => {
  return (
    <div className="item">
      <h5> {name} </h5>
      <button className="button delete-button" onClick={() => removePeople(id)}>
        {" "}
        x{" "}
      </button>
    </div>
  );
};

export default MainComponent;

