import { Box, Typography } from "@mui/material";
import ErrorOutlineIcon from "@mui/icons-material/ErrorOutline";
import { makeStyles } from "./make-styles";

interface ErrorContainerProps {
  message: string;
}

const styles = makeStyles({
  boxStyles: {
    display: "flex",
    alignItems: "center",
    gap: 1,
    p: 2,
    mt: 2,
    borderRadius: 2,
    backgroundColor: "error.main",
    color: "white",
  },
});

export function ErrorContainer({ message }: ErrorContainerProps) {
  if (!message) {
    return null;
  }

  return (
    <Box sx={styles.boxStyles}>
      <ErrorOutlineIcon />
      <Typography variant="body1">{message}</Typography>
    </Box>
  );
}
