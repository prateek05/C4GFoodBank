import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import axios from "axios";
import {
  Button,
  FormControlLabel,
  Grid,
  Paper,
  Radio,
  RadioGroup,
  TextField,
  Typography,
} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";

export default function Survey() {
  const api = axios.create({
    // TODO - In future, move the baseURL to an env file - making it a configuration, so that it is easy to make changes in different evironments.

    baseURL: `https://c4gfoodbank.azurewebsites.net/api/survey`,
  });

  const { campaignId, siteId } = useParams();
  const paperStyle = {
    padding: 20,
    // height: "vh",
    width: "80%",
    margin: "50px auto",
  };
  const [location, setLocation] = useState({
    loaded: false,
    error: false,
    coords: { lat: "", lng: "" },
  });

  const theme = createTheme();

  theme.typography.h3 = {
    fontSize: "1.2rem",
    "@media (min-width:600px)": {
      fontSize: "1.5rem",
    },
    [theme.breakpoints.up("md")]: {
      fontSize: "2rem",
    },
  };

  const [campaign, setCampaign] = useState([]);
  const [currentQue, setCurrentQue] = useState({});
  const [currentQueNum, setCurrentQueNum] = useState(0);

  const [currentAns, setCurrentAns] = useState({ value: "" });
  const [dataLoad, setDataLoad] = useState(false);
  const [error, setError] = useState(false);
  const [completeFlag, setCompleteFlag] = useState(false);
  const [disable, setDisable] = useState(true);

  const initSurvey = async () => {
    api
      .get(campaignId + `/` + siteId)
      .then((returnedResponse) => {
        const data = returnedResponse.data;
        setCampaign(data);

        if (data) {
          setDataLoad(true);
          setCurrentQueNum(0);
          setCurrentQue(data[0]);
        }
      })
      .catch((error) => {
        setError(true);
      });
  };
  const gotoNextQue = (e) => {
    e.preventDefault();

    const loc = location.coords.lat
      ? location.coords.lat + ", " + location.coords.lng
      : null;

    const answer = {
      question_id: currentQue.question_id,
      value: currentAns.value,
      language: currentQue.language,
      coordinates: loc,
    };

    const nextNum = currentQueNum + 1;
    if (nextNum < campaign.length) {
      setCurrentQueNum(nextNum);
      setCurrentQue(campaign[nextNum]);
      setCurrentAns({ value: "" });
    } else {
      setCompleteFlag(true);
    }
    api.post(campaignId + `/` + siteId, answer);
  };
  const onLocSuccess = (location) => {
    setLocation({
      loaded: true,
      error: false,
      coords: {
        lat: location.coords.latitude,
        lng: location.coords.longitude,
      },
    });
  };
  const onLocError = (err) => {
    setLocation({
      loaded: true,
      error: true,
      coords: {
        lat: null,
        lng: null,
      },
    });
  };

  const handleTextFieldInput = (e) => {
    setCurrentAns({ value: e.target.value });
  };

  useEffect(() => {
    if (!("geolocation" in navigator)) {
      onLocError("error");
    }
    navigator.geolocation.getCurrentPosition(onLocSuccess, onLocError);
  }, []);

  useEffect(() => {
    initSurvey();
    // eslint-disable-next-line
  }, []);
  useEffect(() => {
    currentQue.answer_template === "text" || currentAns.value !== ""
      ? setDisable(false)
      : setDisable(true);
  }, [currentAns, currentQue.answer_template]);

  return (
    <Grid
      container
      direction="column"
      justifyContent="space-evenly"
      alignItems="center"
      spacing={{ xs: 0, sm: 0, md: 0 }}
      columns={{ xs: 2, sm: 8, md: 12 }}
      align="center"
    >
      <Grid item xs={12} sm={12} md={12}>
        {dataLoad && !completeFlag && (
          <Paper style={{ minHeight: "75vh", ...paperStyle }} elevation={10}>
            <Grid item align="center">
              <ThemeProvider theme={theme}>
                <Typography variant="h3">{currentQue.question}</Typography>
              </ThemeProvider>
            </Grid>
            {currentQue.additional_info && (
              <Grid item align="center">
                <ThemeProvider theme={theme}>
                  <Typography variant="p">
                    {currentQue.additional_info}
                  </Typography>
                </ThemeProvider>
              </Grid>
            )}
            <Grid
              item
              container
              align="center"
              spacing={1}
              // style={{ height: "25vh" }}
            >
              {currentQue.answer_template === "text" && (
                <TextField
                  label=""
                  placeholder="Enter your response"
                  fullWidth
                  variant="standard"
                  value={currentAns.value}
                  onChange={handleTextFieldInput}
                />
              )}
              {currentQue.answer_template === "radio" && (
                <Grid
                  container
                  direction="column"
                  justifyContent="flex-start"
                  align="left"
                  item
                >
                  <RadioGroup
                    aria-labelledby="radio-answer-options"
                    name="radio-buttons-group"
                    onChange={(e) => setCurrentAns({ value: e.target.value })}
                    key={currentQue.question_id}
                  >
                    {currentQue.answer_choices.map((choice, index) => {
                      return (
                        <FormControlLabel
                          value={choice}
                          key={index + Math.random()}
                          control={<Radio />}
                          label={choice}
                        />
                      );
                    })}
                  </RadioGroup>
                </Grid>
              )}
            </Grid>
            <Grid
              container
              direction="row"
              justifyContent="center"
              alignItems="center"
              item
            >
              <Button
                onClick={gotoNextQue}
                variant="contained"
                disabled={disable}
                style={{ marginTop: "12px" }}
                endIcon={<SendIcon />}
              >
                Continue
              </Button>
            </Grid>
          </Paper>
        )}
        {dataLoad && completeFlag && (
          <Paper style={{ height: "75vh", ...paperStyle }} elevation={10}>
            <Grid
              container
              direction="row"
              justifyContent="center"
              alignItems="center"
            >
              <h1>Thank you for your response!</h1>
            </Grid>
          </Paper>
        )}
        {!dataLoad && !error && (
          // <Paper style={{ height: "75vh", ...paperStyle }} elevation={10}>
          <Grid
            item
            direction="row"
            justifyContent="center"
            alignItems="center"
          >
            <h1>Please wait for the survey to load.</h1>
          </Grid>
          // </Paper>
        )}
        {error && (
          <Paper style={{ height: "75vh", ...paperStyle }} elevation={10}>
            <Grid
              item
              direction="row"
              justifyContent="center"
              alignItems="center"
            >
              <h1>This survey does not exist.</h1>
            </Grid>
          </Paper>
        )}
      </Grid>
    </Grid>
  );
}
