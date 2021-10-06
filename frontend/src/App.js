// react
import { 
  Switch,
  Route,  
  useHistory  
} from 'react-router-dom'

// component
import TimerList from './components/timer_list'
import TimerDetail from './components/timer_detail'
import AuthenticationView from './components/authentication_view'

// mui
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

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

function App(){
  const history = useHistory();
  const handleLink = path => history.push(path)  
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Typography variant="h3" component="h3" onClick={()=>handleLink('/')}>
        タイマー作成サイト
      </Typography>
      <AuthenticationView />
      <Switch>
        <Route path='/' exact component={TimerList} />                    
        <Route path='/timerdetail/:Timer_id' exact component={TimerDetail} />
        <Route>
          <p>Not found</p>
        </Route>
      </Switch>
    </div>
  )
}

export default App