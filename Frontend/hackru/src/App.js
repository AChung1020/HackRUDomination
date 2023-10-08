import './App.css';
import Home from './Pages/Home.js'
import DisplayPage_Vitamins from './Pages/DisplayPage_Vitamins.js'
import DisplayPage_Recipes from './Pages/DisplayPage_Recipes.js'
import React from 'react';
import {Routes, Route} from 'react-router-dom';
import { Buffer } from 'buffer';

global.Buffer = Buffer;


function App() {
  return (
    <React.Fragment>
      <Routes>
        <Route path = '/Home' element = {<Home />} />
        <Route path = '/DisplayPage_Vitamins' element = {<DisplayPage_Vitamins />} />
        <Route path = '/DisplayPage_Recipes' element = {<DisplayPage_Recipes />} />
       </Routes>

    </React.Fragment>
  );
}

export default App;
