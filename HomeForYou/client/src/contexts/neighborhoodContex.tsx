import { createContext, useContext, useState, ReactNode } from "react";
import { useAsync } from "../hooks/useAsync";
import { neighborhoodService } from "../services/neighborhood";
import { NeighborhoodSchema } from "../schemas/neighborhoodSchemas";

type NeighborhoodsContextType = {
  neighborhoods: NeighborhoodSchema[];
  reload: () => void;
};

const NeighborhoodsContext = createContext<
  NeighborhoodsContextType | undefined
>(undefined);

export const NeighborhoodsProvider = ({
  children,
}: {
  children: ReactNode;
}) => {
  const [neighborhoods, setNeighborhoods] = useState<NeighborhoodSchema[]>([]);

  const { reload } = useAsync(async () => {
    const res = await neighborhoodService.getAllNeighborhoods();
    setNeighborhoods(res.result);
  }, []);

  return (
    <NeighborhoodsContext.Provider value={{ neighborhoods, reload }}>
      {children}
    </NeighborhoodsContext.Provider>
  );
};

export const useNeighborhoods = () => {
  const ctx = useContext(NeighborhoodsContext);
  if (!ctx)
    throw new Error(
      "useNeighborhoods must be used inside NeighborhoodsProvider"
    );
  return ctx;
};
