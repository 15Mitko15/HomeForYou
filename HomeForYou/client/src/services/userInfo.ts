import { jwtDecode } from "jwt-decode";
import { LocalStorageServer } from "./localStorage";
import { config } from "../config";
import { User } from "../types/user";

type AuthHandler = (user: Omit<User, "password" | "email"> | null) => void;

export const LOCAL_STORAGE_USER = config.storage.user;

class UserInfoService {
  private handler: AuthHandler | null = null;
  private storage: LocalStorageServer<string>;

  constructor() {
    this.storage = new LocalStorageServer(LOCAL_STORAGE_USER);
  }

  setHandler(handler: AuthHandler | null) {
    this.handler = handler;
  }

  save(token: string) {
    const user = this.getUserFromToken(token);

    this.handler?.(user);

    this.storage.set(token);
  }

  clear() {
    this.handler?.(null);

    this.storage.clear();
  }

  get initialUser() {
    const token = this.storage.get();

    if (!token) {
      return null;
    }

    return this.getUserFromToken(token);
  }

  get authToken() {
    return this.storage.get();
  }

  private getUserFromToken(token: string): Omit<User, "password" | "email"> {
    const decoded = jwtDecode(token) as User;

    return {
      userId: decoded.userId,
      username: decoded.username,
    };
  }

  checkIfTokenIsValid() {
    const token = this.storage.get();

    if (!token) {
      return false;
    }

    const decodedToken = jwtDecode(token) as { exp: number };

    return decodedToken.exp * 1000 > Date.now();
  }
}

export const userInfoService = new UserInfoService();
