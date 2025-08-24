/* eslint-disable no-unused-vars */
export interface User {
  userId: number;
  username: string;
  email: string;
}

export interface RegisterUser {
  username: string;
  email: string;
  password: string;
}

export enum UserRoles {
  Guest = "guest",
  User = "user",
}
