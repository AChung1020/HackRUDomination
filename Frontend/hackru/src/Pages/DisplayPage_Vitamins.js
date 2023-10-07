import React from 'react';
import test from './test.json';

function DisplayPage_Vitamins() {
  return (
    <div className='background'>
      <div className="vitamin-container">
        <h1>Let's add some new foods to your diet!</h1>
        {Object.entries(test.Vitamins).map(([vitamin, foods]) => (
          <div key={vitamin} className="vitamin-listing">
              <h2>Vitamin {vitamin}</h2>
              <ul className="food-list">
                {foods.map(food => (
                  <li key={food}>{food}</li>
                ))}
              </ul>
          </div>
        ))}

      </div>
    </div>
    );
}
export default DisplayPage_Vitamins;
