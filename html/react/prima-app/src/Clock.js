import React from 'react';

const Clock = (props) => {
  console.log(props.timezone, props.country);

  const t = Date.now() + 3600 * props.timezone * 1000;
  const data = new Date(t);

  return (
    <h3>
      {props.country}: <b>{data.toLocaleTimeString()}</b> del giorno: <b>{data.toLocaleDateString()}</b>
    </h3>
  );
};

export default Clock;


 