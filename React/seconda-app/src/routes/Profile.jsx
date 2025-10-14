import React from 'react'
import { Outlet } from 'react-router-dom'

const Profile = () => {
  return (
    <div>
      <h1>Profile</h1>
      <nav className='d-flex flex-row gap-2 justify-content-center'>
        <Link to='me'>Il mio profilo</Link>
        <Link to='/profile/2'>Il mio profilo 2</Link>
      </nav>
      <div>
        <Outlet></Outlet>
      </div>
    </div>
  )
}

export default Profile