import React from 'react'

const Componente1 = (props) => {
  console.log(props)
  return (
    <div>
      <div>componente1 di: {props.children}</div>
      <Anagrafica/>
      <Messaggio/>
    </div>
  );
};

const Anagrafica = () => {
  return(<div>Anagrafica</div>)
}

const Messaggio = () => {
  return(<div>Messaggio</div>)
}

export default Componente1