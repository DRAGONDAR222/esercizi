import React from 'react'
import { useNavigate } from 'react-router-dom';

const ErrorPage = () => {
    const navigate = useNavigate();
  return (
    <div>
        <p>Questa pagina non esiste</p>
        <button className='btn btn-succes' onClick={()=>navigate('/')}>Torna alla Home</button>
    </div>
  )
}

export default ErrorPage