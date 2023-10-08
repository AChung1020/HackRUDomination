import React from 'react';
import recipes from './recipes.json';
import { useState, useEffect } from 'react';

function FoodIngredients() {

      // const [data, setData] = useState();

    // const [data, setData] = useState();
  //const [loading, setLoading] = useState(true);

  // useEffect(() => {
  //   fetch("http://localhost:5000/data")
  //     .then(response => response.json())
  //     .then(data => {
  //       setData(data);
  //       setLoading(false);
  //     })
  //     .catch(error => {
  //       console.error('Error fetching data:', error);
  //       setLoading(false);
  //     });
  // }, []);

  //if (loading) return <div className="loading">Loading...</div>;

    return (
        <div className='background'>
        <div className="vitamin-container">
        <h1>Cook up a new recipe!</h1>
            <ul className="food-list">
                {Object.entries(recipes).map(([food, ingredients]) => (
                    <ul key={food} className="vitamin-listing">
                        <h2>{food}</h2>
                        <ul className="food-list">
                            {ingredients.map(ingredient => (
                                <li key={ingredient}>{ingredient}</li>
                            ))}
                        </ul>
                    </ul>
                ))}
            </ul>
        </div>
        </div>
    );
}

export default FoodIngredients;

