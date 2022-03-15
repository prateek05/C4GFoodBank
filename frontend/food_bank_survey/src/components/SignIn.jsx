import React, { useState } from "react";
import { Grid, Paper, TextField, Button } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import PollOutlinedIcon from "@mui/icons-material/PollOutlined";
import { useNavigate } from "react-router-dom";

function SignIn() {
  let navigate = useNavigate();
  const [surveyDetails, setSurveyDetails] = useState({
    campaign: "",
    site: "",
  });
  const isButtonDisabled = () => {
    if (surveyDetails.campaign === "" || surveyDetails.site === "") {
      return true;
    }
    return false;
  };
  const paperStyle = {
    padding: 20,
    height: "75vh",
    width: "80%",
    margin: "50px auto",
  };

  const iconStyle = {
    fontSize: 50,
  };

  const handleTextFieldInput = (e) => {
    setSurveyDetails({
      ...surveyDetails,
      [e.target.name]: e.target.value,
    });
  };
  return (
    <Grid
      container
      spacing={{ xs: 0, sm: 0, md: 0 }}
      columns={{ xs: 2, sm: 8, md: 12 }}
    >
      <Grid item xs={12} sm={12} md={12}>
        <Paper style={{ height: "38vh", ...paperStyle }} elevation={10}>
          <Grid align="center">
            <PollOutlinedIcon style={iconStyle}></PollOutlinedIcon>
            <h2>Survey</h2>
          </Grid>
          <Grid
            container
            justifyContent="center"
            alignItems="center"
            spacing={1}
          >
            <Grid item xs={8}>
              <TextField
                label="Campaign Code"
                placeholder="Enter the campaign code"
                fullWidth
                name="campaign"
                variant="standard"
                value={surveyDetails.campaign}
                onChange={handleTextFieldInput}
              />
            </Grid>
            <Grid item xs={8}>
              <TextField
                label="Site Code"
                name="site"
                placeholder="Enter the site code"
                fullWidth
                variant="standard"
                value={surveyDetails.site}
                onChange={handleTextFieldInput}
              />
            </Grid>

            <Grid item xs={8}>
              {/* <Link to={`/survey/${surveyDetails.survey}`}> */}
              <Button
                disabled={isButtonDisabled()}
                variant="contained"
                endIcon={<SendIcon />}
                onClick={() => {
                  navigate(
                    `/survey/${surveyDetails.campaign}/${surveyDetails.site}`
                  );
                }}
              >
                Go
              </Button>
              {/* </Link> */}
            </Grid>
          </Grid>
        </Paper>
      </Grid>
    </Grid>
  );
}

export default SignIn;
