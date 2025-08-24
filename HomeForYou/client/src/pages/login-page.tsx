import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  TextField,
  Typography,
  Link,
} from "@mui/material";
import { useForm } from "react-hook-form";
import { Link as RouterLink } from "react-router-dom";
import { authService } from "../services/auth";
import { useAsyncAction } from "../hooks/useAsyncAction";
import { LogUser } from "../schemas/userSchemas";
import { ErrorContainer } from "../components/errorContainer";

export default function LoginPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LogUser>();

  const { trigger, error } = useAsyncAction(async (data: LogUser) => {
    await authService.login(data);
  });

  return (
    <Container
      maxWidth="sm"
      sx={{ display: "flex", alignItems: "center", minHeight: "100vh" }}
    >
      <Card sx={{ width: "100%", boxShadow: 4, borderRadius: 3 }}>
        <CardContent sx={{ p: 4 }}>
          <Typography
            variant="h4"
            fontWeight="bold"
            gutterBottom
            align="center"
          >
            Login
          </Typography>
          <Typography
            variant="body1"
            color="text.secondary"
            align="center"
            sx={{ mb: 3 }}
          >
            Welcome back! Please login to your account.
          </Typography>

          <form onSubmit={handleSubmit(trigger)}>
            <TextField
              fullWidth
              label="Email"
              type="email"
              margin="normal"
              {...register("email", { required: "Email is required" })}
              error={!!errors.email}
              helperText={errors.email?.message}
            />
            <TextField
              fullWidth
              label="Password"
              type="password"
              margin="normal"
              {...register("password", { required: "Password is required" })}
              error={!!errors.email}
              helperText={errors.email?.message}
            />

            <Button
              fullWidth
              variant="contained"
              type="submit"
              sx={{ mt: 3, py: 1.5 }}
            >
              Login
            </Button>

            {!!error && (
              <ErrorContainer message="Email or password are incorrect. Please try again." />
            )}
          </form>

          <Typography variant="body2" align="center" sx={{ mt: 3 }}>
            Don’t have an account?{" "}
            <Link component={RouterLink} to="/register" underline="hover">
              Register
            </Link>
          </Typography>
        </CardContent>
      </Card>
    </Container>
  );
}
