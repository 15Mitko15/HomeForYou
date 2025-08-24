import z from "zod";

const registerUser = z.object({
  username: z.string(),
  email: z.email(),
  password: z.string(),
});

export type RegisterUser = z.infer<typeof registerUser>;

const logUser = z.object({
  email: z.email(),
  password: z.string(),
});

export type LogUser = z.infer<typeof logUser>;
