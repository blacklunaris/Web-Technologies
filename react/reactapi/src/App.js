import React,{useEffect,useState} from "react";
import './App.css';

const App= () =>{
  const APP_ID="3704ea75";
  const APP_KEY="0f7c23dc8001b3f1e205cb30261985fe";
  const[recipes,setRecipes]= useState([]);

  useEffect(() =>{
    getRecipes();
  },[]);

  const getRecipes= async () =>{
    const response= await fetch('https://api.edamam.com/search?q=chicken&app_id=${APP_ID}&app_key=${APP_KEY}');
    const data = await response.json();
    setRecipes(data.hits);

    /* Alternatively
    fetch(https://api.edamam.com)
    .then(response =>{
    response.json()
  })
    */
  };

  return(
    <div className="App">
      <form className="search-form">
        <input className="search-bar" type ="text"/>
        <button
          className="search-button"
          type="submit"
        >
          Search
        </button>
      </form>

    </div>
  );

}


export default App;
