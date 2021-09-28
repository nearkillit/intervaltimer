import axios from 'axios';

// const API_BASE_URL = 'http://www.mypress.jp:3003'; // json-server用
const API_BASE_URL = 'http://127.0.0.1:8000/todo/api/'; // Django用

const client = axios.create({  
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  },
});

export function fetchTodos() {
  return client.get('/todos/');
}

export function createTodos(params) {   
  return client.post('/todos/', params);
}

export function editTodos(id, params) {
  return client.put(`/todos/${id}/`, params);
}

export function deleteTodos(id) {
  return client.delete(`/todos/${id}/`);
}