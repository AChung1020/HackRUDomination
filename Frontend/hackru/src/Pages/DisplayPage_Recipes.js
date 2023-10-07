import React from 'react';
import recipes from './recipes.json';

function FoodIngredients() {
    return (
        <div>
            <h1>Food Recipes</h1>
            <ul>
                {Object.entries(recipes).map(([food, ingredients]) => (
                    <li key={food}>
                        <strong>{food}</strong>
                        <ul>
                            {ingredients.map(ingredient => (
                                <li key={ingredient}>{ingredient}</li>
                            ))}
                        </ul>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default FoodIngredients;

