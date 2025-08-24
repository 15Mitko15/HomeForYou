import { NeighborhoodSchema } from "../schemas/neighborhoodSchemas";
import { http } from "./http";

export class NeighborhoodService {
  async getAllNeighborhoods() {
    return await http.get<NeighborhoodSchema[]>("/neighborhoods", {});
  }

  async getNeighborhoodById(id: number) {
    return await http.get<NeighborhoodSchema>(`/neighborhoods/${id}`, {});
  }

  async getNeighborhoodsByCity(cityId: number) {
    return await http.get<NeighborhoodSchema[]>(
      `/cities/${cityId}/neighborhoods`,
      {}
    );
  }
}

export const neighborhoodService = new NeighborhoodService();
