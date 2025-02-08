import axios from "axios";
import { getToken } from "./auth";

const API_URL = "http://your-fastapi-backend-url"; // Replace with your backend URL

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add a request interceptor to include the JWT token
api.interceptors.request.use((config) => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const register = async (username, password) => {
  return api.post("/register/", { username, password });
};

export const login = async (username, password) => {
  return api.post("/token/", { username, password });
};

export const getRecipes = async (n, portions) => {
  return api.get("/recipes/", { params: { n, portions } });
};