import React from 'react';
import { useState, useEffect } from 'react';
import test from './test.json';
import { useNavigate } from 'react-router-dom';

function DisplayPage_Vitamins() {

  const navigate = useNavigate();

  const [data, setData] = useState();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/necessaryVitamins")
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  // const data = test;

  const routeChangeLogin = () => {
    let path = `/DisplayPage_Recipes`;
    navigate(path);
  };

  const [flipped, setFlipped] = useState(null);

  const handleFlip = (vitamin) => {
    if (flipped === vitamin) {
      setFlipped(null);
    } else {
      setFlipped(vitamin);
    }
  };

  // if (!data) return (
  //   <div className="loading">
  //     Loading...
  //   </div>
  // )

  if (loading) return <div className="loading">Loading...</div>;


  return (
    <div className='background'>
      <button type='submit' onClick={routeChangeLogin}>next &rarr;</button>
      <div className="vitamin-container">
        <h1>Looks like you could use some...</h1>
        
        {Object.entries(data).map(([vitamin, vitaminInfo]) => (
          <div key={vitamin}>
            <h2 className='title-vitamin'>{vitamin}</h2>
            <div className="vitamin-listing">
              <div className="vitamin-listing-content">
                <ul className="food-list">
                  {vitaminInfo[0].food.map((foodItem, idx) => (
                    <li key={foodItem}>
                      {foodItem}
                    </li>
                  ))}
                </ul>
                <div className="image-container" onClick={() => handleFlip(vitamin)}>
                  <div className={`card ${flipped === vitamin ? 'flip' : ''}`}>
                    <div className="front">
                      <div>Click here for a recipe!</div>
                    </div>
                    <div className="back">
                      {vitaminInfo[0].recipe && vitaminInfo[0].recipe.map(r => <li key={r}>{r}</li>)}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DisplayPage_Vitamins;
