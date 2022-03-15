import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import {
  Grid,
  Paper,
  TextField,
  Button,
  RadioGroup,
  FormControlLabel,
  Radio,
} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";

export default function Survey() {
  const api = axios.create({
    // baseURL: `https://22b386a2-2e76-45e8-8e4e-6cc4145b36d6.mock.pstmn.io/api/survey/`,
    baseURL: `http://ec2-3-91-49-197.compute-1.amazonaws.com/api/survey/`,
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

  const [campaign, setCampaign] = useState([]);
  const [currentQue, setCurrentQue] = useState({});
  const [currentQueNum, setCurrentQueNum] = useState(0);
  const [response, setResponse] = useState([]);
  const [currentAns, setCurrentAns] = useState({ value: "" });
  const [dataLoad, setDataLoad] = useState(false);
  const [error, setError] = useState(false);
  const [completeFlag, setCompleteFlag] = useState(false);

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
      setResponse([answer, ...response]);
      setCurrentQueNum(nextNum);
      setCurrentQue(campaign[nextNum]);
      setCurrentAns({ value: "" });
    } else {
      setCompleteFlag(true);
      const finalAnswer = [answer, ...response];
      api.post(
        campaignId + `/` + siteId,
        finalAnswer
      );
    }
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
        lat: 0,
        lng: 0,
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
  }, []);
  return (
    <Grid
      container
      spacing={{ xs: 0, sm: 0, md: 0 }}
      columns={{ xs: 2, sm: 8, md: 12 }}
      align="center"
    >
      <Grid item xs={12} sm={12} md={12}>
        {dataLoad && !completeFlag && (
          <Paper style={{ height: "75vh", ...paperStyle }} elevation={10}>
            <Grid align="center" style={{ height: "15vh" }}>
              <h2>{currentQue.question}</h2>
            </Grid>
            <Grid
              container
              align="center"
              spacing={1}
              style={{ height: "25vh" }}
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
                  alignItems="center"
                >
                  <RadioGroup
                    aria-labelledby="demo-radio-buttons-group-label"
                    name="radio-buttons-group"
                    onChange={(e) => setCurrentAns({ value: e.target.value })}
                    key={currentQue.question_id}
                  >
                    {currentQue.answer_choices
                      .split(",")
                      .map((choice, index) => {
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
            >
              <Button
                onClick={gotoNextQue}
                variant="contained"
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
          <Paper style={{ height: "75vh", ...paperStyle }} elevation={10}>
            <Grid
              container
              direction="row"
              justifyContent="center"
              alignItems="center"
            >
              <h1>Please wait for the survey to load.</h1>
            </Grid>
          </Paper>
        )}
        {error && (
          <Paper style={{ height: "75vh", ...paperStyle }} elevation={10}>
            <Grid
              container
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
