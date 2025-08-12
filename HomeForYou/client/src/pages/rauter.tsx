import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./home-page";
import LoginPage from "./login-page";
import RegisterPage from "./register-page";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </BrowserRouter>
  );
}
