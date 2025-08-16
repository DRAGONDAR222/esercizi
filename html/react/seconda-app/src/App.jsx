import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserAlbums from './esercizi/UserAlbums'
import UserCrud from './esercizi/UserCrud'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <UserAlbums/>
    <UserCrud></UserCrud>
    
    </>
  )
}

export default App
