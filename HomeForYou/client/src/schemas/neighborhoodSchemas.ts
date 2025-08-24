import z from "zod";

const neighborhoodSchema = z.object({
  id: z.number(),
  name: z.string(),
  city_id: z.number(),
});

export type NeighborhoodSchema = z.infer<typeof neighborhoodSchema>;
