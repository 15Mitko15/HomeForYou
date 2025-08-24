import { createContext, useContext, useState, ReactNode } from "react";
import { useAsync } from "../hooks/useAsync";
import { cityService } from "../services/city";
import { CitySchema } from "../schemas/citySchemas";

type CitiesContextType = {
  cities: CitySchema[];
  reload: () => void;
};

const CitiesContext = createContext<CitiesContextType | undefined>(undefined);

export const CitiesProvider = ({ children }: { children: ReactNode }) => {
  const [cities, setCities] = useState<CitySchema[]>([]);

  const { reload } = useAsync(async () => {
    const res = await cityService.getAllCities();
    setCities(res.result);
  }, []);

  return (
    <CitiesContext.Provider value={{ cities, reload }}>
      {children}
    </CitiesContext.Provider>
  );
};

export const useCities = () => {
  const ctx = useContext(CitiesContext);
  if (!ctx) throw new Error("useCities must be used inside CitiesProvider");
  return ctx;
};
