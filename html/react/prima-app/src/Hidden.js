import React, { useState } from "react";

const Hidden = () => {
    const [show,setShow] = useState(true);
    return (
        <div>
            <button onClick={()=> setShow(!show)}>{show ? "Nascondi":"Visualizza"}</button>
        </div>
    )
}

const Elemento = ()=>{
    return (<h2>Elemento</h2>)
}

export default Hidden 