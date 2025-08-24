import { useForm } from "react-hook-form";
import {
  Box,
  Button,
  Card,
  CardContent,
  CardMedia,
  Container,
  MenuItem,
  Table,
  TableBody,
  TableCell,
  TableRow,
  TextField,
  Typography,
  CircularProgress,
} from "@mui/material";
import { makeStyles } from "../components/make-styles";
import { useNeighborhoods } from "../contexts/neighborhoodContex";
import { useCities } from "../contexts/citiesContext";
import { useState, useMemo } from "react";
import { HomeSchema } from "../schemas/homeSchemas";
import { useProperties } from "../contexts/propertiesContext";

const styles = makeStyles({
  heroBox: {
    backgroundSize: "cover",
    backgroundPosition: "center",
    textAlign: "center",
    py: 10,
    width: "100%",
  },
  searchContainer: {
    mt: 4,
    backgroundColor: "rgba(255,255,255,0.85)",
    p: 3,
    borderRadius: 2,
    maxWidth: 900,
    mx: "auto",
  },
  featuredContainer: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    py: 6,
    maxWidth: 900,
    mx: "auto",
  },
  noBorderCell: {
    borderBottom: "none",
  },
});

export default function HomePage() {
  const { register, handleSubmit, watch } = useForm<HomeSchema>();
  const [filters, setFilters] = useState<HomeSchema>({});

  const { cities } = useCities();
  const { neighborhoods } = useNeighborhoods();
  const { properties } = useProperties();

  const selectedCityId = watch("city");

  const filteredProperties = useMemo(() => {
    return properties.filter((p) => {
      if (filters.city && p.neighborhood_id) {
        const n = neighborhoods.find((n) => n.id === p.neighborhood_id);
        if (n?.city_id !== filters.city) return false;
      }
      if (filters.neighborhood && p.neighborhood_id !== filters.neighborhood) {
        return false;
      }
      if (filters.price && p.price > filters.price) {
        return false;
      }
      return true;
    });
  }, [filters, properties, neighborhoods]);

  const onSubmit = (data: HomeSchema) => {
    setFilters(data);
  };

  return (
    <Box>
      <Box sx={styles.heroBox}>
        <Typography variant="h2" fontWeight="bold">
          Find Your Dream Home
        </Typography>
        <Typography variant="h5" sx={{ mt: 2 }}>
          Buy or rent the perfect place for you
        </Typography>

        <Container sx={styles.searchContainer}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <Table>
              <TableBody>
                <TableRow>
                  <TableCell sx={styles.noBorderCell}>
                    <TextField
                      select
                      fullWidth
                      label="City"
                      {...register("city")}
                    >
                      {cities.map((city) => (
                        <MenuItem key={city.id} value={city.id}>
                          {city.name}
                        </MenuItem>
                      ))}
                    </TextField>
                  </TableCell>

                  {selectedCityId && (
                    <TableCell sx={styles.noBorderCell}>
                      <TextField
                        select
                        fullWidth
                        label="Neighborhood"
                        {...register("neighborhood")}
                      >
                        {neighborhoods
                          .filter((n) => n.city_id === selectedCityId)
                          .map((n) => (
                            <MenuItem key={n.id} value={n.id}>
                              {n.name}
                            </MenuItem>
                          ))}
                      </TextField>
                    </TableCell>
                  )}

                  <TableCell sx={styles.noBorderCell}>
                    <TextField
                      fullWidth
                      label="Max Price"
                      {...register("price")}
                    />
                  </TableCell>

                  <TableCell sx={{ ...styles.noBorderCell, width: "1%" }}>
                    <Button
                      variant="contained"
                      type="submit"
                      sx={{ height: "100%" }}
                    />
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </form>
        </Container>
      </Box>

      <Container sx={styles.featuredContainer}>
        <Typography variant="h4" fontWeight="bold" gutterBottom>
          Featured Listings
        </Typography>

        {filteredProperties.length === 0 && (
          <Typography>No properties found.</Typography>
        )}

        <Table>
          <TableBody>
            {filteredProperties.map((property) => (
              <TableRow key={property.id}>
                <TableCell sx={{ ...styles.noBorderCell, width: "250px" }}>
                  <Card>
                    <CardMedia
                      component="img"
                      height="150"
                      image={"https://via.placeholder.com/400x250"}
                      alt={property.description}
                    />
                  </Card>
                </TableCell>
                <TableCell sx={styles.noBorderCell}>
                  <CardContent>
                    <Typography variant="h6">{property.description}</Typography>
                    <Typography variant="body2" color="text.secondary">
                      ${property.price}
                    </Typography>
                  </CardContent>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Container>
    </Box>
  );
}
