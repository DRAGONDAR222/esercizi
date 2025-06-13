import React from 'react'

const Clock = () => {
  return (
    <h2>{new Date().toLocaleDateString()+ " " + new Date().toLocaleTimeString()}</h2>
  )
}

export default Clock

 