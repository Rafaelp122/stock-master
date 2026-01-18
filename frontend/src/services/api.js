import axios from "axios";

// Cria uma instância do Axios com a URL base dinâmica do .env
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Interceptor para logs em desenvolvimento ou injetar tokens JWT no futuro
api.interceptors.response.use(
  response => response,
  error => {
    console.error("Erro na chamada da API:", error.response || error.message);
    return Promise.reject(error);
  }
);

export default api;
