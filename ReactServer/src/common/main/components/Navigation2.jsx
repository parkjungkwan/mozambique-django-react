import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import RestoreIcon from '@mui/icons-material/Restore';
import FavoriteIcon from '@mui/icons-material/Favorite';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import { Link } from "react-router-dom"

const Navigation2 = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 500 }}>
      <BottomNavigation
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <Link to="/home" style={{width:50, margin:10}}>홈</Link>
        <Link to="/counter" style={{width:50, margin:10}}>카운터</Link>
        <Link to="/todos" style={{width:50, margin:10}}>할일</Link>
        <Link to="/signup" style={{width:70, margin:10}}>회원가입</Link>
        <Link to="/login" style={{width:50, margin:10}}>로그인</Link>
        <Link to="/stroke" style={{width:50, margin:10}}>뇌졸증</Link>
        <Link to="/iris" style={{width:50, margin:10}}>붓꽃</Link>
      </BottomNavigation>
    </Box>
  );
}

export default Navigation2