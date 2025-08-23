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
} from "@mui/material";
import { makeStyles } from "../components/make-styles";

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
  const { register, handleSubmit } = useForm();

  const onSubmit = (data: any) => {
    console.log("Search Data:", data);
  };

  const listings = [
    {
      id: 1,
      title: "Modern Apartment in City Center",
      price: "$1,200/mo",
      img: "https://via.placeholder.com/400x250",
    },
    {
      id: 2,
      title: "Cozy Suburban House",
      price: "$250,000",
      img: "https://via.placeholder.com/400x250",
    },
    {
      id: 3,
      title: "Luxury Villa with Pool",
      price: "$1,500,000",
      img: "https://via.placeholder.com/400x250",
    },
  ];

  return (
    <Box>
      {/* Hero Section */}
      <Box sx={styles.heroBox}>
        <Typography variant="h2" fontWeight="bold">
          Find Your Dream Home
        </Typography>
        <Typography variant="h5" sx={{ mt: 2 }}>
          Buy or rent the perfect place for you
        </Typography>

        {/* Search Form */}
        <Container sx={styles.searchContainer}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <Table>
              <TableBody>
                <TableRow>
                  <TableCell sx={styles.noBorderCell}>
                    <TextField
                      fullWidth
                      label="Location"
                      {...register("location")}
                    />
                  </TableCell>
                  <TableCell sx={styles.noBorderCell}>
                    <TextField
                      select
                      fullWidth
                      label="Type"
                      defaultValue="buy"
                      {...register("type")}
                    >
                      <MenuItem value="buy">Buy</MenuItem>
                      <MenuItem value="rent">Rent</MenuItem>
                    </TextField>
                  </TableCell>
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
                    >
                      Search
                    </Button>
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
        <Table>
          <TableBody>
            {listings.map((listing) => (
              <TableRow key={listing.id}>
                <TableCell sx={{ ...styles.noBorderCell, width: "250px" }}>
                  <Card>
                    <CardMedia
                      component="img"
                      height="150"
                      image={listing.img}
                      alt={listing.title}
                    />
                  </Card>
                </TableCell>
                <TableCell sx={styles.noBorderCell}>
                  <CardContent>
                    <Typography variant="h6">{listing.title}</Typography>
                    <Typography variant="body2" color="text.secondary">
                      {listing.price}
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
