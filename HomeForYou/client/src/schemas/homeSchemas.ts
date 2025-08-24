import z from "zod";

export const homeSchema = z.object({
  city: z.number().optional(),
  neighborhood: z.number().optional(),
  price: z.preprocess(
    (val) => (val ? Number(val) : undefined),
    z.number().positive().optional()
  ),
});

export type HomeSchema = z.infer<typeof homeSchema>;
