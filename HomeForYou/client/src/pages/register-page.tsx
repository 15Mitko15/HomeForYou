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
import { useForm, SubmitHandler } from "react-hook-form";
import { Link as RouterLink } from "react-router-dom";
import { RegisterUser } from "../schemas/userSchemas";
import { authService } from "../services/auth";
import { useAsyncAction } from "../hooks/useAsyncAction";
import { ErrorContainer } from "../components/errorContainer";

export default function RegisterPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterUser>();

  const { trigger, error } = useAsyncAction(async (data: RegisterUser) => {
    await authService.register(data);
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
            Register
          </Typography>
          <Typography
            variant="body1"
            color="text.secondary"
            align="center"
            sx={{ mb: 3 }}
          >
            Create your account to get started.
          </Typography>

          <form onSubmit={handleSubmit(trigger)}>
            <TextField
              fullWidth
              label="Username"
              margin="normal"
              {...register("username", { required: "Username is required" })}
              error={!!errors.username}
              helperText={errors.username?.message}
            />
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
              error={!!errors.username}
              helperText={errors.username?.message}
            />

            <Button
              fullWidth
              variant="contained"
              type="submit"
              sx={{ mt: 3, py: 1.5 }}
            >
              Register
            </Button>

            {!!error && (
              <ErrorContainer message="Something went wrong. Please try again." />
            )}
          </form>

          <Typography variant="body2" align="center" sx={{ mt: 3 }}>
            Already have an account?{" "}
            <Link component={RouterLink} to="/login" underline="hover">
              Login
            </Link>
          </Typography>
        </CardContent>
      </Card>
    </Container>
  );
}
