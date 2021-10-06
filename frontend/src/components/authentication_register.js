import LockOpenIcon from '@material-ui/icons/LockOpen';
import LockIcon from '@material-ui/icons/Lock';
import BackupIcon from '@material-ui/icons/Backup';
import PublishIcon from '@material-ui/icons/Publish';
import Button from '@material-ui/core/Button';

function AuthenticationRegister(){

    return(
        <>
          <span>
            <Button>
              <LockIcon />Logout
            </Button>
            <Button>
              <BackupIcon />データを保存する
            </Button>
            <Button>
              <PublishIcon />データを取得する
            </Button>                         
          </span>            
            {/* :
          <div>                                  
            <Button>
              ログイン<LockOpenIcon />
            </Button>                 
          </div>  */}
        </> 
    )

}

export default AuthenticationRegister
