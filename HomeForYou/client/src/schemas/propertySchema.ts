import z from "zod";

const propertyCreationSchema = z.object({
  description: z.string(),
  price: z.number(),
  area: z.number(),
  neighborhood_id: z.number(),
  user_id: z.number(),
});

export type PropertyCreationSchema = z.infer<typeof propertyCreationSchema>;

const propertySchema = z.object({
  id: z.number(),
  description: z.string(),
  price: z.number(),
  area: z.number(),
  neighborhood_id: z.number(),
  user_id: z.number(),
});

export type PropertySchema = z.infer<typeof propertySchema>;
