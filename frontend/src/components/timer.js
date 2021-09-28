import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import InputAdornment from '@material-ui/core/InputAdornment';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles({
    root: {    
      textAlign: 'center'
    },
    cardContents: {
      textAlign: 'center',    
    }
  });

function Timer (){
    const classes = useStyles();

    return (
        <Card className={classes.cardContents}>
            <CardContent>
              <Typography variant="h5" component="h5">
                筋トレ
              </Typography>
              <Table>
                <TableBody>
                  <TableRow>
                    <TableCell>1</TableCell>
                    <TableCell>
                      <TextField defaultValue="10" 
                        InputProps={{
                          endAdornment: 
                          <InputAdornment position="end">秒</InputAdornment>,
                      }}/>
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>2</TableCell>
                    <TableCell>
                      <TextField defaultValue="10" 
                        InputProps={{
                          endAdornment: 
                          <InputAdornment position="end">秒</InputAdornment>,
                      }}/>
                    </TableCell>                    
                  </TableRow>
                </TableBody>
              </Table>
              <Button>スタート</Button>
            </CardContent>
          </Card>          
        )
}

export default Timer