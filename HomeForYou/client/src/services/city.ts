import { CitySchema } from "../schemas/citySchemas";
import { http } from "./http";

export class CityService {
  async getAllCities() {
    return await http.get<CitySchema[]>("/cities", {});
  }

  async getCityById(id: number) {
    return await http.get<CitySchema>(`/cities/${id}`, {});
  }
}

export const cityService = new CityService();
