import z from "zod";

const citySchema = z.object({
  id: z.number(),
  name: z.string(),
});

export type CitySchema = z.infer<typeof citySchema>;
