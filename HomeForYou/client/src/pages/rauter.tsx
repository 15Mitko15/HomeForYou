import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./home-page";
import LoginPage from "./login-page";
import RegisterPage from "./register-page";
import CreatePropertyPage from "./create-property-page";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/create" element={<CreatePropertyPage />} />
      </Routes>
    </BrowserRouter>
  );
}
