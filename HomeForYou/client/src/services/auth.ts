import { AuthError } from "../errors";
import { LogUser, RegisterUser } from "../schemas/userSchemas";
import { http } from "./http";
import { userInfoService } from "./userInfo";

class AuthService {
  async register(body: RegisterUser) {
    await http.post("/auth/register", { body });
  }

  logout() {
    userInfoService.clear();
  }

  async login(body: LogUser) {
    const { headers } = await http.post("/auth/login", {
      body,
    });

    const bearerToken = headers.get("authorization");

    if (!bearerToken) {
      throw new AuthError();
    }

    this.saveToken(bearerToken);
  }

  private saveToken(bearerToken: string) {
    const token = bearerToken?.replace("Bearer ", "");
    userInfoService.save(token);
  }
}

export const authService = new AuthService();
