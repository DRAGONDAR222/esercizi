import React from 'react'

const Clock = (props) => {
    console.log(props.timezone,props.country)
    const data= new Date(t);
    const t=Date.now()+3600*props.timezone*1000;
  return (
    <h2>in {props.country} sono le {data.toLocaleTimeString()} del giorno {data.toLocaleDateString()}</h2>
  )
}

export default Clock

 