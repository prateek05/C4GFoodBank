import React from "react";
import { Grid, Paper, TextField, Button, Stack } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import PollOutlinedIcon from "@mui/icons-material/PollOutlined";
import LoginOutlinedIcon from '@mui/icons-material/LoginOutlined';
import {Link} from 'react-router-dom'

function SignIn() {
  const values = {survey:''}
  const paperStyle = {
    padding: 20,
    // height: "vh",
    width: "80%",
    margin: "50px auto",
  };
  
  const iconStyle = {
    fontSize: 50,
  };
  return (
    <Grid
      container
      spacing={{ xs: 0, sm: 0, md: 0 }}
      columns={{ xs: 2, sm: 8, md: 12 }}
    >
      <Grid item xs={12} sm={4} md={6}>
        <Paper style={{ height: "38vh", ...paperStyle }} elevation={10}>
          <Grid align="center">
            <PollOutlinedIcon style={iconStyle}></PollOutlinedIcon>
            <h2>Survey</h2>
          </Grid>

          <TextField
            label="Survey Code"
            placeholder="Enter the survey code"
            fullWidth
            variant="standard"
            value={values.survey}
          />
          <Stack
            direction="row"
            justifyContent="flex-end"
            alignItems="flex-start"
            spacing={2}
            style={{ padding: 10 }}
          >
            <Link to={`/survey/${values.survey}`}>
            <Button variant="contained" endIcon={<SendIcon />} >
              Go
            </Button>
            </Link>
          </Stack>
        </Paper>
      </Grid>
      <Grid item xs={12} sm={4} md={6}>
        <Paper elevation={0} style={{ height: "30vh", ...paperStyle }}>
          <Grid align="center">
            <LoginOutlinedIcon style={iconStyle}/>
            <h2>Admin Sign In</h2>
          </Grid>

          <TextField
            label="Username"
            placeholder="Username"
            fullWidth
            variant="standard"
          />
          <TextField
            label="Password"
            placeholder="Password"
            type="password"
            fullWidth
            variant="standard"
          />
          <Stack
            direction="row"
            justifyContent="flex-end"
            alignItems="flex-start"
            spacing={2}
            style={{ padding: 10 }}
          >
            <Button variant="contained" endIcon={<SendIcon />}>
              Login
            </Button>
          </Stack>
        </Paper>
      </Grid>
    </Grid>
  );
}

export default SignIn;
