import { createContext, useContext, useState, ReactNode } from "react";
import { propertyService } from "../services/proprty";
import { useAsync } from "../hooks/useAsync";
import { PropertySchema } from "../schemas/propertySchema";

type PropertiesContextType = {
  properties: PropertySchema[];
  reload: () => void;
};

const PropertiesContext = createContext<PropertiesContextType | undefined>(
  undefined
);

export const PropertiesProvider = ({ children }: { children: ReactNode }) => {
  const [properties, setProperties] = useState<PropertySchema[]>([]);

  const { reload } = useAsync(async () => {
    const res = await propertyService.getAllProperties();
    setProperties(res.result);
  }, []);

  return (
    <PropertiesContext.Provider value={{ properties, reload: reload }}>
      {children}
    </PropertiesContext.Provider>
  );
};

export const useProperties = (): PropertiesContextType => {
  const ctx = useContext(PropertiesContext);
  if (!ctx)
    throw new Error("useProperties must be used inside PropertiesProvider");
  return ctx;
};
