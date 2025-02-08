import React, { useState } from "react";
import { getRecipes } from "../api";
import RecipeCard from "../components/RecipeCard";

const Recipes = () => {
  const [n, setN] = useState(1);
  const [portions, setPortions] = useState(2);
  const [recipes, setRecipes] = useState([]);
  const [shoppingList, setShoppingList] = useState({});

  const handleGetRecipes = async () => {
    try {
      const response = await getRecipes(n, portions);
      setRecipes(response.data.recipes);
      setShoppingList(response.data.shopping_list);
    } catch (err) {
      console.error("Failed to fetch recipes", err);
    }
  };

  return (
    <div>
      <h2>Recipes</h2>
      <div>
        <label>Number of recipes:</label>
        <input
          type="number"
          value={n}
          onChange={(e) => setN(e.target.value)}
          min="1"
        />
      </div>
      <div>
        <label>Portions per recipe:</label>
        <input
          type="number"
          value={portions}
          onChange={(e) => setPortions(e.target.value)}
          min="1"
        />
      </div>
      <button onClick={handleGetRecipes}>Get Recipes</button>

      <div>
        {recipes.map((recipe) => (
          <RecipeCard key={recipe.id} recipe={recipe} />
        ))}
      </div>

      <h3>Shopping List</h3>
      <ul>
        {Object.entries(shoppingList).map(([ingredient, quantity]) => (
          <li key={ingredient}>
            {ingredient}: {quantity}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recipes;