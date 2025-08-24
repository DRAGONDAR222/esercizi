import { useState } from 'react'
import './App.css'
import UserAlbums from './esercizi/UserAlbums'
import UserCrud from './esercizi/UserCrud'
import CardUtente from './esercizi_agosto/esercizio_2/CardUtente'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <UserAlbums/>
    <UserCrud></UserCrud>
    
      <CardUtente 
        nome="Mario Rossi" 
        email="mario.rossi@example.com" 
        imgUrl="https://placehold.co/200x200"
      />

      <CardUtente 
        nome="Laura Verdi" 
        email="laura.verdi@example.com" 
        imgUrl="https://placehold.co/200x200"
      />
    
    </>
  )
}

export default App
