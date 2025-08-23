import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    primary: {
      main: "#4a6fa5",
    },
    secondary: {
      main: "#d4a373",
    },
    background: {
      default: "#f4f1ee",
      paper: "#ffffff",
    },
    text: {
      primary: "#2f2f2f",
      secondary: "#555555",
    },
  },
  typography: {
    fontFamily: "system-ui, Avenir, Helvetica, Arial, sans-serif",
  },
});
