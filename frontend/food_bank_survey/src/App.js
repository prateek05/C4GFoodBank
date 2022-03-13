import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Survey from "./components/Survey";
import SignIn from "./components/SignIn";

function App() {
  return (
    <Router>
      <Routes>
      <Route path='*' element={<SignIn />} />
        <Route path="/" element={<SignIn />} />
        <Route path="/survey/:campaing/:site" element={<Survey />} />
      </Routes>
    </Router>
  );
}

export default App;
