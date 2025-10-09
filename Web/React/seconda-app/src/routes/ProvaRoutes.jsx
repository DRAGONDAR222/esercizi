import React, { useEffect, useState } from "react";
import Home from "./Home";
import About from "./About";
import Profile from "./Profile";
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import ErrorPage from "./ErrorPage";
import SingleProfile from "./SingleProfile";
import MyProfile from "./MyProfile";

const ProvaRoutes = () => {
//   const [link, setLink] = useState("Home");
//   const renderComponent = () => {
//     if (link === "Home") {
//       return <Home></Home>;
//     }
//     if (link === "About") {
//       return <About />;
//     }
//     if (link === "Profile") {
//       return <Profile></Profile>;
//     }
//   };
//  useEffect(()=>{
//     console.log("Componente renderizzato")
//  });
  return (

    <BrowserRouter>
        <nav className="navbar bg-body-tertiary">
          <div className="container-fluid">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/profile">Profile</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<Home></Home>}></Route>
          <Route path="/about" element={<About></About>}></Route>
          <Route path="/profile/" element={<Profile></Profile>}>
            <Route path='id:' element={<SingleProfile></SingleProfile>}></Route>
            <Route path='me' element={<MyProfile></MyProfile>}></Route>
          </Route>
          <Route path='*' element={<ErrorPage></ErrorPage>}></Route>
        </Routes>
      </BrowserRouter>
    // <div>
    //   <nav className="navbar bg-body-tertiary">
    //     <div className="container-fluid">
    //       <button
    //         className="btn btn-link nav-link"
    //         onClick={() => setLink("Home")}
    //       >
    //         Home
    //       </button>
    //       <button
    //         className="btn btn-link nav-link"
    //         onClick={() => setLink("About")}
    //       >
    //         About
    //       </button>
    //       <button
    //         className="btn btn-link nav-link"
    //         onClick={() => setLink("Profile")}
    //       >
    //         Profile
    //       </button>
    //     </div>
    //   </nav>
    //   <div className="container">
    //     <br></br>
    //     <b>{renderComponent()}</b>
    //   </div>
    // </div>
  );
};

export default ProvaRoutes;