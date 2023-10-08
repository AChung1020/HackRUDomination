import React from 'react';
import recipes from './recipes.json';

function FoodIngredients() {
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

