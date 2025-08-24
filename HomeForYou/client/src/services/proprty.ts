import {
  PropertyCreationSchema,
  PropertySchema,
} from "../schemas/propertySchema";
import { http } from "./http";

export class PropertyService {
  async getAllProperties(): Promise<{
    result: PropertySchema[];
    headers: Headers;
  }> {
    return await http.get<PropertySchema[]>("/property", {});
  }
  async getPropertyById(id: number) {
    return await http.get<PropertySchema>(`/property/${id}`, {});
  }

  async createNewProperty(body: PropertyCreationSchema) {
    return await http.post<PropertySchema>(`/property/add`, { body });
  }
}

export const propertyService = new PropertyService();
