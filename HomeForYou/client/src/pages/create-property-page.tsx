import {
  Button,
  Card,
  CardContent,
  CircularProgress,
  Container,
  MenuItem,
  TextField,
  Typography,
} from "@mui/material";
import { useForm } from "react-hook-form";
import { useAsyncAction } from "../hooks/useAsyncAction";
import { PropertyCreationSchema } from "../schemas/propertySchema";
import { ErrorContainer } from "../components/errorContainer";
import { propertyService } from "../services/proprty";
import { useCurrentUser } from "../contexts/CurrentUser";
import { useCities } from "../contexts/citiesContext";
import { useNeighborhoods } from "../contexts/neighborhoodContex";

export default function CreatePropertyPage() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<PropertyCreationSchema>();

  const user = useCurrentUser();

  const { trigger, error, loading } = useAsyncAction(
    async (data: PropertyCreationSchema) => {
      await propertyService.createNewProperty({
        ...data,
        user_id: user?.userId ?? 1,
      });
    }
  );

  const selectedCity = watch("area");

  const { cities } = useCities();
  const { neighborhoods } = useNeighborhoods();

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
            Post property
          </Typography>
          <Typography
            variant="body1"
            color="text.secondary"
            align="center"
            sx={{ mb: 3 }}
          >
            Fill out the details of your new property.
          </Typography>

          <form onSubmit={handleSubmit(trigger)}>
            <TextField
              fullWidth
              label="Description"
              margin="normal"
              {...register("description", {
                required: "Description is required",
              })}
              error={!!errors.description}
              helperText={errors.description?.message}
            />

            <TextField
              fullWidth
              label="Price"
              type="number"
              margin="normal"
              {...register("price", {
                required: "Price is required",
                min: { value: 1, message: "Price must be greater than 0" },
              })}
              error={!!errors.price}
              helperText={errors.price?.message}
            />

            <TextField
              select
              fullWidth
              label="City"
              margin="normal"
              {...register("area", { required: "City is required" })}
              error={!!errors.area}
              helperText={errors.area?.message}
            >
              {cities.map((city) => (
                <MenuItem key={`tag-${city.id}`} value={city.id}>
                  {city.name}
                </MenuItem>
              ))}
            </TextField>

            {selectedCity && (
              <TextField
                select
                fullWidth
                label="Neighborhood"
                margin="normal"
                {...register("neighborhood_id", {
                  required: "Neighborhood is required",
                })}
                error={!!errors.neighborhood_id}
                helperText={errors.neighborhood_id?.message}
              >
                {neighborhoods
                  .filter(({ city_id }) => city_id === selectedCity)
                  .map((neighborhood) => (
                    <MenuItem key={neighborhood.id} value={neighborhood.id}>
                      {neighborhood.name}
                    </MenuItem>
                  ))}
              </TextField>
            )}

            <Button
              fullWidth
              variant="contained"
              type="submit"
              sx={{ mt: 3, py: 1.5 }}
              disabled={loading}
            >
              {loading ? <CircularProgress size={24} /> : "Create Property"}
            </Button>

            {!!error && (
              <ErrorContainer message="Something went wrong while creating the property." />
            )}
          </form>
        </CardContent>
      </Card>
    </Container>
  );
}
