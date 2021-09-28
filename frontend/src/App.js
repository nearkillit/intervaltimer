import { useSelector, useDispatch } from "react-redux";
import Actions from './modules/actions'
import { useState } from "react";
import * as api from "./api"

function App(){
  const dispatch = useDispatch();
  const state = useSelector(state => state)
  const [todo, setTodo] = useState("")

  const getTodo = (e) => {
    setTodo(e.target.value)
  }

  const addTodo = () => {
    // dispatch(Actions.addTodo({todo}))    
  }

  const createState = () => {
    api
      .createTodos({ todo })
      .then( res => {
        console.log(res); 
      })
      .catch( e => {
        console.log(e);
      })
  }

  const checkState = () => {
    api
      .fetchTodos()
      .then( res => {
        dispatch(Actions.fetchTodo({ todos: res.data })) 
      })
      .catch( e => {
        console.log(e);
      })
  }

  const deleteState = () => {
    api
      .deleteTodos(8)
      .then( res => {
        console.log(res);
      })
      .catch( e => {
        console.log(e);
      })
  }

  const editState = () => {
    api
      .editTodos(7,{ todo:"changed" })
      .then( res => {
        console.log(res);
      })
      .catch( e => {
        console.log(e);
      })
  }

  return (
    <div>
      <input onChange={getTodo} />
      <button onClick={addTodo}>Add</button>
      <button onClick={createState}>createState</button>
      <button onClick={checkState}>checkState</button>
      <button onClick={deleteState}>deleteState</button>
      <button onClick={editState}>editState</button>
      <table>
        <thead>
          <tr>
            <td>id</td>
            <td>内容</td>
            <td>作成日付</td>
            <td>更新日付</td>
          </tr>
        </thead>
        <tbody>
        { state.todos.map( (t,index) => ( 
          <tr key={index}>
            <td>{t.id}</td>
            <td>{t.todo}</td>
            <td>{t.created_at}</td>
            <td>{t.updated_at}</td>
          </tr>))
        }
        </tbody>
      </table>
    </div>
  )
}

export default App