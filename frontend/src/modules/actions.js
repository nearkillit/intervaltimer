const Actions = {
    addTodo(value) {
      return {
        type: 'ADDTODO',
        value,
      }
    },
    fixTodo(value) {
      return {
        type: 'FIXTODO',
        value,
      }
    },
    updTodo(value) {
      return {
        type: 'UPDTODO',
        value,
      }
    },
    delTodo(value) {
      return {
        type: 'DELTODO',
        value,
      }
    },
    fetchTodo(value) {
      return {
        type: 'FETCHTODO',
        value,
      }
    },
  }
  
  export default Actions