import { CitiesProvider } from "./contexts/citiesContext";
import { CurrentUserProvider } from "./contexts/CurrentUser";
import { NeighborhoodsProvider } from "./contexts/neighborhoodContex";
import { PropertiesProvider } from "./contexts/propertiesContext";
import Router from "./pages/rauter";

import { BrowserRouter } from "react-router-dom";

export function App() {
  return (
    <CurrentUserProvider>
      <CitiesProvider>
        <NeighborhoodsProvider>
          <PropertiesProvider>
            <Router />
          </PropertiesProvider>
        </NeighborhoodsProvider>
      </CitiesProvider>
    </CurrentUserProvider>
  );
}
