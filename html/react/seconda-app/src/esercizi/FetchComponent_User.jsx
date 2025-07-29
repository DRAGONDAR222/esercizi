import React, { useEffect, useState } from 'react';

const url = "https://jsonplaceholder.typicode.com/users";

const FetchComponent = () => {
  const [users, setUsers] = useState([]);

  const getData = async function () {
    const user = await fetch(url).then(ris => ris.json());
    setUsers(user);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <>
      <select className="users form-select">
        {users.map((el) => {
          const { id, name, email } = el;
          return (
            <option key={id} value={id}>
              {name} 
            </option>
          );
        })}
      </select>
    </>
  );
};

export default FetchComponent;
