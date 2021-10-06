// 初期State
const initialState = {    
        user:0,        
        timers:[
          {
            id:0,
            name:'筋トレ',            
            interval:[3,3,3],
            loop:0
          }
        ],
        timerStopFlag: true     
  }

  // Reducer処理
  const reducer = (state = initialState, action) => {
    switch (action.type) {
      case 'ADD_TIMER': {
        const initialTimer = { 
          id:0,
          name:'',            
          interval:[],
          loop:5
        }
        const newTimer = Object.assign({},initialTimer)
        const newTimers = state.timers
        newTimer.name = action.value.timerName  
        // idの付与
        newTimer.id = newTimers.reduce((p,c) => p > c.id ? p : c.id , 0) + 1
        newTimers.push(newTimer)             
        return { ...state, timers: newTimers }
      }
      case 'DELETE_TIMER': {        
        const newTimers = state.timers.filter(t => t.id !== action.value.timersId)
        return { ...state, timers: newTimers }
      }
      case 'ADD_INTERVAL_TIMER': {        
        const getTimers = state.timers
        const getTimer = getTimers.filter(t => t.id === action.value.timersId)[0]        
        getTimer.interval.push(5)        
        const newTimers = getTimers.map(t => t.id === action.value.timersId ? getTimer : t)
        return { ...state, timers: newTimers }
      }
      case 'UPDATE_INTERVAL_TIMER': {
        const getTimers = state.timers
        const getTimer = getTimers.filter(t => t.id === action.value.timersId)[0]
        getTimer.interval[action.value.index] = action.value.intervalTime * 1        
        const newTimers = getTimers.map(t => t.id === action.value.timersId ? getTimer : t)        
        return { ...state, timers: newTimers }
      }
      case 'DELETE_INTERVAL_TIMER': {        
        const getTimers = state.timers
        const getTimer = getTimers.filter(t => t.id === action.value.timersId)[0]
        getTimer.interval.splice(action.value.index, 1)        
        const newTimers = getTimers.map(t => t.id === action.value.timersId ? getTimer : t)        
        return { ...state, timers: newTimers }
      }
      case 'UPDATE_LOOP': {
        const getTimers = state.timers
        const getTimer = getTimers.filter(t => t.id === action.value.timersId)[0]        
        getTimer.loop = action.value.loop * 1        
        const newTimers = getTimers.map(t => t.id === action.value.timersId ? getTimer : t)        
        return { ...state, timers: newTimers }
      }
      case 'UPDATE_TIMER_STOP_FLAG': {
        return { ...state, timerStopFlag: action.value}
      }
      default: {
        return state
      }
    }
  }
  
  export default reducer