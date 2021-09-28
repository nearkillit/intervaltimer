// 初期State
const initialState = {
    todos: [{ created_at:'000', updated_at:'000', id:1, todo:"test"}],    
  }
  // Reducer処理
  const reducer = (state = initialState, action) => {
    switch (action.type) {
      case 'ADDTODO': {
        const newTodos = state.todos        
        const newTodo = { todo: action.value.todo }
        newTodo.id = state.todos.reduce( (a,c) =>  a.id > c.id ? a.id : c.id , { id:0 }) + 1
        newTodo.created_at = '作成'
        newTodo.updated_at = '更新'
        newTodos.push(newTodo)             
        return { ...state, todos: newTodos }
      }      
      case 'UPDTODO': {
        return console.log(action.value)
      }
      case 'DELTODO': {
        return console.log(action.value)
      }
      case 'FETCHTODO': {
        return { ...state, todos: action.value.todos }
      }
      default: {
        return state
      }
    }
  }
  
  export default reducer