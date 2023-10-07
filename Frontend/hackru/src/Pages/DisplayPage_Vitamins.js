import React from 'react';
import test from './test.json';

function DisplayPage_Vitamins() {

    return (
        <div>
          <h1>Vitamin Sources</h1>
          <ul>
            {/* for loop */}
            {Object.entries(test.Vitamins).map(([vitamin, foods]) => (
              <li key={vitamin}>
                <strong>Vitamin {vitamin}</strong>
                <ul>
                  {foods.map(food => (
                    <li key={food}>{food}</li>
                  ))}
                </ul>
              </li>
            ))}
          </ul>
        </div>
      );
}

export default DisplayPage_Vitamins;
