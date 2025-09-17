import { useState } from 'react'
import './App.css'
import UserAlbums from './esercizi/UserAlbums'
import UserCrud from './esercizi/UserCrud'
import Saluto from './esercizi_agosto/esercizio_1/Saluto'
import CardUtente from './esercizi_agosto/esercizio_2/CardUtente'
import MenuRistorante from './esercizi_agosto/esercizio_3/MenuRistorante'
import Termostato from './esercizi_agosto/esercizio_4/Termostato'
import CampoRicerca from './esercizi_agosto/esercizio_5/CampoRicerca'
import MessaggioSegreto from './esercizi_agosto/esercizio_6/MessaggioSegreto'
import AggiornaTitolo from './esercizi_agosto/esercizio_7/AggiornaTitolo'
import GalleriaFoto from './esercizi_agosto/esercizio_8/GalleriaFoto'
import ModuloContatti from './esercizi_agosto/esercizio_9/ModuloContatti'
import BlogApp from './esercizi_agosto/esercizio_10/BlogApp'
import Render_menu from "./esercizi_agosto/Render_menu";



function App() {
  const [esercizio, setEsercizio] = useState('')

  const renderCondizionale = () => {
    switch (esercizio) {
      case "Saluto":
        return <Saluto />
      case "CardUtente":
        return <CardUtente
          nome="Mario Rossi"
          email="mario.rossi@example.com"
          imgUrl="https://placehold.co/200x200"
        />
      case "MenuRistorante":
        return <MenuRistorante />
      case "Termostato":
        return <Termostato />
      case "CampoRicerca":
        return <CampoRicerca />
      case "MessaggioSegreto":
        return <MessaggioSegreto />
      case "AggiornaTitolo":
        return <AggiornaTitolo />
      case "GalleriaFoto":
        return <GalleriaFoto />
      case "ModuloContatti":
        return <ModuloContatti />
      case "BlogApp":
        return <BlogApp />
}
  }

  return (
    <>
      <Render_menu onSetEsercizio={setEsercizio} />
      <div>{renderCondizionale()}</div>
    </>
  )
}

export default App
