import { useSelector, useDispatch } from "react-redux";
import Actions from '../modules/actions'
import { useState } from "react";
// react
import { 
  Switch,
  Route,  
  useHistory
  // useParams,  
} from 'react-router-dom'

// component
import Timer from './timer'

// mui
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';


// material ui のスタイルの指定https://qiita.com/uehaj/items/969ef20ccef850d2e9b1
// material ui gridの作成　https://qiita.com/vimyum/items/5ba06ca166ebe4992617
const useStyles = makeStyles({
  root: {    
    textAlign: 'center'
  },
  cardContents: {
    textAlign: 'center',    
  }
});

function TimerList(){
  const history = useHistory();
  const handleLink = path => history.push(path)
  const dispatch = useDispatch();
  const state = useSelector(state => state)
  const [todo, setTodo] = useState("")
  const classes = useStyles();

  const getTodo = (e) => {
    setTodo(e.target.value)
  }

  const addTodo = () => {
    // dispatch(Actions.addTodo({todo}))    
  }

  return (
    <div>
      <TextField label="タイマー名" variant="outlined"  onChange={getTodo} />
      <Button onClick={addTodo}>追加する</Button>
      <Grid container spacing={1}>
        <Grid item xs={5}>
          <Timer />   
        </Grid>
      </Grid>      
    </div>
  )
}

export default TimerList